import bcrypt
import random
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from database import conectar

load_dotenv()

emailenv = os.getenv('emailenv')
senha_app_email = os.getenv('senha_app_email')

def gerar_cod():
    return f"meow{random.randint(0, 9999)}"

def criar_user(username, email, senha):

    hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
    codigo = gerar_cod()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO usuarios (username, email, senha_hash, codigo, email_verificado)
    VALUES (?, ?, ?, ?, ?)
""",(username, email, hash, codigo, 0))

    conexao.commit()
    conexao.close()

def veri_user_email(email):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT codigo
        FROM usuarios
        WHERE email = ?
""", (email,))

    cod = cursor.fetchone()

    conexao.close()

    msg = EmailMessage()
    msg['Subject'] = 'Código de verificação Ronrom'
    msg['From'] = emailenv
    msg['To'] = email
    msg.set_content(f'Olá, este é o email de verificação da Ronrom. Seu código de verificação de email é {cod[0]}, não compartilhe o código de verificação para ninguém!')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(emailenv, senha_app_email)
        smtp.send_message(msg)

def veri_cod(email, codigo):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT codigo
        FROM usuarios
        WHERE email = ? AND codigo = ?
""", (email, codigo))

    cod = cursor.fetchone()

    conexao.close()

    if cod:
        return True

    return False

def confirmar_email(email):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE usuarios
        SET email_verificado = 1
        WHERE email = ?
""", (email,))

    conexao.commit()
    conexao.close()