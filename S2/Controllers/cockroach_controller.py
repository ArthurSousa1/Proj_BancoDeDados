from Models.cockroach_model import registrar_avaliacao, obter_avaliacoes

def processar_avaliacao(dados, cursor, conn):
    registrar_avaliacao(dados, cursor)
    conn.commit()
    print("Avaliação registrada no CockroachDB.")

def listar_avaliacoes(cursor):
    return obter_avaliacoes(cursor)
    