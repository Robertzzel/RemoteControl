package main

import (
	"bytes"
	"context"
	"errors"
	"fmt"
	"github.com/icza/mjpeg"
	"golang.org/x/sync/errgroup"
	"log"
	"time"
)

type Recorder struct {
	screenshotTool      *Screenshot
	fps                 int
	width               int32
	height              int32
	imageBuffer         chan []byte
	VideoBuffer         chan string
	errorGroup          *errgroup.Group
	outContext          context.Context
	ctx                 context.Context
	contextCancellation context.CancelFunc
}

func NewRecorder(outContext context.Context, fps int) (*Recorder, error) {
	if fps > 60 && fps < 1 {
		return nil, errors.New("fps must be between 1 and 60")
	}

	screenshot, err := NewScreenshot()
	if err != nil {
		return nil, err
	}

	img, err := screenshot.Get()
	if err != nil {
		return nil, err
	}

	return &Recorder{
		screenshotTool:      screenshot,
		fps:                 fps,
		width:               int32(img.Width),
		height:              int32(img.Height),
		imageBuffer:         make(chan []byte, 256),
		VideoBuffer:         make(chan string, 10),
		errorGroup:          nil,
		outContext:          outContext,
		ctx:                 nil,
		contextCancellation: nil,
	}, nil
}

func (r *Recorder) Stop() {
	if r.contextCancellation != nil {
		r.contextCancellation()
	}
}

func (r *Recorder) Start(startTime time.Time, chunkSize time.Duration) {
	r.ctx, r.contextCancellation = context.WithCancel(r.outContext)
	r.errorGroup, r.ctx = errgroup.WithContext(r.ctx)

	r.errorGroup.Go(func() error {
		for time.Now().Before(startTime) && r.outContext.Err() == nil {
			time.Sleep(time.Now().Sub(startTime))
		}

		r.errorGroup.Go(r.startRecording)
		r.errorGroup.Go(func() error { return r.processImagesBuffer(startTime, chunkSize) })

		return r.errorGroup.Wait()
	})
}

func (r *Recorder) startRecording() error {
	ticker := time.NewTicker(time.Duration(int64(time.Second) / int64(r.fps)))
	var encodedImageBuffer = bytes.Buffer{}

	for r.outContext.Err() == nil {
		img, err := r.screenshotTool.Get()
		if err != nil {
			return err
		}

		encodedImageBuffer.Reset()
		if err = img.Compress(&encodedImageBuffer, 100); err != nil {
			return err
		}

		r.imageBuffer <- encodedImageBuffer.Bytes()
		<-ticker.C
	}

	return nil
}

func (r *Recorder) processImagesBuffer(startTime time.Time, chunkSize time.Duration) error {
	nextChunkEndTime := startTime

	for r.outContext.Err() == nil {
		nextChunkEndTime = nextChunkEndTime.Add(chunkSize)
		videoFileName := fmt.Sprintf("/tmp/%s.mkv", fmt.Sprint(nextChunkEndTime.Add(-chunkSize).UnixMilli()))
		video, err := mjpeg.New(videoFileName, r.width, r.height, int32(r.fps))
		if err != nil {
			fmt.Println("initing a video err", err.Error())
			return err
		}

		for r.outContext.Err() == nil && time.Now().Before(nextChunkEndTime) {
			if err = video.AddFrame(<-r.imageBuffer); err != nil {
				log.Println("Error adding frame to video file ", err)
				return err
			}
		}

		r.VideoBuffer <- videoFileName

		if err = video.Close(); err != nil {
			return err
		}
	}

	return nil
}
