from model import salvar_mensagem_log

def registrar_log(dados, es_client):
    salvar_mensagem_log(es_client, dados)
    print("Mensagem registrada no Elasticsearch.")