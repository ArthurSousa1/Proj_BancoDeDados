from controller import registrar_filme, avaliar_filme, assistir_filme, encerrar

def menu():
    while True:
        print("\n--- Menu S1 ---")
        print("1. Enviar novo filme")
        print("2. Enviar avaliação")
        print("3. Enviar registro de visualização")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            registrar_filme()
        elif escolha == '2':
            avaliar_filme()
        elif escolha == '3':
            assistir_filme()
        elif escolha == '4':
            break
        else:
            print("Opção inválida.")

    encerrar()


menu()