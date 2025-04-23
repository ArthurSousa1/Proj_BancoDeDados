// kafka.js
const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'my-producer',
  brokers: ['localhost:9091'], // endereço do broker Kafka
});

const producer = kafka.producer();

module.exports = producer;
