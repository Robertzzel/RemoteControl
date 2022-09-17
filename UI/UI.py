import os.path
import sys, asyncio, websockets
import webbrowser

FRONTEND_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Security-Policy"  content="connect-src * 'unsafe-inline';">
</head>
<body>
  <div class="col align-self-center">
    <video playsinline muted controls preload="none" width="100%"></video>
  </div>
  
  <script>
    let queue = []
    let video = document.querySelector('video');
    let webSocket   = null;
    let sourceBuffer = null;
    let streamingStarted = false;
    let ms = new MediaSource();
    video.src = window.URL.createObjectURL(ms);
    const VIDEO_TYPE = 'video/mp4;codecs="avc1.64001e, mp4a.40.2"'
    const SOCKET_URL = `ws://localhost:8081`

    function initMediaSource() {
      video.onerror = () => {console.log("Media element error");}
      video.loop = false;
      video.addEventListener('canplay', (event) => {
        console.log('Video can start, but not sure it will play through.');
        video.play();
      });
      video.addEventListener('paused', (event) => {
        console.log('Video paused for buffering...');
        setTimeout(function() { video.play(); }, 2000);
      });

      ms.addEventListener('sourceopen', onMediaSourceOpen);

      function onMediaSourceOpen() {
        sourceBuffer = ms.addSourceBuffer(VIDEO_TYPE);
        sourceBuffer.mode = 'sequence';
        sourceBuffer.addEventListener("updateend",loadPacket);
        sourceBuffer.addEventListener("onerror", () => {console.log("Media source error");});
      }

      function loadPacket() {
        if (sourceBuffer.updating) {
          return
        }
        if (queue.length>0) {
          appendToBuffer(queue.shift());
        } else {
          streamingStarted = false;
        }
      }
    }

    function appendToBuffer(videoChunk) {
      if (videoChunk) {
        sourceBuffer.appendBuffer(videoChunk);
      }
    }

    function openWSConnection() {
      console.log("openWSConnection::Connecting to: " + SOCKET_URL);

      try {
        webSocket = new WebSocket(SOCKET_URL);
        webSocket.debug = true;
        webSocket.timeoutInterval = 3000;
        webSocket.onopen = function(openEvent) {
          console.log("WebSocket open");
        };
        webSocket.onclose = function (closeEvent) {
          console.log("WebSocket closed");
        };
        webSocket.onerror = function (errorEvent) {
          console.log("WebSocket ERROR: " + error);
        };
        webSocket.onmessage = async function (messageEvent) {
          let wsMsg = messageEvent.data.arrayBuffer();

          if (!streamingStarted) {
            appendToBuffer(await wsMsg);
            streamingStarted=true;
            return;
          }
          queue.push(await wsMsg);
        };
      } catch (exception) {
        console.error(exception);
      }
    }

    if (!window.MediaSource) {
      console.error("No Media Source API available");
    }

    if (!MediaSource.isTypeSupported(VIDEO_TYPE)) {
      console.error("Unsupported MIME type or codec: " + VIDEO_TYPE);
    }

    initMediaSource();
    openWSConnection();
  </script>
</body>
</html>
"""


async def main():
    if len(sys.argv) != 3:
        print("Error not using pattern: ./python3 UI.py <IP> <PORT>")
        return

    ip, port = sys.argv[1], int(sys.argv[2])
    reader, writer = await asyncio.open_connection(host=ip, port=port)

    webbrowser.open("file://" + os.path.realpath("UI.html"))

    async with websockets.serve(lambda ws: handle(ws, reader), "localhost", 8081):
        await asyncio.Future()


async def handle(websocket, reader):
    while True:
        print("Waiting for message..")
        size_buffer = b''
        while len(size_buffer) < 10:
            size_buffer += await reader.read(10 - len(size_buffer))

        size = int(size_buffer)

        buffer = b''
        while len(buffer) < size:
            buffer += await reader.read(size - len(buffer))

        print("Message received")
        await websocket.send(buffer)


if __name__ == "__main__":
    asyncio.run(main())