def registrar_assistencia(dados, cursor):
    cursor.execute(
        """
        INSERT INTO assistencias (usuario_id, filme_id, genero, data)
        VALUES (%s, %s, %s, %s)
        """,
        (dados['usuarioId'], dados['filmeId'], dados['genero'], dados['data'])
    )