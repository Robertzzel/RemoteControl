package main

import (
	"Licenta/kafka"
	"errors"
	"fmt"
	"github.com/gordonklaus/portaudio"
	"strings"
	"time"
)

const (
	kafkaAudioTopic = "audio"
	kafkaSyncTopic  = "sync"
	secondsToRecord = 1.0 / 6
)

type AudioGeneratorService struct {
	sampleRate         float64
	numberOfChannels   int
	latency            time.Duration
	deviceNameToRecord string
	stream             *portaudio.Stream
	AudioBuffer        []byte
}

func NewAudioGeneratorService() (*AudioGeneratorService, error) {
	ags := &AudioGeneratorService{
		sampleRate:         44100,
		numberOfChannels:   1,
		latency:            0,
		deviceNameToRecord: "pulse",
	}

	ags.AudioBuffer = make([]byte, int(secondsToRecord*ags.sampleRate))

	err := ags.Initialize()
	if err != nil {
		return nil, err
	}

	info, err := ags.getPulseDeviceInfo()
	if err != nil {
		return nil, err
	}

	stream, err := ags.getAudioStream(info, ags.AudioBuffer)
	if err != nil {
		return nil, err
	}

	ags.stream = stream
	return ags, nil
}

func (ags *AudioGeneratorService) Initialize() error {
	if err := portaudio.Initialize(); err != nil {
		return err
	}
	return nil
}

func (ags *AudioGeneratorService) Terminate() error {
	if err := portaudio.Terminate(); err != nil {
		return err
	}
	return nil
}

func (ags *AudioGeneratorService) getPulseDeviceInfo() (*portaudio.DeviceInfo, error) {
	devices, err := portaudio.Devices()
	if err != nil {
		return nil, err
	}

	for _, device := range devices {
		if strings.Contains(device.Name, ags.deviceNameToRecord) {
			return device, nil
		}
	}

	return nil, errors.New("no pulse device found")
}

func (ags *AudioGeneratorService) getAudioStream(deviceInfo *portaudio.DeviceInfo, buffer []byte) (*portaudio.Stream, error) {
	stream, err := portaudio.OpenStream(
		portaudio.StreamParameters{
			Input: portaudio.StreamDeviceParameters{
				Device:   deviceInfo,
				Channels: ags.numberOfChannels,
				Latency:  ags.latency,
			},
			Output:     portaudio.StreamDeviceParameters{Device: nil},
			Flags:      portaudio.NoFlag,
			SampleRate: ags.sampleRate,
		},
		buffer,
	)
	if err != nil {
		return nil, err
	}

	return stream, nil
}

func (ags *AudioGeneratorService) recordStream() error {
	err := ags.stream.Start()
	if err != nil {
		return err
	}

	err = ags.stream.Read()
	if err != nil {
		return err
	}

	err = ags.stream.Stop()
	if err != nil {
		return err
	}

	return nil
}

func main() {
	err := kafka.CreateTopic(kafkaAudioTopic)
	if err != nil {
		fmt.Println(err)
	}
	err = kafka.CreateTopic(kafkaSyncTopic)
	if err != nil {
		fmt.Println(err)
	}

	kafkaAudioProducer := kafka.NewKafkaProducer(kafkaAudioTopic)

	service, err := NewAudioGeneratorService()
	if err != nil {
		fmt.Println(err)
		return
	}
	defer service.Terminate()

	for {
		err = service.recordStream()
		if err != nil {
			fmt.Println(err)
			return
		}

		go func() {
			err = kafkaAudioProducer.PublishWithTimestamp(service.AudioBuffer)
			if err != nil {
				fmt.Println(err)
				return
			}
		}()
	}
}