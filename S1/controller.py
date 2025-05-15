from kafka import KafkaProducer
import json
from model import gerar_filme, gerar_avaliacao, gerar_assistencia

producer = KafkaProducer(
    bootstrap_servers='localhost:9091',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
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
    dados = gerar_assistencia()
    mensagem = {"tipo": "assistir_filme", "dados": dados}
    producer.send("projetoDB", mensagem)
    print("Mensagem enviada para projetoDB")

def encerrar():
    producer.flush()