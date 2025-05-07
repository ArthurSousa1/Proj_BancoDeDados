from pymongo import MongoClient # type: ignore
from bson.objectid import ObjectId # type: ignore

client = MongoClient("mongodb+srv://sousaarthur840:sXFWGkNwWCcpknkq@estoque.djdf0fe.mongodb.net/?retryWrites=true&w=majority&appName=Estoque&tlsAllowInvalidCertificates=true")
db = client.marketplace
produtos = db.produtos

# Create
def adicionar_produto(dados_produto):
    result = produtos.insert_one(dados_produto)
    return str(result.inserted_id)

# Read
def buscar_produto_por_id(produto_id):
    return produtos.find_one({"_id": ObjectId(produto_id)})

# Update
def atualizar_estoque(produto_id, nova_quantidade):
    produtos.update_one({"_id": ObjectId(produto_id)}, {"$set": {"quantidade_estoque": nova_quantidade}})

# Delete
def remover_produto(produto_id):
    produtos.delete_one({"_id": ObjectId(produto_id)})
