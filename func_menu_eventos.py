from func_eventos_bd import *

def adicao_eventos_menu():
    nome = input("Nome do evento: ")
    data = input("Data (AAAA-MM-DD): ")
    tema = input("Tema: ")
    adicionar_evento(nome, data, tema)
    print("Evento adicionado com sucesso.")

def listar_eventos_menu():
    for evento in listar_eventos():
        print(f"ID: {evento[0]} | Nome: {evento[1]} | Data: {evento[2]} | Tema: {evento[3]}")