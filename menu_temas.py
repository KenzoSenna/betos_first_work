from func_menu_temas import *
from utilidades_cod import clean_terminal_by_op_sys, continue_by_pressing_enter
from func_menu_temas import *

def themes_menu():
    while True:
        continue_by_pressing_enter()
        clean_terminal_by_op_sys()
        print("\n--- Menu de Temas ---")
        print("1. Adicionar tema")
        print("2. Listar temas")
        print("3. Remover tema")
        print("4. Atualizar tema")
        print("5. Buscar tema")
        print("0. Voltar")

        opcao = input("Escolha: ")
             
        if opcao == "0":
            print("\n<<< Saindo >>>")
            break     

        opcoes = {
             
            "1": add_themes_menu,
            "2": display_themes_menu,
            "3": themes_removal_menu,
            "4": themes_update_menu,
            "5": theme_search_menu

        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.")