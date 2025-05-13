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

class KafkaConsumer:

    def iniciarConsumidor(self):
        print("Consumindo mensagens... (CTRL+C para sair)")
        try:
            while True:
                msg = consumer.poll(timeout=1.0)  # Espera até 1 segundo por mensagens
                if msg is None:
                    continue
                if msg.error():
                    print("Erro: {}".format(msg.error()))
                else:
                    self.validarMensagem(msg)
        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()
    
    def validarMensagem(self, message):
        # decodedMessage = message.value().decode('utf-8')
        for chave, valor in message.items():
            if chave == 'Catalogo' and valor == 'buscar':
                self.catalogFlow(message)
            print(f"Chave: {chave}, Valor: {valor}")

    def catalogFlow(self, message):
        
        print('pegando dados')


kafka = KafkaConsumer()
kafka.iniciarConsumidor()