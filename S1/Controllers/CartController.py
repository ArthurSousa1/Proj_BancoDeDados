from Mensageria.Producer import send_message

class CartController:

    def add_to_cart():
        produto = input('\nMaravilha! Digite o nome do produto:\n')
        valor = input('\nAgora o valor:\n')
        quantidade = input('\nE para fechar a quantidade:\n')

        mensagem = {
            'tipo': 'Catalogo',
            'produto': produto,
            'preco': valor,
            'quantidade': quantidade
        }

        print(mensagem)
        send_message(mensagem)