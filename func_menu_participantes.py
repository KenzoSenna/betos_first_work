from func_participantes_bd import *
from func_eventos_bd import get_events_from_db

def add_participant_menu():
    # This function allows the user to add a new participant.
    # It prompts the user for the participant's name, email, and thematic preferences.
    try:
        nome = input("\nNome do participante: ")
        email = input("Email: ")
        preferencias = input("Preferencias tematicas: ")
        add_participants_in_db(nome, email, preferencias)
        print("Participante cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar participante: {e}")

def display_participants_menu():
    # This function displays all participants registered in the database.
    # It retrieves the list of participants from the database and prints their details.
    try: 
        participantes = get_participants_from_db()
        [print(f"\nID: {p[0]} | Nome: {p[1]} | Email: {p[2]} | Preferencias: {p[3]}") for p in participantes]
        if not participantes:
            print("\nNenhum participante cadastrado.")
    except Exception as e:
        print(f"Erro ao listar participantes: {e}")

def participant_removal_menu():
    # This function allows the user to remove a participant by ID.
    # It prompts the user to enter the ID of the participant to be removed.
    try:
        id_participante = int(input("ID do participante a ser removido: "))
        if not id_participante:
            print("ID inválido. O participante não foi removido.")
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
        id_participante = int(input("\nID do participante a ser atualizado: "))
        nome = input("Novo nome (deixe em branco para não alterar): ")
        email = input("Novo email (deixe em branco para não alterar): ")
        preferencias = input("Novas preferências temáticas (deixe em branco para não alterar): ")
        if not id_participante:
            print("ID inválido. O participante não foi atualizado.")
            return
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
        id_participante = int(input("\nID do participante a ser buscado: "))
        participante = search_participants_in_db(id_participante)
        if not id_participante:
            print("ID inválido. O participante não foi encontrado.")
            return
        if participante:
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
        id_participante = int(input("\nID do participante a ser inscrito: "))
        if not id_participante:
            print("ID do participante inválido.")
            return
        print("Eventos disponíveis:")
        get_events_from_db()
        id_evento = int(input("ID do evento: "))
        if not id_participante or not id_evento:
            print("ID do participante ou do evento inválido.")
            return
        register_participant_to_event_db(id_participante, id_evento)
        print("\nParticipante inscrito no evento com sucesso.")
    except Exception as e:
        print(f"Erro ao inscrever participante no evento: {e}")