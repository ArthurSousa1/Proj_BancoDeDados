import redis # type: ignore
import json

r = redis.Redis(host='redis-11658.crce196.sa-east-1-2.ec2.redns.redis-cloud.com', port=11658, password='jzXQ3bYSEd12khkblAXBxIvhRgflqXTn')

# Create/Update
def adicionar_item_ao_carrinho(usuario_id, item):
    chave = f"carrinho:{usuario_id}"
    carrinho = json.loads(r.get(chave) or '{"itens": []}')
    carrinho['itens'].append(item)
    r.set(chave, json.dumps(carrinho))

# Read
def consultar_carrinho(usuario_id):
    chave = f"carrinho:{usuario_id}"
    dados = r.get(chave)
    return json.loads(dados) if dados else {"itens": []}

# Delete
def limpar_carrinho(usuario_id):
    r.delete(f"carrinho:{usuario_id}")
