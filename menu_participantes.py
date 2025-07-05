from func_participantes_bd import *
from func_menu_participantes import *
from utilidades_cod import *

def participants_menu():
    while True:
        continue_by_pressing_enter()
        clean_terminal_by_op_sys()
        print("\n--- Menu de Participantes ---")
        print("1. Adicionar participante")
        print("2. Listar participantes")
        print("3. Remover participante")
        print("4. Atualizar participante")
        print("5. Buscar participante")
        print("6. Inscrever participante em evento")
        print("0. Voltar")


        opcao = input("\nEscolha: ")
    
        if opcao == "0":
            print("<<< Saindo >>>")
            break

        opcoes = {
            "1": add_participant_menu,
            "2": display_participants_menu,
            "3": participant_removal_menu,
            "4": update_participants_menu,
            "5": search_participant_menu,
            "6": subscribe_participant_to_event
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.")