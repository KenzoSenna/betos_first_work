from func_participantes_bd import listar_participantes, listar_inscricoes
from func_eventos_bd import listar_eventos


def total_participantes():
    return print(f"Total de Participantes Cadastrados: {len(listar_participantes())}")

def total_inscricoes():
    inscricoes = listar_inscricoes()
    if inscricoes:
        return print(f"Total de Inscrições: {len(inscricoes)}")
    else:
        return print("Nenhuma inscrição encontrada.")
    
def participantes_por_evento():
    eventos = listar_eventos()
    for evento in eventos:
        participantes = (evento[0])
        print(f"\nEvento: {evento[1]} - Participantes: {len(participantes)}")



