from database import conectar

def adicionar_evento(nome, data, tema):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO eventos (nome, data, tema) VALUES (?, ?, ?)", (nome, data, tema))
    conn.commit()
    conn.close()

def listar_eventos():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventos")
    eventos = cur.fetchall()
    conn.close()
    return eventos