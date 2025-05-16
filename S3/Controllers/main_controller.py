from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch # type: ignore

from Controllers.elasticsearch_controller import registrar_log

es_client = Elasticsearch(
    "http://localhost:9200",
    headers={"Accept": "application/vnd.elasticsearch+json; compatible-with=8",
             "Content-Type": "application/vnd.elasticsearch+json; compatible-with=8"}
)

consumer = KafkaConsumer(
    'projetoDB',
    bootstrap_servers='localhost:9091',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-s3'
)

def processar_mensagem(mensagem):
    print('Mensagem recebida: \n', mensagem)
    registrar_log(mensagem, es_client)