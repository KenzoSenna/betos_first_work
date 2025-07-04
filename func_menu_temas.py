from func_tema_bd import *

def add_themes_menu():
    # This function allows the user to add a new theme to the database.
    # It first retrieves the most preferred themes from the database and then prompts the user to input
    try:
        from func_menu_temas import temas_mais_preferidos
        temas_preferidos = temas_mais_preferidos()
        if temas_preferidos:
            print("\nTemas que os participantes disseram preferir:")
            for tema in temas_preferidos:
                print(f"ID: {tema[0]} | Tema: {tema[1]} | Descrição: {tema[2]}")
        tema = input("\nDigite o nome do tema: ")
        descricao = input("Digite a descrição do tema: ")
        add_themes_in_db(tema, descricao)
        print("\nTema adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar temas: {e}")

def display_themes_menu():
    # This function retrieves and displays all themes from the database.
    # It prints the ID, name, and description of each theme.
    try:
        temas = display_themes_from_db()
        if temas:
            print("\nLista de Temas:")
            for tema in temas:
                print(f"\nID: {tema[0]} | Tema: {tema[1]} | Descrição: {tema[2]}")
        else:
            print("\nNenhum tema encontrado.")
    except Exception as e:
        print(f"Erro ao listar temas: {e}")

def themes_removal_menu():
    # This function allows the user to remove a theme from the database.
    # It prompts the user to input the ID of the theme they wish to remove.
    try:
        id_tema = input("Digite o id do tema a ser removido: ")
        if id_tema:
            theme_removal_in_db(id_tema)
            print("\nTema removido com sucesso!")
        else:
            print(f"Não foi possível encontrar o tema: {id_tema}")
    except Exception as e:
        print(f"Erro ao remover tema: {e}")

def themes_update_menu():
    # This function allows the user to update an existing theme in the database.
    # It prompts the user to input the ID of the theme they wish to update,
    try:
        id_tema = input("Digite o id do tema a ser atualizado: ")
        if id_tema:
            novo_tema = input("Digite o novo nome do tema: ")
            nova_descricao = input("Digite a nova descrição do tema: ")
            theme_update_in_db(id_tema, novo_tema, nova_descricao)
            print("\nTema atualizado com sucesso!")
        else:
            print(f"Não foi possível encontrar o tema: {id_tema}")
    except Exception as e:
        print(f"Erro ao buscar tema: {e}")

def theme_search_menu():
    # This function allows the user to search for a theme by its name or ID.
    # It prompts the user to input a search term and retrieves matching themes from the database.
    try:
        termo = input("Digite o Nome ou ID do tema a ser buscado: ")
        resultados = search_theme_from_db(termo)
        if resultados:
            print("\nResultados da busca:")
            for tema in resultados:
                print(f"ID: {tema[0]} | Tema: {tema[1]} | Descrição: {tema[2]}")
        else:
            print("\nNenhum tema encontrado.")
    except Exception as e:
        print(f"\nErro ao buscar tema: {e}")
