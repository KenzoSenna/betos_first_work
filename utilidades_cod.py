import os

def clean_terminal_by_op_sys():
    # This function clears the terminal screen based on the operating system.
    # It uses 'cls' for Windows and 'clear' for Unix-like systems.
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"erro ao limpar o terminal: {e}")
def continue_by_pressing_enter():
    # This function prompts the user to press Enter to continue.
    # It waits for the user to press Enter before returning and cleaning the terminal.
    resposta_user = input("<<< APERTE ENTER para continuar >>>\n")
    if resposta_user == "":
        return
    return continue_by_pressing_enter()