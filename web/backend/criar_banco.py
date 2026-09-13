import sqlite3

conexao = sqlite3.connect("web/database/ronrom.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha_hash TEXT NOT NULL,
        codigo TEXT,
        email_verificado BOLEAN NOT NULL DEFAULT FALSE
    )
""")

conexao.commit()
conexao.close()