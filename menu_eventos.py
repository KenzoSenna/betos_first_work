from func_menu_eventos import *
from utilidades_cod import *

def menu_eventos():

    while True:
        continuar()
        limpa_terminal()
        print("\n--- Menu de Eventos ---")
        print("1. Adicionar evento")
        print("2. Listar eventos")
        print("3. Alterar evento")
        print("4. Remover evento")
        print("5. Buscar evento")
        print("0. Voltar")

        opcao = input("Escolha: ")
        if opcao == "0":
            break

        opcoes = {
            "1": adicao_eventos_menu,
            "2": listar_eventos_menu,
            "3": alterar_evento_menu,
            "4": remover_evento_menu,
            "5": buscar_evento,
            "0": lambda: print("\nVoltando ao Menu principal")
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()

        else:
            print("\nOpção inválida. Tente novamente.")