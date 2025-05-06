# main.py

from Controllers.CartController import CartController
from Controllers.CatalogController import CatalogController
from Controllers.OrderController import OrderController

class Main:
    def start_project(self):
        # while True:
            answer = input('\nAntes de começarmos, nos informe qual sua área: \n1 para vendedor \n2 para cliente \n9 para sair\n')
            if answer == '1':
                self.seller_flow()
            elif answer == '2':
                self.customer_flow()
            elif answer == '9':
                print("Encerrando...")
            else:
                print('Área inválida, por favor tente novamente \n')

    def seller_flow(self):
        # while True:
            print('\nÓtimo, bem vindo vendedor!')
            print('Selecione o que deseja fazer')
            answer = input('1 para consultar estoque \n2 para adicionar items ao estoque \n9 para retornar ao menu principal\n')
            if answer == '1':
                CatalogController.get_catalog(lambda x: print(f"{x}"))
            elif answer == '2':
                CatalogController.add_to_catalog()
            elif answer == '9':
                self.start_project()
            else:
                print('Opção inválida, por favor tente novamente \n')

    def customer_flow(self):
        # while True:
            print('\nÓtimo, bem vindo comprador!')
            print('Selecione o que deseja fazer')
            answer = input('1 para consultar estoque \n2 para adicionar items ao carrinho \n3 para realizar um pedido \n4 para consultar últimos pedidos \n9 para retornar ao menu principal\n')
            if answer == '1':
                CatalogController.get_catalog(lambda x: print(f"{x}"))
            elif answer == '2':
                CartController.add_to_cart()
            elif answer == '3':
                OrderController.send_order()
            elif answer == '4':
                OrderController.get_last_orders()
            elif answer == '9':
                self.start_project()
            else:
                print('Opção inválida, por favor tente novamente \n')


if __name__ == "__main__":
    main = Main()
    main.start_project()
