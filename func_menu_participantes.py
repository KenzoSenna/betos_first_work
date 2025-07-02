from func_participantes_bd import *

def adicionar_participante_menu():
    try:
        nome = input("\nNome do participante: ")
        email = input("Email: ")
        preferencias = input("Preferencias tematicas: ")
        adicionar_participante(nome, email, preferencias)
        print("Participante cadastrado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar participante: {e}")

def listar_participantes_menu():
    try: 
        participantes = listar_participantes_bd()
        [print(f"\nID: {p[0]} | Nome: {p[1]} | Email: {p[2]} | Preferencias: {p[3]}") for p in participantes]
        if not participantes:
            print("\nNenhum participante cadastrado.")
    except Exception as e:
        print(f"Erro ao listar participantes: {e}")

def remover_participantes_menu():
    try:
        id_participante = int(input("ID do participante a ser removido: "))
        remover_participante_bd(id_participante)
        print("\nParticipante removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover participante: {e}")


def atualizar_participantes_menu():
    try:
        id_participante = int(input("\nID do participante a ser atualizado: "))
        nome = input("Novo nome (deixe em branco para não alterar): ")
        email = input("Novo email (deixe em branco para não alterar): ")
        preferencias = input("Novas preferências temáticas (deixe em branco para não alterar): ")
        
        atualizar_participant_bd(id_participante, nome or None, email or None, preferencias or None)
        print("\nParticipante atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar o participante: {e}")

def buscar_participantes_menu():
    try:
        id_participante = int(input("\nID do participante a ser buscado: "))
        participante = buscar_participante_bd(id_participante)

        if participante:
            print(f"ID: {participante[0]} | Nome: {participante[1]} | Email: {participante[2]} | Preferencias: {participante[3]}")
        else:
            print("Participante não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar participante: {e}")