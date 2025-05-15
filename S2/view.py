from Controllers.main_controller import consumer, processar_mensagem

def iniciar_consumo():
    print("Iniciando consumidor S2...")
    for msg in consumer:
        mensagem = msg.value
        processar_mensagem(mensagem)

if __name__ == '__main__':
    iniciar_consumo()