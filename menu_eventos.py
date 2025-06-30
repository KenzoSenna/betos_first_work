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
            "3": alterar_evento_menu,
            "4": remover_evento_menu,
            "5": buscar_evento_por_id_menu,
            "0": print("Voltando ao Menu principal")
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        elif opcao == "0":
            break
        else:
            print("\nOpção inválida. Tente novamente.")