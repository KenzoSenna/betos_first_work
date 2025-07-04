from database import conectar


def add_themes_in_db(nome, descricao=None):
    # This function adds a new theme to the database.
    # It connects to the database and inserts the theme's name and description.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO tema (nome, descricao) VALUES (?, ?)", (nome, descricao))
    conn.commit()
    conn.close()

def display_themes_from_db():
    # This function retrieves all themes from the database.
    # It connects to the database and fetches all records from the tema table.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tema")
    temas = cur.fetchall()
    conn.close()
    return temas

def theme_removal_in_db(id_tema):
    # This function removes a theme from the database by its ID.
    # It connects to the database and deletes the theme's record from the tema table.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM tema WHERE id_tema = ?", (id_tema,))
    conn.commit()
    conn.close()

def theme_update_in_db(id_tema, novo_tema, nova_descricao):
    # This function updates an existing theme in the database.
    # It connects to the database and updates the theme's name and description based on its ID.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("UPDATE tema SET nome = ?, descricao = ? WHERE id_tema = ?", (novo_tema, nova_descricao, id_tema))
    conn.commit()
    conn.close()

def search_theme_from_db(termo):
    # This function searches for themes in the database by name or ID.
    # It connects to the database and retrieves themes that match the search term.
    # The search term can be a partial match for both the theme name and ID.
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