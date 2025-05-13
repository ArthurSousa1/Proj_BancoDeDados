from pymongo import MongoClient # type: ignore
from bson.objectid import ObjectId # type: ignore

client = MongoClient("mongodb+srv://sousaarthur840:sXFWGkNwWCcpknkq@estoque.djdf0fe.mongodb.net/?retryWrites=true&w=majority&appName=Estoque&tlsAllowInvalidCertificates=true")
db = client.marketplace
produtos = db.produtos
