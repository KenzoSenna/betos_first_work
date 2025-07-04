from database import conectar

def add_participants_in_db(nome, email, preferencias):
    # This function adds a new participant to the database.
    # It connects to the database and inserts the participant's details.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO participantes (nome, email, preferencias) VALUES (?, ?, ?)",
                (nome, email, preferencias))
    conn.commit()
    conn.close()

def get_participants_from_db():
    # This function retrieves all participants from the database.
    # It connects to the database and fetches all records from the participantes table.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM participantes")
    participantes = cur.fetchall()
    conn.close()
    return participantes

def register_participant_to_event_db(id_evento, id_participante):
    # This function registers a participant to an event in the database.
    # It connects to the database and inserts a record into the inscricoes table.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO inscricoes (id_evento, id_participante) VALUES (?, ?)",
                (id_evento, id_participante))
    conn.commit()
    conn.close()

def display_inscriptions_from_db():
    # This function retrieves all inscriptions from the database.
    # It connects to the database and fetches all records from the inscricoes table.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inscricoes")
    inscricoes = cur.fetchall()
    conn.close()
    return inscricoes

def participant_removal_in_db(id_participante):
    # This function removes a participant from the database by their ID.
    # It connects to the database and deletes the participant's record from the participantes table.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM participantes WHERE id = ?", (id_participante,))
    conn.commit()
    conn.close()

def update_participants_in_db(id_participante, nome=None, email=None, preferencias=None):
    # This function updates an existing participant's details in the database.
    # It connects to the database and updates the participant's record in the participantes table.
    conn = conectar()
    cur = conn.cursor()
    if nome:
        cur.execute("UPDATE participantes SET nome = ? WHERE id = ?", (nome, id_participante))
    if email:
        cur.execute("UPDATE participantes SET email = ? WHERE id = ?", (email, id_participante))
    if preferencias:
        cur.execute("UPDATE participantes SET preferencias = ? WHERE id = ?", (preferencias, id_participante))
    conn.commit()
    conn.close()

def search_participants_in_db(parametro):
    # This function searches for a participant in the database by ID or name.
    # It connects to the database and retrieves records from the participantes table that match the search criteria
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM participantes WHERE id = ? OR nome LIKE ?", (parametro, '%' + parametro + '%'))
    participante = cur.fetchall()
    conn.close()
    return participante

def register_participant_to_event_db(id_participante, id_evento):
    # This function register the participant into events in the database by values ID_pariticipante and ID_evento
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO inscricoes (id_participante, id_evento) VALUES (?, ?)",
                (id_participante, id_evento))
    conn.commit()
    conn.close()