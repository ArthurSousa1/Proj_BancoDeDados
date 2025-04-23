// consumer.js
const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'topic1',
  brokers: ['localhost:9091'],
});

const consumer = kafka.consumer({ groupId: 'grupo-exemplo' });

const run = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic: 'meu-topico', fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        value: message.value.toString(),
        partition,
        offset: message.offset,
      });
    },
  });
};

run().catch(console.error);
