import uuid
from datetime import datetime

def gerar_filme():
    return {
        "filmeId": f"f{uuid.uuid4().hex[:6]}",
        "titulo": input("\nTítulo do filme: "),
        "genero": input("\nGênero: "),
        "diretor": input("\nDiretor: "),
        "ano": int(input("\nAno: ")),
        "duracao": int(input("\nDuração (min): ")),
        "sinopse": input("\nSinopse: ")
    }

def gerar_avaliacao():
    return {
        "avaliacaoId": f"a{uuid.uuid4().hex[:6]}",
        "usuarioId": input("\nID do usuário: "),
        "filmeId": input("\nID do filme avaliado: "),
        "nota": int(input("\nNota (0-10): ")),
        "comentario": input("\nComentário: "),
        "data": datetime.today().strftime("%Y-%m-%d")
    }

def gerar_assistencia():
    return {
        "usuarioId": input("\nID do usuário: "),
        "filmeId": input("\nID do filme assistido: "),
        "genero": input("\nGênero do filme: "),
        "data": datetime.today().strftime("%Y-%m-%d")
    }