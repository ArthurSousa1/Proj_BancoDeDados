from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch # type: ignore

from Controllers.elasticsearch_controller import registrar_log

es_client = Elasticsearch("http://localhost:9200")

consumer = KafkaConsumer(
    'projetoDB',
    bootstrap_servers='localhost:9091',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-s3'
)

def processar_mensagem(mensagem):
    print('Mensagem recebida: \n', mensagem)
    tipo = mensagem['tipo']
    dados = mensagem['dados']

    if tipo == 'log_s3':
        registrar_log(dados, es_client)