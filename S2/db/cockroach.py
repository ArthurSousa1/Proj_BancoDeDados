import asyncpg # type: ignore
import asyncio, uuid, json
from datetime import datetime

async def conectar():
    return await asyncpg.connect(
        user='arthur-sousa', password='P9ClrcZsNNk0t_D2Ff38dg',
        database='defaultdb', host='projeto-banco-de-dados-14602.7tt.aws-us-east-1.cockroachlabs.cloud', port=26257
    )

# Create
async def criar_pedido(usuario_id, total, endereco, itens):
    conn = await conectar()
    pedido_id = str(uuid.uuid4())
    await conn.execute("""
        INSERT INTO pedidos (id, usuario_id, data_pedido, total, status, endereco_entrega)
        VALUES ($1, $2, $3, $4, $5, $6)
    """, pedido_id, usuario_id, datetime.utcnow(), total, "em processamento", json.dumps(endereco))

    for item in itens:
        await conn.execute("""
            INSERT INTO itens_pedido (id, pedido_id, produto_id, nome_produto, quantidade, preco_unitario)
            VALUES ($1, $2, $3, $4, $5, $6)
        """, str(uuid.uuid4()), pedido_id, item["produto_id"], item["nome_produto"], item["quantidade"], item["preco_unitario"])

    await conn.close()
    return pedido_id

# Read (últimos pedidos por usuário)
async def consultar_pedidos_por_usuario(usuario_id):
    conn = await conectar()
    rows = await conn.fetch("""
        SELECT p.id, p.data_pedido, p.total, p.status, p.endereco_entrega, 
               json_agg(json_build_object(
                   'produto_id', i.produto_id,
                   'nome_produto', i.nome_produto,
                   'quantidade', i.quantidade,
                   'preco_unitario', i.preco_unitario
               )) AS itens
        FROM pedidos p
        JOIN itens_pedido i ON p.id = i.pedido_id
        WHERE p.usuario_id = $1
        GROUP BY p.id
        ORDER BY p.data_pedido DESC
        LIMIT 5
    """, usuario_id)
    await conn.close()
    return [dict(row) for row in rows]
