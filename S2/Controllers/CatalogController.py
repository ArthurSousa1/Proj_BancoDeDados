from db.mongo import produtos

class CatalogController:

    # Create
    def adicionar_produto(nome, descricao, categoria, quantidade):
        dados_produto = {
            "nome": nome,
            "descricao": descricao,
            "categoria": categoria,
            "quantidade_estoque": quantidade
        }
        result = produtos.insert_one(dados_produto)
        return str(result.inserted_id)

    def buscar_todos_produtos():
        produtos_cursor = produtos.find()
        lista_produtos = list(produtos_cursor)
        return lista_produtos
    # Read
    def buscar_produto_por_id(produto_id):
        return produtos.find_one({"_id": ObjectId(produto_id)})

    # Update
    def atualizar_estoque(produto_id, nova_quantidade):
        produtos.update_one({"_id": ObjectId(produto_id)}, {"$set": {"quantidade_estoque": nova_quantidade}})

    # Delete
    def remover_produto(produto_id):
        produtos.delete_one({"_id": ObjectId(produto_id)})
