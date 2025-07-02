from func_participantes_bd import *

def adicionar():
    nome = input("\nNome do participante: ")
    email = input("Email: ")
    preferencias = input("Preferencias tematicas: ")
    adicionar_participante(nome, email, preferencias)
    print("Participante cadastrado com sucesso.")

def listar():
    participantes = listar_participantes_bd()
    [print(f"\nID: {p[0]} | Nome: {p[1]} | Email: {p[2]} | Preferencias: {p[3]}") for p in participantes]
    if not participantes:
        print("\nNenhum participante cadastrado.")

def remover():
    id_participante = int(input("ID do participante a ser removido: "))
    remover_participante_bd(id_participante)
    print("\nParticipante removido com sucesso.")

def atualizar():
    id_participante = int(input("\nID do participante a ser atualizado: "))
    nome = input("Novo nome (deixe em branco para não alterar): ")
    email = input("Novo email (deixe em branco para não alterar): ")
    preferencias = input("Novas preferências temáticas (deixe em branco para não alterar): ")
    
    atualizar_participant_bd(id_participante, nome or None, email or None, preferencias or None)
    print("\nParticipante atualizado com sucesso.")

def buscar_participante():
    id_participante = int(input("\nID do participante a ser buscado: "))
    participante = buscar_participante_bd(id_participante)

    if participante:
        print(f"ID: {participante[0]} | Nome: {participante[1]} | Email: {participante[2]} | Preferencias: {participante[3]}")
    else:
        print("Participante não encontrado.")