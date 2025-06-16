from func_eventos import adicionar_evento, listar_eventos

def menu_eventos():
    while True:
        print("\n--- Menu de Eventos ---")
        print("1. Adicionar evento")
        print("2. Listar eventos")
        print("0. Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do evento: ")
            data = input("Data (AAAA-MM-DD): ")
            tema = input("Tema: ")
            adicionar_evento(nome, data, tema)
            print("Evento adicionado com sucesso.")
        elif opcao == "2":
            for evento in listar_eventos():
                print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")