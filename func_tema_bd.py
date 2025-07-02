from database import conectar


def adicionar_tema_bd(nome, descricao=None):
    
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO tema (nome, descricao) VALUES (?, ?)", (nome, descricao))
    conn.commit()
    conn.close()

def listar_temas_bd():

    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tema")
    temas = cur.fetchall()
    conn.close()
    return temas

def remover_tema_bd(id_tema):

    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM tema WHERE id_tema = ?", (id_tema,))
    conn.commit()
    conn.close()

def atualizar_tema_bd(id_tema, novo_tema):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("UPDATE temas SET tema = ? WHERE id_tema = ?", (novo_tema, id_tema))
    conn.commit()
    conn.close()

def buscar_tema_bd(termo):
    try:
        conn = conectar()
        cur = conn.cursor()
        termo_busca = f"%{termo}%"
        cur.execute(
            "SELECT * FROM tema WHERE id_tema LIKE ? OR tema LIKE ?",
            (termo_busca, termo_busca)
        )
        temas = cur.fetchall()
        conn.close()
        return temas
    except Exception as e:
        print(f"Erro ao buscar tema: {e}")