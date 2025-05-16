from controller import registrar_filme, avaliar_filme, assistir_filme, exibir_filmes, exibir_avaliacoes, exibir_estatisticas, encerrar

def menu():
    while True:
        print("\n--- Menu S1 ---")
        print("1. Enviar novo filme")
        print("2. Enviar avaliação")
        print("3. Enviar registro de visualização")
        print("4. Listar Filmes")
        print("5. Listar Avaliações")
        print("6. Estatísticas por Gênero e Dia")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            registrar_filme()
        elif escolha == '2':
            avaliar_filme()
        elif escolha == '3':
            assistir_filme()
        elif escolha == '4':
            exibir_filmes()
        elif escolha == '5':
            exibir_avaliacoes()
        elif escolha == '6':
            exibir_estatisticas()
        elif escolha == '7':
            break
        else:
            print("Opção inválida.")

    encerrar()


menu()