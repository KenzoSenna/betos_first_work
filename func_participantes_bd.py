from database import conectar

def adicionar_participante(nome, email, preferencias):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO participantes (nome, email, preferencias) VALUES (?, ?, ?)",
                (nome, email, preferencias))
    conn.commit()
    conn.close()

def listar_participantes_bd():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM participantes")
    participantes = cur.fetchall()
    conn.close()
    return participantes

def inscrever_participante_bd(id_evento, id_participante):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO inscricoes (id_evento, id_participante) VALUES (?, ?)",
                (id_evento, id_participante))
    conn.commit()
    conn.close()

def listar_inscricoes_bd():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM inscricoes")
    inscricoes = cur.fetchall()
    conn.close()
    return inscricoes

def remover_participante_bd(id_participante):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM participantes WHERE id = ?", (id_participante,))
    conn.commit()
    conn.close()

def atualizar_participant_bd(id_participante, nome=None, email=None, preferencias=None):
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

def buscar_participante_bd(parametro):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM participantes WHERE id = ? OR nome LIKE ?", (parametro, '%' + parametro + '%'))
    participante = cur.fetchall()
    conn.close()
    return participante

