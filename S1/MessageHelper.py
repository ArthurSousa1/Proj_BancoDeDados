from confluent_kafka import Producer
import socket
import json

# Criação do produtor
producer = Producer({
    'bootstrap.servers': 'localhost:9091',
    'client.id': socket.gethostname(),
    'acks': 'all',  
    'enable.idempotence': True
})

def send_message(message):
    message_bytes = json.dumps(message).encode('utf-8')
    producer.produce('projetoDB', key='valor', value=message_bytes, callback=delivery_report)
    producer.flush()


# Função de callback para erro
def delivery_report(err, msg):
    if err is not None:
        print(f"Mensagem falhou: {err}")
    else:
        print(f"Mensagem entregue para {msg.topic()} [{msg.partition()}]")