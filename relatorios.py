from database import conectar

def mostrar_estatisticas():
    conn = conectar()
    cur = conn.cursor()

    print("\n--- Participantes mais ativos ---")
    cur.execute('''
        SELECT p.nome, COUNT(*) as total
        FROM participantes p
        JOIN inscricoes i ON p.id = i.id_participante
        GROUP BY p.id
        ORDER BY total DESC
        LIMIT 3
    ''')
    for nome, total in cur.fetchall():
        print(f"{nome} - {total} eventos")

    print("\n--- Temas mais populares ---")
    cur.execute('''
        SELECT tema, COUNT(*) as qtd FROM eventos
        GROUP BY tema ORDER BY qtd DESC LIMIT 3
    ''')
    for tema, qtd in cur.fetchall():
        print(f"{tema} - {qtd} eventos")

    conn.close()