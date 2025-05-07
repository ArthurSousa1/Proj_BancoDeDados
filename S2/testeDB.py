## Redis 
# from db.mongo import adicionar_produto, buscar_produto_por_id

# # Adiciona um produto
# produto_id = adicionar_produto({
#     "nome": "Webcam Full HD",
#     "descricao": "1080p com microfone embutido",
#     "preco": 299.90,
#     "categoria": "Acessórios",
#     "quantidade_estoque": 15,
#     "ativo": True
# })

# # Busca pelo ID
# produto = buscar_produto_por_id(produto_id)
# print("Produto encontrado:", produto)

#### Redis
# from db.redis_db import adicionar_item_ao_carrinho, consultar_carrinho

# adicionar_item_ao_carrinho("user123", {
#     "produto_id": "abc", "nome": "Fone", "quantidade": 2, "preco_unitario": 89.90
# })

# print(consultar_carrinho("user123"))

import asyncio
from db.cockroach import criar_pedido, consultar_pedidos_por_usuario

async def testar_pedido():
    pedido_id = await criar_pedido(
        usuario_id="user789",
        total=300.00,
        endereco={"rua": "Av X", "numero": "100"},
        itens=[{"produto_id": "prod1", "nome_produto": "Item A", "quantidade": 1, "preco_unitario": 300.00}]
    )
    pedidos = await consultar_pedidos_por_usuario("user789")
    print(pedidos)

asyncio.run(testar_pedido())
