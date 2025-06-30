from func_menu_eventos import *

def menu_eventos():
    while True:
        print("\n--- Menu de Eventos ---")
        print("1. Adicionar evento")
        print("2. Listar eventos")
        print("0. Voltar")

        opcao = input("Escolha: ")

        opcoes = {
            "1": adicao_eventos_menu,
            "2": listar_eventos_menu,
            "0": lambda: None
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.")