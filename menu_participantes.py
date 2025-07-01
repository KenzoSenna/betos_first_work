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
        print("5. Buscar participante por ID")
        print("6. Buscar participante por nome")
        print("0. Voltar")

        opcao = input("Escolha: ")
        
        if opcao == "0":
            print("\nVoltando ao menu principal...")
            break

        opcoes = {
            "1": adicionar,
            "2": listar,
            "3": remover,
            "4": atualizar,
            "5": buscar_por_id,
            "6": buscar_por_nome,
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.")