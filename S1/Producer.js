// index.js
const producer = require('./kafka');

const run = async () => {
  await producer.connect();

  const mensagem = {
    topic: 'topic1',
    messages: [
      { value: 'Olá Kafka!' },
      { value: 'Mensagem 2' },
    ],
  };

  await producer.send(mensagem);

  console.log('Mensagens enviadas com sucesso!');
  await producer.disconnect();
};

run().catch(console.error);
