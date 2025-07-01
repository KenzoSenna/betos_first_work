import os

def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    resposta_user = input("<<< Digite ENTER para continuar >>>\n")
    if resposta_user == "":
        return
    return continuar()