from func_menu_eventos import *
from utilidades_cod import *

def events_menu():
    while True:
        continue_by_pressing_enter()
        clean_terminal_by_op_sys()
        print("\n--- Menu de Eventos ---")
        print("1. Adicionar evento")
        print("2. Listar eventos")
        print("3. Alterar evento")
        print("4. Remover evento")
        print("5. Buscar evento")
        print("0. Voltar")

        opcao = input("Escolha: ")
        if opcao == "0":
            print("\n<<< Saindo >>>")
            break

        opcoes = {
            "1": event_creation_menu,
            "2": display_event_menu,
            "3": update_event_menu,
            "4": event_removal_menu,
            "5": search_event_menu
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()

        else:
            print("\nOpção inválida. Tente novamente.")