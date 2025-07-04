from menu_eventos import *
from  menu_participantes import *
from menu_temas import *
from menu_estatisticas import statistics_menu
from utilidades_cod import clean_terminal_by_op_sys

def main_menu():
    while True:
        clean_terminal_by_op_sys()
        print("\n=== Sistema de Gestao de Eventos ===")
        print("1. Gerenciar Eventos")
        print("2. Gerenciar Participantes")
        print("3. Gerenciar temas")
        print("4. Estatísticas")

        print("0. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "0":
            print("\n<<< Saindo >>>")
            break

        opcoes = {
            "1": events_menu,
            "2": participants_menu,
            "3": themes_menu,
            "4": statistics_menu
            
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()

        else:
            print("\nOpção inválida. Tente novamente.")