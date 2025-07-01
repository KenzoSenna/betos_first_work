from menu_eventos import *
from  menu_participantes import *
from menu_estatisticas import mostrar_estatisticas
from utilidades_cod import limpa_terminal


def menu_principal():
    while True:
        limpa_terminal()
        print("\n=== Sistema de Gestao de Eventos ===")
        print("1. Gerenciar Eventos")
        print("2. Gerenciar Participantes")
        print("3. Estatisticas")
        print("0. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "0":
            print("\nEncerrando!")
            break

        opcoes = {
            "1": menu_eventos,
            "2": menu_participantes,
            "3": mostrar_estatisticas,
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()

        else:
            print("\nOpção inválida. Tente novamente.")