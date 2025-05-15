from kafka import KafkaConsumer
import json
from pymongo import MongoClient # type: ignore
import redis # type: ignore
import psycopg2 # type: ignore

from Controllers.mongo_controller import processar_filme
from Controllers.redis_controller import processar_avaliacao
from Controllers.cockroach_controller import processar_assistencia

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

def processar_mensagem(mensagem):
    print('Mensagem recebida: \n', mensagem)
    tipo = mensagem['tipo']
    dados = mensagem['dados']

    if tipo == 'registrar_filme':
        processar_filme(dados, mongo_db)
    elif tipo == 'avaliar_filme':
        processar_avaliacao(dados, redis_db)
    elif tipo == 'assistir_filme':
        processar_assistencia(dados, cockroach_cursor, cockroach_conn)