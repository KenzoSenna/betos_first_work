from func_eventos_bd import *
from func_tema_bd import listar_temas_bd
from datetime import datetime


def adicao_eventos_menu():
    try:
        temas = listar_temas_bd()
        if not temas:
            print("Nenhum tema cadastrado. Cadastre um tema antes de criar um evento.")
            return
        print("\nTemas disponíveis:")
        for t in temas:
            print(f"ID: {t[0]} | Tema: {t[1]}")
        id_tema = int(input("Selecione o ID do tema para este evento: "))
        nome = input("Nome do evento: ")
        data = datetime.strptime(input("Data (DD-MM-AAAA): "), "%d-%m-%Y").strftime("%d-%m-%Y")
        if not nome or not data:
            print("Nome ou data inválidos. O evento não foi adicionado.")
            return
        adicionar_evento_bd(nome, data, id_tema)
        print("Evento adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar evento: {e}")


def listar_eventos_menu():
    try:
        eventos = listar_eventos_bd()
        if not eventos:
            print("Nenhum evento cadastrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
    except Exception as e:
        print(f"Erro ao listar eventos: {e}")

def alterar_evento_menu():
    try:
        print("\n--- Alterar Evento ---")
        eventos = listar_eventos_bd()
        if not eventos:
            print("Nenhum evento cadastrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
        id_evento = int(input("Selecione o ID do evento que deseja alterar: "))
        nome = input("Novo nome do evento (deixe em branco para não alterar): ")
        data = input("Nova data do evento (dd-MM-AAAA) (deixe em branco para não alterar): ")
        tema = input("Novo tema do evento (deixe em branco para não alterar): ")
        alterar_evento_bd(id_evento, nome, data, tema)
        if not nome and not data and not tema:
            print("Nenhuma alteração foi feita.")
            return
        print("Evento alterado com sucesso.")
    except Exception as e:
        print(f"Erro ao alterar evento: {e}")

def excluir_evento_menu():
    try:
        print("Eventos cadastrados:")
        eventos = listar_eventos_bd()
        if not eventos:
            print("\nNenhum evento cadastrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
        id_evento = int(input("Selecione o ID do evento que deseja excluir: "))
        if not id_evento:
            print("ID inválido. O evento não foi excluído.")
            return
        excluir_evento_bd(id_evento)
        print("Evento excluído com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir evento: {e}")

def buscar_evento_menu():
    try:
        print("\n--- Buscar Evento ---")
        termo = input("Digite o termo de busca (ID, nome, tema ou data): ")
        eventos = buscar_evento_bd(termo)
        if not eventos:
            print("Nenhum evento encontrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
    except Exception as e:
        print(f"Erro ao buscar evento: {e}")