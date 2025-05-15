from Models.mongo_model import salvar_filme

def processar_filme(dados, mongo_db):
    salvar_filme(dados, mongo_db)
    print("Filme salvo no MongoDB.")