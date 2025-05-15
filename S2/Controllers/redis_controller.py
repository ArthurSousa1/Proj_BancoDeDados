from Models.redis_model import salvar_avaliacao

def processar_avaliacao(dados, redis_db):
    salvar_avaliacao(dados, redis_db)
    print("Avaliação salva no Redis.")