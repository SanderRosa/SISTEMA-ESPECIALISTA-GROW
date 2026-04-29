import sqlite3

def criar_banco():
    conn = sqlite3.connect("grow.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leituras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura REAL,
        umidade REAL,
        umidade_solo REAL,
        hora INTEGER,
        acoes TEXT
    )
    """)

    conn.commit()
    conn.close()


def salvar_leitura(temp, umid, solo, hora, acoes):
    conn = sqlite3.connect("grow.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leituras (temperatura, umidade, umidade_solo, hora, acoes)
    VALUES (?, ?, ?, ?, ?)
    """, (temp, umid, solo, hora, ", ".join(acoes)))

    conn.commit()
    conn.close()