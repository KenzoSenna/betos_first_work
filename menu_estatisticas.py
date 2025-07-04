from func_menu_estatisticas import *
from utilidades_cod import limpa_terminal, continuar

def mostrar_estatisticas():

        continuar()
        limpa_terminal()
        print("\n=== Estatísticas de Eventos ===")
        print("1. Total de Participantes")
        print("2. Total de Inscrições")
        print("3. Participantes por Evento")
        print("4. Temas Mais Preferidos")
        print("5. Eventos Mais Populares")
        print("6. Eventos por Tema")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        
        opcoes = {
            "1": total_participantes,
            "2": total_inscricoes,
            "3": participantes_por_evento,
            "4": temas_mais_preferidos,
            "5": eventos_mais_populares,
            "6": eventos_por_tema,
            "0": lambda: None
        }
        
        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.") 