from database import conectar
from datetime import datetime

def add_event_in_db(nome, data, id_tema):
    # This function adds a new event to the database.
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        print("Data inválida! Use o formato DD/MM/AAAA.")
        return

    conn = conectar()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO eventos (nome, data, id_tema) VALUES (?, ?, ?)",
        (nome, data, id_tema)
    )
    conn.commit()
    conn.close()

def get_events_from_db():
     # This function retrieves all events from the database.
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT e.id, e.nome, e.data, t.nome
            FROM eventos e
            LEFT JOIN tema t ON e.id_tema = t.id_tema
            """
        )
        eventos = cur.fetchall()
        conn.close()
        return eventos
        
def update_event_in_db(id_evento, nome=None, data=None, id_tema=None):
    # This function updates an existing event in the database.
    conn = conectar()
    cur = conn.cursor()
    if nome:
        cur.execute("UPDATE eventos SET nome = ? WHERE id = ?", (nome, id_evento))
    if data:
        cur.execute("UPDATE eventos SET data = ? WHERE id = ?", (data, id_evento))
    if id_tema is not None:
        cur.execute("UPDATE eventos SET id_tema = ? WHERE id = ?", (id_tema, id_evento))
    conn.commit()
    conn.close()

def delete_event_from_db(id_evento):
    # This function deletes an event from the database by its ID.
    
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM eventos WHERE id = ?", (id_evento,))
    conn.commit()
    conn.close()

def search_event_in_db(termo):
    try:
        conn = conectar()
        cur = conn.cursor()
        termo_busca = f"%{termo}%"
        cur.execute(
            "SELECT * FROM eventos WHERE CAST(id AS TEXT) LIKE ? OR nome LIKE ? OR id_tema LIKE ? OR data LIKE ?",
            (termo_busca, termo_busca, termo_busca, termo_busca)
        )
        evento = cur.fetchall()
        conn.close()
        return evento
    except Exception as e:
        print(f"Erro ao buscar evento: {e}")
        return []