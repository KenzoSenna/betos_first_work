from func_menu_temas import *
from utilidades_cod import limpa_terminal, continuar
from func_menu_temas import *

def menu_temas():
    while True:
        continuar()
        limpa_terminal()
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
             
            "1": adicionar_tema,
            "2": listar_temas,
            "3": remover_tema,
            "4": atualizar_tema,
            "5": buscar_tema

        }

        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.")