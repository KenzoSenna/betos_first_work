from func_eventos_bd import *
from func_tema_bd import display_themes_from_db
from datetime import datetime


def event_creation_menu():
    # This function allows the user to create a new event.
    try:
        temas = display_themes_from_db()
        if not temas:
            print("Nenhum tema cadastrado. Cadastre um tema antes de criar um evento.")
            return
        print("\nTemas disponíveis:")
        for t in temas:
            print(f"ID: {t[0]} | Tema: {t[1]}")
        id_tema = int(input("Selecione o ID do tema para este evento: "))
        nome = input("Nome do evento: ")
        data = datetime.strptime(input("Data (DD/MM/AAAA): "), "%d/%m/%Y").strftime("%d/%m/%Y")
        if not nome or not data:
            print("Nome ou data inválidos. O evento não foi adicionado.")
            return
        add_event_in_db(nome, data, id_tema)
        print("Evento adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar evento: {e}")


def display_event_menu():
    # This function displays all events registered in the database.
    try:
        eventos = get_events_from_db()
        if not eventos:
            print("Nenhum evento cadastrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
    except Exception as e:
        print(f"Erro ao listar eventos: {e}")

def update_event_menu():
    # This function allows the user to update an existing event.
    # It prompts the user to select an event by ID and enter new details.
    # If no details are provided, it will not update the event.
    try:
        print("\n--- Alterar Evento ---")
        eventos = get_events_from_db()
        if not eventos:
            print("Nenhum evento cadastrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
        id_evento = int(input("Selecione o ID do evento que deseja alterar: "))
        nome = input("Novo nome do evento (deixe em branco para não alterar): ")
        data = input("Nova data do evento (dd/MM/AAAA) (deixe em branco para não alterar): ")
        tema = input("Novo tema do evento (deixe em branco para não alterar): ")
        update_event_in_db(id_evento, nome, data, tema)
        if not nome and not data and not tema:
            print("Nenhuma alteração foi feita.")
            return
        print("Evento alterado com sucesso.")
    except Exception as e:
        print(f"Erro ao alterar evento: {e}")

def event_removal_menu():
    # This function allows the user to remove an event by its ID.
    # It lists all events and prompts the user to select one for deletion.
    try:
        print("Eventos cadastrados:")
        eventos = get_events_from_db()
        if not eventos:
            print("\nNenhum evento cadastrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
        id_evento = int(input("Selecione o ID do evento que deseja excluir: "))
        if not id_evento:
            print("ID inválido. O evento não foi excluído.")
            return
        delete_event_from_db(id_evento)
        print("Evento excluído com sucesso.")
    except Exception as e:
        print(f"Erro ao excluir evento: {e}")

def search_event_menu():
    # This function allows the user to search for an event by ID, name, theme, or date.
    # It prompts the user to enter a search term and displays matching events.
    try:
        print("\n--- Buscar Evento ---")
        termo = input("Digite o termo de busca (ID, nome, tema ou data): ")
        eventos = search_event_in_db(termo)
        if not eventos:
            print("Nenhum evento encontrado.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
    except Exception as e:
        print(f"Erro ao buscar evento: {e}")