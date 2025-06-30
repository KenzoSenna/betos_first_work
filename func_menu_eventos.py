from func_eventos_bd import *

def adicao_eventos_menu():
    nome = input("Nome do evento: ")
    data = input("Data (AAAA-MM-DD): ")
    tema = input("Tema: ")
    adicionar_evento(nome, data, tema)
    print("Evento adicionado com sucesso.")

def listar_eventos_menu():
    for evento in listar_eventos():
        print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
def alterar_evento_menu():
    id_evento = int(input("ID do evento a ser alterado: "))
    nome = input("Novo nome (deixe em branco para não alterar): ")
    data = input("Nova data (AAAA-MM-DD) (deixe em branco para não alterar): ")
    tema = input("Novo tema (deixe em branco para não alterar): ")
    alterar_evento(id_evento, nome or None, data or None, tema or None)
    print("Evento alterado com sucesso.")

def remover_evento_menu():
    id_evento = int(input("ID do evento a ser removido: "))
    excluir_evento(id_evento)
    print("Evento removido com sucesso.")

def buscar_evento_por_id_menu():
    id_evento = int(input("ID do evento a ser buscado: "))
    evento = buscar_evento_por_id(id_evento)
    
    if evento:
        print(f"ID: {evento[0][0]} | Nome: {evento[0][1]} | Data: {evento[0][2]} | Tema: {evento[0][3]}")
    else:
        print("Evento não encontrado.")

def buscar_evento_por_nome_menu():
    nome = input("Nome do evento a ser buscado: ")
    eventos = buscar_evento_por_nome(nome)
    
    if eventos:
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
    else:
        print("Nenhum evento encontrado com esse nome.")