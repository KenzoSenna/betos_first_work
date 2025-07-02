from func_participantes_bd import listar_inscricoes_bd, listar_participantes_bd
from func_eventos_bd import listar_eventos

def total_participantes():
    try:
        return print(f"Total de Participantes Cadastrados: {len(listar_participantes_bd())}")
    except Exception as e:
        print(f"Errp ao listar total de participantes: {e}")

def total_inscricoes():
    try:
        inscricoes = listar_inscricoes_bd()
        if inscricoes:
            return print(f"Total de Inscrições: {len(inscricoes)}")
        else:
            return print("\nNenhuma inscrição encontrada.")
    except Exception as e:
        print(f"Erro ao listar total de inscrições: {e}")   
def participantes_por_evento():
    try:
        eventos = listar_eventos()
        for evento in eventos:
            participantes = (evento[0])
            print(f"\nEvento: {evento[1]} - Participantes: {len(participantes)}")
    except Exception as e:
        print(f"\nErro ao listar participantes por evento: {e}")

def temas_mais_preferidos():
    try:
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
    except Exception as e:
        print(f"\nErro ao listar temas mais preferidos: {e}")

def eventos_mais_populares():
    try:
        eventos = listar_eventos()
        participantes_por_evento = {evento[0]: len(evento[2]) for evento in eventos}
        
        print("\nEventos mais populares:")
        for evento_id, count in sorted(participantes_por_evento.items(), key=lambda x: x[1], reverse=True):
            print(f"Evento ID {evento_id}: {count} participantes")
    except Exception as e:
        print(f"\nErro listar eventos mais populares: {e}")

def eventos_por_tema():
    try:
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
    except Exception as e:
        print(f"\nErro ao listar eventos por tema: {e}")