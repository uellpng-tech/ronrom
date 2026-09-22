import bcrypt
import random
import smtplib
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from email.message import EmailMessage
from database import conectar

def editar_user(username, email, senha, foto_user, email_atual):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT username, email, senha_hash, foto_user
    FROM usuarios
    WHERE email = ?
""", (email_atual,))

    usuario = cursor.fetchone()

    if usuario is None:
        conexao.close()
        return False

    username_atual, email_atual_db, senha_atual, foto_atual = usuario

    if not username:
        username = username_atual

    if not email:
        email = email_atual_db

    if not foto_user:
        foto_user = foto_atual

    if senha:
        senha = bcrypt.hashpw(
            senha.encode("utf-8"),
            bcrypt.gensalt()
        )
    else:
        senha = senha_atual

    cursor.execute("""
    SELECT id
    FROM usuarios
    WHERE (username = ? OR email = ?)
    AND email != ?
""", (username, email, email_atual_db))

    usuario_existente = cursor.fetchone()

    if usuario_existente:
        conexao.close()
        return "usuario_ou_email_inexistente"

    cursor.execute("""
    UPDATE usuarios
    SET username = ?,
        email = ?,
        senha_hash = ?,
        foto_user = ?
    WHERE email = ?
""", (username, email, senha, foto_user, email_atual_db))

    conexao.commit()
    conexao.close()

    return {
        "username": username,
        "email": email,
        "foto_user": foto_user
    }

def confirmar_senha_user(email, senha):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT senha_hash
        FROM usuarios
        WHERE email = ?
""", (email,))

    usuario = cursor.fetchone()

    conexao.close()

    if usuario is None:
        return False

    senha_hash = usuario[0]

    return bcrypt.checkpw(
        senha.encode("utf-8"),
        senha_hash
    )

def resetar_senha_email(email, senha, senha_nova):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT senha_hash
    FROM usuarios
    WHERE email = ?
""", (email,))

    usuario = cursor.fetchone()

    if usuario is None:
        conexao.close()
        return False

    senha_hash = usuario[0]

    if not bcrypt.checkpw(
        senha.encode("utf-8"),
        senha_hash
    ):
        conexao.close()
        return "senha_incorreta"

    nova_senha_hash = bcrypt.hashpw(
        senha_nova.encode("utf-8"),
        bcrypt.gensalt()
    )

    cursor.execute("""
        UPDATE usuarios
        SET senha_hash = ?
        WHERE email = ?
""", (nova_senha_hash, email))

    conexao.commit()
    conexao.close()

    return True
