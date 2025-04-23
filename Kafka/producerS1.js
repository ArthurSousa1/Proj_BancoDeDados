const {Kafka} = require('kafka.js');

const kafka = new Kafka({
    clientId: 's1-simulador',
    brokers: ['localhost:9092']
});

const producer = Kafka.producer();

const connectProducer = async () => {
    await producer.connect();
}    

const sendEvent = async(message) => {
    await producer.send({
        topic: 'estoque-eventos',
        message: [
            {value: JSON.stringify(message)}
        ]
    });
};

module.exports = {connectProducer, sendEvent};

