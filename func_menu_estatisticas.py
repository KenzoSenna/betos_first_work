from func_participantes_bd import display_inscriptions_from_db, get_participants_from_db
from func_eventos_bd import get_events_from_db

def participants_total():
    # This function lists the total number of participants.
    # It assumes that the participants data is stored in a database.
    try:
        return print(f"Total de Participantes Cadastrados: {len(get_participants_from_db())}")
    except Exception as e:
        print(f"Errp ao listar total de participantes: {e}")

def inscriptions_total():
    # This function lists the total number of inscriptions.
    # It assumes that the inscriptions data is stored in a database.
    try:
        inscricoes = display_inscriptions_from_db()
        if inscricoes:
            return print(f"Total de Inscrições: {len(inscricoes)}")
        else:
            return print("\nNenhuma inscrição encontrada.")
    except Exception as e:
        print(f"Erro ao listar total de inscrições: {e}")   
def participantes_por_evento():
    try:
        eventos = get_events_from_db()
        for evento in eventos:
            participantes = (evento[0])
            print(f"\nEvento: {evento[1]} - Participantes: {len(participantes)}")
    except Exception as e:
        print(f"\nErro ao listar participantes por evento: {e}")

def most_popular_themes():
    # This function lists the most preferred themes based on the number of participants.
    # It assumes that the event data includes a theme field.
    try:
        eventos = get_events_from_db()
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

def most_popular_events():
    # This function lists the most popular events based on the number of participants.
    # It assumes that the event data includes a list of participants.
    try:
        eventos = get_events_from_db()
        participantes_por_evento = {evento[0]: len(evento[2]) for evento in eventos}
        if not participantes_por_evento:
            print("\nNenhum evento encontrado.")
            return
        
        print("\nEventos mais populares:")
        for evento_id, count in sorted(participantes_por_evento.items(), key=lambda x: x[1], reverse=True):
            print(f"Evento ID {evento_id}: {count} participantes")
    except Exception as e:
        print(f"\nErro listar eventos mais populares: {e}")

def events_in_themes():
    # This function lists events grouped by their themes.
    try:
        eventos = get_events_from_db()
        temas = {}
        if not eventos:
            print("\nNenhum evento encontrado.")
            return
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