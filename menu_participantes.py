from func_participantes_bd import *
from func_menu_participantes import *
from utilidades_cod import *

def menu_participantes():

    while True:
        continuar()
        limpa_terminal()
        print("\n--- Menu de Participantes ---")
        print("1. Adicionar participante")
        print("2. Listar participantes")
        print("3. Remover participante")
        print("4. Atualizar participante")
        print("5. Buscar participante")
        print("0. Voltar")

        opcao = input("Escolha: ")
        
        if opcao == "0":
            print("\nVoltando ao menu principal...")
            break

        opcoes = {
            "1": adicionar_participante_menu,
            "2": listar_participantes_menu,
            "3": remover_participantes_menu,
            "4": atualizar_participantes_menu,
            "5": buscar_participantes_menu
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.")