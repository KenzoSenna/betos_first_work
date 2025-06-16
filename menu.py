from menu_eventos import *
from  menu_participantes import *
from relatorios import mostrar_estatisticas

def menu_principal():
    while True:
        print("\n=== Sistema de Gestao de Eventos ===")
        print("1. Gerenciar Eventos")
        print("2. Gerenciar Participantes")
        print("3. Estatisticas")
        print("0. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            menu_eventos()
        elif opcao == "2":
            menu_participantes()
        elif opcao == "3":
            mostrar_estatisticas()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida.")