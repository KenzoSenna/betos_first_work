from func_menu_estatisticas import total_participantes, total_inscricoes, participantes_por_evento
from utilidades_cod import limpa_terminal, continuar

def mostrar_estatisticas():
    while True:
        continuar()
        limpa_terminal()
        print("\n=== Estatísticas de Eventos ===")
        print("1. Total de Participantes")
        print("2. Total de Inscrições")
        print("3. Participantes por Evento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":

            print("\nEncerrando estatísticas!")
            break
        
        opcoes = {
            "1": total_participantes,
            "2": total_inscricoes,
            "3": participantes_por_evento,
        }
        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("\nOpção inválida. Tente novamente.") 