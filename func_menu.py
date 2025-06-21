from func_participantes import adicionar_participante, listar_participantes
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
