from database import conectar

def adicionar_evento_bd(nome, data, id_tema):
    conn = conectar()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO eventos (nome, data, id_tema) VALUES (?, ?, ?)",
        (nome, data, id_tema)
    )
    conn.commit()
    conn.close()

def listar_eventos_bd():
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

def alterar_evento_bd(id_evento, nome=None, data=None, id_tema=None):
    
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

def excluir_evento_bd(id_evento):
    
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM eventos WHERE id = ?", (id_evento,))
    conn.commit()
    conn.close()

def buscar_evento_bd(termo):
    try:

        conn = conectar()
        cur = conn.cursor()
        termo_busca = f"%{termo}%"
        cur.execute(
            "SELECT * FROM eventos WHERE CAST(id AS TEXT) LIKE ? OR nome LIKE ? OR tema LIKE ? OR data LIKE ?",
            (termo_busca, termo_busca, termo_busca, termo_busca)
        )
        evento = cur.fetchall()
        conn.close()
        return evento
    except Exception as e:
        print(f"Erro ao buscar evento: {e}")