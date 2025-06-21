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

def remover_participante(id_participante):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM participantes WHERE id = ?", (id_participante,))
    conn.commit()
    conn.close()
    
def atualizar_participante(id_participante, nome=None, email=None, preferencias=None):
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

def buscar_participante_por_id(id_participante):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM participantes WHERE id = ?", (id_participante,))
    participante = cur.fetchone()
    conn.close()
    return participante

def buscar_participante_por_nome(nome):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM participantes WHERE nome LIKE ?", ('%' + nome + '%',))
    participantes = cur.fetchall()
    conn.close()
    return participantes
