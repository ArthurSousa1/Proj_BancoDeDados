from Models.mongo_model import salvar_filme

def processar_filme(dados, mongo_db):
    salvar_filme(dados, mongo_db)
    print("Filme salvo no MongoDB.")

def listar_filmes(mongo_db):
    filmes_collection = mongo_db["filmes"]
    filmes = list(filmes_collection.find({}, {"_id": 0}))
    return filmes