import sqlite3

def conectar():
    return sqlite3.connect("base_eventos.db")

def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()

    # Cria tabela de participantes
    cur.execute('''
    CREATE TABLE IF NOT EXISTS participantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        preferencias TEXT
    )''')

    # Cria tabela de eventos
    cur.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data TEXT NOT NULL,
        tema TEXT
    )''')

    # Cria tabela de inscricoes
    cur.execute('''
    CREATE TABLE IF NOT EXISTS inscricoes (
        id_evento INTEGER,
        id_participante INTEGER,
        FOREIGN KEY(id_evento) REFERENCES eventos(id),
        FOREIGN KEY(id_participante) REFERENCES participantes(id)
    )''')

    conn.commit()
    conn.close()