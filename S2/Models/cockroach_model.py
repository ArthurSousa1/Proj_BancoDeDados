def registrar_avaliacao(dados, cursor):
    avaliacaoId = dados['avaliacaoId']
    usuario = dados['usuario']
    filme = dados['filme']
    nota = dados['nota']
    comentario = dados['comentario']
    data = dados['data']

    cursor.execute(
        """
        INSERT INTO avaliacoes (avaliacao_id, usuario, filme, nota, comentario, data)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (avaliacaoId, usuario, filme, nota, comentario, data)
    )

def obter_avaliacoes(cursor):
    cursor.execute("SELECT * FROM avaliacoes")
    rows = cursor.fetchall()
    return [
        {
            "id": str(row[0]),
            "usuario": str(row[1]),
            "filme": str(row[2]),
            "nota": row[3],
            "comentario": row[4],
            "data": str(row[5])
        } for row in rows
    ]