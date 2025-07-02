from func_tema_bd import *
from utilidades_cod import limpa_terminal, continuar

def adicionar_tema():
    tema = input("Digite o nome do tema: ")
    descricao = input("Digite a descrição do tema: ")
    adicionar_tema_bd(tema, descricao)
    print("\nTema adicionado com sucesso!")

def listar_temas():
    temas = listar_temas_bd()
    if temas:
        print("\nLista de Temas:")
        for tema in temas:
            print(f"\nID: {tema[0]} | Tema: {tema[1]} | Descrição: {tema[2]}")
    else:
        print("\nNenhum tema encontrado.")

def remover_tema():
    id_tema = input("Digite o id do tema a ser removido: ")
    if id_tema:
        remover_tema_bd(id_tema)
        print("\nTema removido com sucesso!")
    else:
        print(f"Não foi possível encontrar o tema: {id_tema}")

def atualizar_tema():
    id_tema = input("Digite o id do tema a ser atualizado: ")
    if id_tema:
        novo_tema = input("Digite o novo nome do tema: ")
        nova_descricao = input("Digite a nova descrição do tema: ")
        atualizar_tema_bd(id_tema, novo_tema, nova_descricao)
        print("\nTema atualizado com sucesso!")
    else:
        print(f"Não foi possível encontrar o tema: {id_tema}")

def buscar_tema():
    termo = input("Digite o termo a ser buscado: ")
    resultados = buscar_tema_bd(termo)
    if resultados:
        print("\nResultados da busca:")
        for tema in resultados:
            print(f"ID: {tema[0]} | Tema: {tema[1]} | Descrição: {tema[2]}")
    else:
        print("\nNenhum tema encontrado.")