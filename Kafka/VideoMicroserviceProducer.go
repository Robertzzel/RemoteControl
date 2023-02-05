package Kafka

import "github.com/confluentinc/confluent-kafka-go/kafka"

type VideoMicroserviceProducer struct {
	*ProducerWrapper
	deliverChannel chan kafka.Event
	topic          string
}

func (producer *VideoMicroserviceProducer) Publish(message []byte, headers []kafka.Header) error {
	return producer.ProducerWrapper.Publish(message, headers, producer.topic, AggregatorMicroservicePartition, producer.deliverChannel)
}

func NewVideoMicroserviceProducer(brokerAddress, topic string) (*VideoMicroserviceProducer, error) {
	p, err := kafka.NewProducer(&kafka.ConfigMap{
		"bootstrap.servers": brokerAddress,
		"client.id":         "-",
		"acks":              "all",
	})
	if err != nil {
		return nil, err
	}

	return &VideoMicroserviceProducer{topic: topic, ProducerWrapper: &ProducerWrapper{p}, deliverChannel: make(chan kafka.Event, 5)}, nil
}