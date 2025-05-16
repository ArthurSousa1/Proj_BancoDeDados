from datetime import datetime

def registrar_visualizacao(dados, redis_db):
    data_hoje = datetime.utcnow().strftime('%Y-%m-%d')
    chave = f"estatisticas:{data_hoje}"
    redis_db.hincrby(chave, dados['genero'], 1)