import threading
from flask import Flask, request
from flask_cors import CORS
from usuarios import criar_user, veri_user_email

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

app.run(debug=True)