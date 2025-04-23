const { connectProducer, sendEvent } = require('./kafka/producer');
const generateEvent = require('.../utils/generateEvent');

const main = async () => {
  await connectProducer();
  console.log('Produtor conectado ao Kafka.');

  setInterval(async () => {
    const event = generateEvent();
    await sendEvent(event);
    console.log('Evento enviado:', event);
  }, 3000); // envia a cada 3 segundos
};

main();