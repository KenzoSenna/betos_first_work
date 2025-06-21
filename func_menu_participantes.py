from func_participantes_bd import *
def adicionar():
    nome = input("Nome do participante: ")
    email = input("Email: ")
    preferencias = input("Preferencias tematicas: ")
    adicionar_participante(nome, email, preferencias)
    print("Participante cadastrado com sucesso.")

def listar():
    participantes = listar_participantes()
    [print(f"ID: {p[0]} | Nome: {p[1]} | Email: {p[2]} | Preferencias: {p[3]}") for p in participantes]
    if not participantes:
        print("Nenhum participante cadastrado.")
def remover():
    id_participante = int(input("ID do participante a ser removido: "))
    remover_participante(id_participante)
    print("Participante removido com sucesso.")

def atualizar():
    id_participante = int(input("ID do participante a ser atualizado: "))
    nome = input("Novo nome (deixe em branco para não alterar): ")
    email = input("Novo email (deixe em branco para não alterar): ")
    preferencias = input("Novas preferências temáticas (deixe em branco para não alterar): ")
    
    atualizar_participante(id_participante, nome or None, email or None, preferencias or None)
    print("Participante atualizado com sucesso.")
def buscar_por_id():
    id_participante = int(input("ID do participante a ser buscado: "))
    participante = buscar_participante_por_id(id_participante)

    if participante:
        print(f"ID: {participante[0]} | Nome: {participante[1]} | Email: {participante[2]} | Preferencias: {participante[3]}")
    else:
        print("Participante não encontrado.")
        
def buscar_por_nome():
    nome = input("Nome do participante a ser buscado: ")
    participantes = buscar_participante_por_nome(nome)

    if participantes:
        for p in participantes:
            print(f"ID: {p[0]} | Nome: {p[1]} | Email: {p[2]} | Preferencias: {p[3]}")
    else:
        print("Nenhum participante encontrado com esse nome.")