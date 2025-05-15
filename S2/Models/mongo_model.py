def salvar_filme(dados, mongo_db):
    mongo_db.filmes.insert_one(dados)