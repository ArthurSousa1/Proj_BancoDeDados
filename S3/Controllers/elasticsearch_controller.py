from model import salvar_mensagem_log

def registrar_log(mensagem, es_client):
    salvar_mensagem_log(es_client, mensagem)
    print("Mensagem registrada no Elasticsearch.")