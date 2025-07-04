from menu_eventos import *
from  menu_participantes import *
from menu_temas import *
from menu_estatisticas import mostrar_estatisticas
from utilidades_cod import limpa_terminal

def menu_principal():

        limpa_terminal()
        print("\n=== Sistema de Gestao de Eventos ===")
        print("1. Gerenciar Eventos")
        print("2. Gerenciar Participantes")
        print("3. Gerenciar temas")
        print("4. Estatísticas")
        print("0. Sair")

        opcao = input("Escolha uma opcao: ")

        opcoes = {
            "1": menu_eventos,
            "2": menu_participantes,
            "3": menu_temas,
            "4": mostrar_estatisticas,
            "0": lambda: None
        }

        acao = opcoes.get(opcao)
        if acao:
            acao()

        else:
            print("\nOpção inválida. Tente novamente.")