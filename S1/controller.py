from kafka import KafkaProducer, KafkaConsumer
import json
import uuid
from model import gerar_filme, gerar_avaliacao, gerar_visualizacao

producer = KafkaProducer(
    bootstrap_servers='localhost:9091',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

consumer = KafkaConsumer(
    'projetoDB',
    bootstrap_servers='localhost:9091',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-s1'
)

def registrar_filme():
    dados = gerar_filme()
    mensagem = {"tipo": "registrar_filme", "dados": dados}
    producer.send("projetoDB", mensagem)
    print("Mensagem enviada para projetoDB")

def avaliar_filme():
    dados = gerar_avaliacao()
    mensagem = {"tipo": "avaliar_filme", "dados": dados}
    producer.send("projetoDB", mensagem)
    print("Mensagem enviada para projetoDB")

def assistir_filme():
    dados = gerar_visualizacao()
    mensagem = {"tipo": "assistir_filme", "dados": dados}
    producer.send("projetoDB", mensagem)
    print("Mensagem enviada para projetoDB")

def exibir_filmes():
    id_correlacao = str(uuid.uuid4())
    mensagem = {
        "id_correlacao": id_correlacao,
        "tipo": "listar_filmes"
    }
    filmes = enviar_requisicao_e_esperar("projetoDB", mensagem)
    for f in filmes:
        print(f)

def exibir_avaliacoes():
    id_correlacao = str(uuid.uuid4())
    mensagem = {
        "id_correlacao": id_correlacao,
        "tipo": "listar_avaliacoes"
    }
    avaliacoes = enviar_requisicao_e_esperar("projetoDB", mensagem)
    for a in avaliacoes:
        print(a)

def exibir_estatisticas():
    id_correlacao = str(uuid.uuid4())
    mensagem = {
        "id_correlacao": id_correlacao,
        "tipo": "estatisticas_genero"
    }
    resultado = enviar_requisicao_e_esperar("projetoDB", mensagem)
    for genero, qtd in resultado.items():
        print(f"{genero}: {qtd}")

def enviar_requisicao_e_esperar(topic, mensagem):
    producer.send(topic, mensagem)
    producer.flush()

    print("Aguardando resposta...")
    for msg in consumer:
        resposta = msg.value
        if resposta.get("id_correlacao") == mensagem['id_correlacao'] and resposta.get('tipo') == 'resposta':
            return resposta.get("resultado")
        
def encerrar():
    producer.flush()