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
        "usuario": input("\nUsuário: "),
        "filme": input("\nFilme avaliado: "),
        "nota": int(input("\nNota (0-10): ")),
        "comentario": input("\nComentário: "),
        "data": datetime.today().strftime("%Y-%m-%d")
    }

def gerar_visualizacao():
    return {
        "usuario": input("\nUsuário: "),
        "filme": input("\nFilme assistido: "),
        "genero": input("\nGênero do filme: "),
        "data": datetime.today().strftime("%Y-%m-%d")
    }