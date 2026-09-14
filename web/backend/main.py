import threading
from flask import Flask, request
from flask_cors import CORS
from usuarios import criar_user, veri_user_email, veri_cod, confirmar_email

app = Flask(__name__)
CORS(app)

@app.route("/api/cadastro", methods=["POST"])
def cadastro():

    dados = request.json

    username = dados["username"]
    email = dados["email"]
    senha = dados["senha"]

    criar_user(username, email, senha)

    threading.Thread(target=veri_user_email, args=(email,), daemon=True).start()

    return {"mensagem": "usuário criado"}, 201

@app.route("/api/verificar-email", methods=["POST"])
def veri_codf():

    dadosc = request.json

    codigo = dadosc["codigo"]
    email = dadosc["email"]

    correto = veri_cod(email, codigo)

    if correto:
        confirmar_email(email)
        return {"mensagem": "código correto"}, 200

    return {"mensagem": "código incorreto"}, 400

app.run(debug=True)