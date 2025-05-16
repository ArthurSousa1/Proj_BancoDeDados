from elasticsearch import Elasticsearch # type: ignore
from datetime import datetime

def salvar_mensagem_log(es_client, dados):
    es_client.index(
        index="projetoDB",
        document={
            "mensagem": dados,
            "timestamp": datetime.utcnow().isoformat()
        }
    )