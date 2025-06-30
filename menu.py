from menu_eventos import *
from  menu_participantes import *
from menu_estatisticas import mostrar_estatisticas



def menu_principal():
    while True:
        print("\n=== Sistema de Gestao de Eventos ===")
        print("1. Gerenciar Eventos")
        print("2. Gerenciar Participantes")
        print("3. Estatisticas")
        print("0. Sair")

        opcao = input("Escolha uma opcao: ")

        opcoes = {
            "1": menu_eventos,
            "2": menu_participantes,
            "3": mostrar_estatisticas,
            "0": print("\nEncerrando!")
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida. Tente novamente.")