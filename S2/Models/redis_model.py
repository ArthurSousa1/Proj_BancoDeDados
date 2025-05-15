def salvar_avaliacao(dados, redis_db):
    key = f"avaliacao:{dados['avaliacaoId']}"
    redis_db.hmset(key, dados)