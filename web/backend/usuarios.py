import bcrypt
import random
import smtplib
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from email.message import EmailMessage
from database import conectar

load_dotenv()

emailenv = os.getenv('emailenv')
senha_app_email = os.getenv('senha_app_email')

def gerar_cod():
    return f"meow{random.randint(0, 9999):04d}"

def gerar_expiracao():
    return datetime.now() + timedelta(minutes=5)

def criar_user(username, email, senha):

    hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
    codigo = gerar_cod()
    expiracao = gerar_expiracao()

    conexao = conectar()
    cursor = conexao.cursor()

    erros = []

    cursor.execute(
        "SELECT username FROM usuarios WHERE username = ?",
        (username,)
    )

    if cursor.fetchone():
        erros.append("username_em_uso")

    

    cursor.execute(
        "SELECT email FROM usuarios WHERE email = ?",
        (email,)
    )

    if cursor.fetchone():
        erros.append("email_em_uso")

    if erros:
        conexao.close()
        return erros
    
    cursor.execute("""
    INSERT INTO usuarios (username, email, senha_hash, codigo, email_verificado, codigo_expira_em, foto_user)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,(username, email, hash, codigo, 0, expiracao, "user-ft-1.png"))

    conexao.commit()
    conexao.close()

    return["sucesso"]

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
        SELECT codigo, codigo_expira_em
        FROM usuarios
        WHERE email = ? AND codigo = ?
""", (email, codigo))

    cod = cursor.fetchone()

    conexao.close()

    if not cod:
        return False

    expiracao = datetime.fromisoformat(cod[1])

    if datetime.now() > expiracao:
        return False

    return True

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

def atualizar_cod(email):

    conexao = conectar()
    cursor = conexao.cursor()

    codigo = gerar_cod()
    expiracao = gerar_expiracao()

    cursor.execute("""
        UPDATE usuarios
        SET codigo = ?, codigo_expira_em = ?
        WHERE email = ?
""", (codigo, expiracao, email))

    conexao.commit()
    conexao.close()

    return codigo

def reenviar_email(email):

    cod = atualizar_cod(email)

    msg = EmailMessage()
    msg['Subject'] = 'Código de verificação Ronrom'
    msg['From'] = emailenv
    msg['To'] = email
    msg.set_content(f'Olá, este é o email de verificação da Ronrom. Seu código de verificação de email é {cod}, não compartilhe o código de verificação para ninguém!')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(emailenv, senha_app_email)
        smtp.send_message(msg)

def veri_login(email, senha):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT email, senha_hash
    FROM usuarios
    WHERE email = ?
""", (email,))

    usuario = cursor.fetchone()

    conexao.close()

    if not usuario:
        return False

    senha_corr = bcrypt.checkpw(senha.encode("utf-8"), usuario[1])

    return senha_corr