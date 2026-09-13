from flask import Flask, request
from flask_cors import CORS
from usuarios import criar_user

app = Flask(__name__)
CORS(app)

@app.route("/api/cadastro", methods=["POST"])
def cadastro():

    dados = request.json

    username = dados["username"]
    email = dados["email"]
    senha = dados["senha"]

    criar_user(username, email, senha)

    return {"mensagem": "usuário criado"}, 201

app.run(debug=True)