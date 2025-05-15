from Models.cockroach_model import registrar_assistencia

def processar_assistencia(dados, cursor, conn):
    registrar_assistencia(dados, cursor)
    conn.commit()
    print("Assistência registrada no CockroachDB.")