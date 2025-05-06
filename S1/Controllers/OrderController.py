from MessageHelper import send_message

class OrderController:

    def send_order():
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

    def get_last_orders():
        print('Estou enviando tudo')