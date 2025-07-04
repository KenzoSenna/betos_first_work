import os

def limpa_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"erro ao limpar o terminal: {e}")
def continuar():
    resposta_user = input("<<< APERTE ENTER para continuar >>>\n")
    if resposta_user == "":
        return
    return continuar()