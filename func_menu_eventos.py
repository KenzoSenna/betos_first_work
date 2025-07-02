from func_eventos_bd import *

def adicao_eventos_menu():
    try:
        nome = input("Nome do evento: ")
        data = input("Data (AAAA-MM-DD): ")
        tema = input("Tema: ")
        adicionar_evento(nome, data, tema)
        print("Evento adicionado com sucesso.")
    
    except Exception as e:
        print(f"Erro ao adicionar evento: {e}")

def listar_eventos_menu():
    try:
        for evento in listar_eventos():
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
    except Exception as e:
        print(f"Erro ao listar eventos: {e}")
        
def alterar_evento_menu():
    try:
        id_evento = int(input("ID do evento a ser alterado: "))
        nome = input("Novo nome (deixe em branco para não alterar): ")
        data = input("Nova data (AAAA-MM-DD) (deixe em branco para não alterar): ")
        tema = input("Novo tema (deixe em branco para não alterar): ")
        alterar_evento(id_evento, nome or None, data or None, tema or None)
        print("Evento alterado com sucesso.")

    except Exception as e:
        print(f"Erro ao alterar evento: {e}")

def remover_evento_menu():
    try:

        id_evento = int(input("ID do evento a ser removido: "))
        excluir_evento(id_evento)
        print("\nEvento removido com sucesso.")
        
    except Exception as e:
        print(F"\nErro ao remover evento: {e}")

def buscar_evento_menu():
    try:
        termo = input("Digite o ID, nome, tema ou data do evento a ser buscado: ")
        eventos = buscar_evento(termo)

        if eventos:
            for evento in eventos:
                print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
        else:
            print("\nNenhum evento encontrado.")

    except Exception as e:
        print(F"\nErro ao buscar evento: {e}")