import bcrypt
from database import conectar

def gerar_cod()

def criar_user(username, email, senha):

    hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO usuarios (username, email, senha_hash)
    VALUES (?, ?, ?, ?, ?, ?)
""",(username, email, hash, codigo, 0))

    conexao.commit()
    conexao.close()

def veri_user(email):

    conexao = 