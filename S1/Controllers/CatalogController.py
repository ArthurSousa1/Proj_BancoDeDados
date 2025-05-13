from Mensageria.Producer import send_message

class CatalogController:

    def add_to_catalog():
        nome = input('\nMaravilha! Digite o nome do produto:\n')
        descricao = input('\nValor:\n')
        categoria = input('\n Categoria:')
        quantidade = input('\nQuantidade:\n')

        mensagem = {
            'controller': 'Catalogo',
            'tipo': 'adicionar',
            "nome": nome,
            "descricao": descricao,
            "categoria": categoria,
            "quantidade_estoque": quantidade
        }

        print(mensagem)
        send_message(mensagem)

    def get_catalog(callback):
        mensagem = {
            'controller': 'Catalogo',
            'tipo': 'buscar',
        }
        
        print(mensagem)
        send_message(mensagem)