from func_participantes import adicionar_participante, listar_participantes

def menu_participantes():
    while True:
        print("\n--- Menu de Participantes ---")
        print("1. Adicionar participante")
        print("2. Listar participantes")
        print("0. Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do participante: ")
            email = input("Email: ")
            preferencias = input("Preferencias tematicas: ")
            adicionar_participante(nome, email, preferencias)
            print("Participante cadastrado com sucesso.")
        elif opcao == "2":
            for p in listar_participantes():
                print(f"ID: {p[0]} | Nome: {p[1]} | Email: {p[2]} | Preferencias: {p[3]}")
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")