from Models.redis_model import registrar_visualizacao
from datetime import datetime

def processar_visualizacao(dados, redis_db):
    registrar_visualizacao(dados, redis_db)
    print("Visualização salva no Redis.")

def estatisticas_genero_por_dia(redis_db):
    data_hoje = datetime.utcnow().strftime('%Y-%m-%d')
    chave = f"estatisticas:{data_hoje}"
    dados = redis_db.hgetall(chave)
    return {k.decode(): int(v.decode()) for k, v in dados.items()}