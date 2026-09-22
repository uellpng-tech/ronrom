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
        email_verificado BOOLEAN NOT NULL DEFAULT FALSE,
        codigo_expira_em DATETIME,
        foto_user TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS gatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cor TEXT,
        idade_aproximada TEXT,
        sexo TEXT,
        peso REAL,
        castrado BOOLEAN NOT NULL DEFAULT FALSE,
        vacinado BOOLEAN NOT NULL DEFAULT FALSE,
        vermifugado BOOLEAN NOT NULL DEFAULT FALSE,
        fiv BOOLEAN NOT NULL DEFAULT FALSE,
        felv BOOLEAN NOT NULL DEFAULT FALSE,
        deficiente BOOLEAN NOT NULL DEFAULT FALSE,
        comportamento TEXT,
        historico_resgate TEXT,
        foto TEXT,
        video TEXT,
        usuario_id INTERAGER NOT NULL,
        CRIADO_em DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
""")

conexao.commit()
conexao.close()