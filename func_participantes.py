from database import conectar

def adicionar_participante(nome, email, preferencias):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO participantes (nome, email, preferencias) VALUES (?, ?, ?)",
                (nome, email, preferencias))
    conn.commit()
    conn.close()

def listar_participantes():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM participantes")
    participantes = cur.fetchall()
    conn.close()
    return participantes