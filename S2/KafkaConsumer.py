from confluent_kafka import Consumer, KafkaException
import socket

# Configurações do consumidor
conf = {
    'bootstrap.servers': 'localhost:9091',
    'client.id': socket.gethostname(),
    'group.id': 'meu-grupo',
    'auto.offset.reset': 'earliest'  # Pode ser 'latest' ou 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['projetoDB'])

print("Consumindo mensagens... (CTRL+C para sair)")
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # Espera até 1 segundo por mensagens
        if msg is None:
            continue
        if msg.error():
            print("Erro: {}".format(msg.error()))
        else:
            print(f"Mensagem recebida: {msg.value().decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()