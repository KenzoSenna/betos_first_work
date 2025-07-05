from func_participantes_bd import *
from func_eventos_bd import get_events_from_db

def add_participant_menu():
    # This function allows the user to add a new participant.
    # It prompts the user for the participant's name, email, and thematic preferences.
    try:
        nome = input("\nNome do participante: ")
        email = input("Email: ")
        preferencias = input("Preferencias tematicas: ")
        if not nome.strip() or not email.strip():
            print("Nome e email são obrigatórios.")
            return
        add_participants_in_db(nome, email, preferencias)
        print("Participante cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar participante: {e}")

def display_participants_menu():
    # This function displays all participants registered in the database.
    # It retrieves the list of participants from the database and prints their details.
    try: 
        participantes = get_participants_from_db()
        if participantes:
            for p in participantes:
                print(f"\nID: {p[0]} | Nome: {p[1]} | Email: {p[2]} | Preferencias: {p[3]}")
        else:
            print("\nNenhum participante cadastrado.")
    except Exception as e:
        print(f"Erro ao listar participantes: {e}")

def participant_removal_menu():
    # This function allows the user to remove a participant by ID.
    # It prompts the user to enter the ID of the participant to be removed.
    try:
        try:
            id_participante = int(input("ID do participante a ser removido: "))
            if id_participante <= 0:
                print("ID inválido. O participante não foi removido.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID.")
            return
        participant_removal_in_db(id_participante)
        print("\nParticipante removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover participante: {e}")


def update_participants_menu():
    # This function allows the user to update an existing participant's details.
    # It lists all participants, prompts the user to select one by ID,
    try:
        print("Participantes cadastrados:")
        display_participants_menu()
        try:
            id_participante = int(input("\nID do participante a ser atualizado: "))
            if id_participante <= 0:
                print("ID inválido. O participante não foi atualizado.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID.")
            return
        nome = input("Novo nome (deixe em branco para não alterar): ")
        email = input("Novo email (deixe em branco para não alterar): ")
        preferencias = input("Novas preferências temáticas (deixe em branco para não alterar): ")
        if not nome and not email and not preferencias:
            print("Nenhuma alteração foi feita.")
            return
        update_participants_in_db(id_participante, nome or None, email or None, preferencias or None)
        print("\nParticipante atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar o participante: {e}")

def search_participant_menu():
    # This function allows the user to search for a participant by ID.
    # It prompts the user to enter an ID and displays the participant's details if found.
    try:
        try:
            id_participante = int(input("\nID do participante a ser buscado: "))
            if id_participante <= 0:
                print("ID inválido. O participante não foi encontrado.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID.")
            return
        participantes = search_participants_in_db(id_participante)
        if participantes:
            for participante in participantes:
                print(f"ID: {participante[0]} | Nome: {participante[1]} | Email: {participante[2]} | Preferencias: {participante[3]}")
        else:
            print("Participante não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar participante: {e}")

def subscribe_participant_to_event():
    # This function allows the user to subscribe a participant to an event.
    # It lists all participants and events, then prompts the user to select one of each.
    # it checks if the participant and event IDs are valid before proceeding with the subscription.
    try:
        print("Participantes cadastrados:")
        display_participants_menu()
        try:
            id_participante = int(input("\nID do participante a ser inscrito: "))
            if id_participante <= 0:
                print("ID do participante inválido.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID do participante.")
            return
        print("Eventos disponíveis:")
        eventos = get_events_from_db()
        if not eventos:
            print("Nenhum evento disponível.")
            return
        for evento in eventos:
            print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
        try:
            id_evento = int(input("ID do evento: "))
            if id_evento <= 0:
                print("ID do evento inválido.")
                return
        except ValueError:
            print("Por favor, digite um número válido para o ID do evento.")
            return
        # Verificação de inscrição duplicada pode ser feita aqui, se desejar
        register_participant_to_event_db(id_participante, id_evento)
        print("\nParticipante inscrito no evento com sucesso.")
    except Exception as e:
        print(f"Erro ao inscrever participante no evento: {e}")