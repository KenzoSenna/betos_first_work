from func_participantes_bd import listar_inscricoes_bd, listar_participantes_bd
from func_eventos_bd import listar_eventos


def total_participantes():
    return print(f"Total de Participantes Cadastrados: {len(listar_participantes_bd())}")

def total_inscricoes():
    inscricoes = listar_inscricoes_bd()
    if inscricoes:
        return print(f"Total de Inscrições: {len(inscricoes)}")
    else:
        return print("Nenhuma inscrição encontrada.")
    
def participantes_por_evento():
    eventos = listar_eventos()
    for evento in eventos:
        participantes = (evento[0])
        print(f"\nEvento: {evento[1]} - Participantes: {len(participantes)}")

def temas_mais_preferidos():
    eventos = listar_eventos()
    temas = {}
    
    for evento in eventos:
        tema = evento[3]
        if tema in temas:
            temas[tema] += 1
        else:
            temas[tema] = 1
    
    print("\nTemas mais preferidos:")
    for tema, count in sorted(temas.items(), key=lambda x: x[1], reverse=True):
        print(f"{tema}: {count} participantes")

def eventos_mais_populares():
    eventos = listar_eventos()
    participantes_por_evento = {evento[0]: len(evento[2]) for evento in eventos}
    
    print("\nEventos mais populares:")
    for evento_id, count in sorted(participantes_por_evento.items(), key=lambda x: x[1], reverse=True):
        print(f"Evento ID {evento_id}: {count} participantes")

def eventos_por_tema():
    eventos = listar_eventos()
    temas = {}
    
    for evento in eventos:
        tema = evento[3]
        if tema in temas:
            temas[tema].append(evento)
        else:
            temas[tema] = [evento]
    
    print("\nEventos por Tema:")
    for tema, eventos_lista in temas.items():
        print(f"\nTema: {tema}")
        for evento in eventos_lista:
            print(f"Evento ID {evento[0]}: {evento[1]} - Data: {evento[2]}")