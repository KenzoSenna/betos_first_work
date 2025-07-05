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
        try:
            id_tema = int(input("Selecione o ID do tema para este evento: "))
            if id_tema <= 0:
                print("ID de tema inválido.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID do tema.")
            return
        nome = input("Nome do evento: ")
        if not nome.strip():
            print("Nome do evento não pode ser vazio.")
            return
        try:
            data_str = input("Data (DD/MM/AAAA): ")
            data = datetime.strptime(data_str, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida! Use o formato DD/MM/AAAA.")
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
        try:
            id_evento = int(input("Selecione o ID do evento que deseja alterar: "))
            if id_evento <= 0:
                print("ID inválido.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID do evento.")
            return
        nome = input("Novo nome do evento (deixe em branco para não alterar): ")
        data = input("Nova data do evento (DD/MM/AAAA) (deixe em branco para não alterar): ")
        id_tema = input("Novo ID do tema (deixe em branco para não alterar): ")
        
        if data:
            try:
                data = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")
                return
        else:
            data = None
        
        if id_tema:
            try:
                id_tema = int(id_tema)
                if id_tema <= 0:
                    print("ID de tema inválido.")
                    return
            except ValueError:
                print("Por favor, digite um número válido para o ID do tema.")
                return
        else:
            id_tema = None
        if not nome and not data and not id_tema:
            print("Nenhuma alteração foi feita.")
            return
        update_event_in_db(id_evento, nome or None, data, id_tema)
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
        try:
            id_evento = int(input("Selecione o ID do evento que deseja excluir: "))
            if id_evento <= 0:
                print("ID inválido. O evento não foi excluído.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID do evento.")
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