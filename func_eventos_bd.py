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

def alterar_evento(id_evento, nome=None, data=None, tema=None):
    conn = conectar()
    cur = conn.cursor()
    
    if nome:
        cur.execute("UPDATE eventos SET nome = ? WHERE id = ?", (nome, id_evento))
    if data:
        cur.execute("UPDATE eventos SET data = ? WHERE id = ?", (data, id_evento))
    if tema:
        cur.execute("UPDATE eventos SET tema = ? WHERE id = ?", (tema, id_evento))
    conn.commit()
    conn.close()

def excluir_evento(id_evento):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM eventos WHERE id = ?", (id_evento,))
    conn.commit()
    conn.close()

def buscar_evento(termo):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventos WHERE id LIKE ? or nome LIKE ? or tema LIKE ? or data LIKE ?", (termo, termo, termo, termo))
    evento = cur.fetchall()
    conn.close()
    return evento
