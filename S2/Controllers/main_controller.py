from kafka import KafkaConsumer, KafkaProducer
import json
from pymongo import MongoClient # type: ignore
import redis # type: ignore
import psycopg2 # type: ignore

from Controllers.mongo_controller import processar_filme, listar_filmes
from Controllers.redis_controller import processar_visualizacao, estatisticas_genero_por_dia 
from Controllers.cockroach_controller import processar_avaliacao, listar_avaliacoes

mongo_client = MongoClient("mongodb+srv://sousaarthur840:sXFWGkNwWCcpknkq@estoque.djdf0fe.mongodb.net/?retryWrites=true&w=majority&appName=Estoque&tlsAllowInvalidCertificates=true")
mongo_db = mongo_client["catalogo"]

redis_db = redis.StrictRedis(host='redis-11658.crce196.sa-east-1-2.ec2.redns.redis-cloud.com', port=11658, password='jzXQ3bYSEd12khkblAXBxIvhRgflqXTn')

cockroach_conn = psycopg2.connect(
    user='arthur-sousa', password='P9ClrcZsNNk0t_D2Ff38dg',
    database='defaultdb', host='projeto-banco-de-dados-14602.7tt.aws-us-east-1.cockroachlabs.cloud', port=26257
)
cockroach_cursor = cockroach_conn.cursor()

consumer = KafkaConsumer(
    'projetoDB',
    bootstrap_servers='localhost:9091',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-s2'
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9091',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def processar_mensagem(mensagem):
    if mensagem['tipo'] == 'resposta':
        return
    
    print('Mensagem recebida: \n', mensagem)
    tipo = mensagem['tipo']

    if tipo == 'registrar_filme':
        dados = mensagem['dados']
        processar_filme(dados, mongo_db)
    elif tipo == 'avaliar_filme':
        dados = mensagem['dados']
        processar_avaliacao(dados, cockroach_cursor, cockroach_conn)
    elif tipo == 'assistir_filme':
        dados = mensagem['dados']
        processar_visualizacao(dados, redis_db)
    elif tipo == 'listar_filmes':
        resultado = listar_filmes(mongo_db)
        id_correlacao = mensagem['id_correlacao']
        responder(id_correlacao, resultado)
    elif tipo == 'listar_avaliacoes':
        resultado = listar_avaliacoes(cockroach_cursor)
        id_correlacao = mensagem['id_correlacao']
        responder(id_correlacao, resultado)
    elif tipo == 'estatisticas_genero':
        resultado = estatisticas_genero_por_dia(redis_db)
        id_correlacao = mensagem['id_correlacao']
        responder(id_correlacao, resultado)

def responder(id_correlacao, resultado):
    mensagem_resposta = {
        "id_correlacao": id_correlacao,
        "tipo": "resposta",
        "resultado": resultado
    }
    producer.send('projetoDB', mensagem_resposta)
    producer.flush()