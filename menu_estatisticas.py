from func_menu_estatisticas import *
from utilidades_cod import clean_terminal_by_op_sys, continue_by_pressing_enter

def statistics_menu():
    while True:
        continue_by_pressing_enter()
        clean_terminal_by_op_sys()
        print("\n--- Menu de Estatísticas Gerais ---")
        print("1. Total de Participantes")
        print("2. Total de Inscrições")
        print("3. Participantes por Evento")
        print("4. Temas Mais Preferidos")
        print("5. Eventos Mais Populares")
        print("6. Eventos por Tema")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("\n<<< Saindo >>>")
            break
        
        opcoes = {
            "1": participants_total,
            "2": inscriptions_total,
            "3": participantes_por_evento,
            "4": most_popular_themes,
            "5": most_popular_events,
            "6": events_in_themes
        }
        
        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.") 