import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
from usuarios import criar_user, veri_user_email, veri_cod, confirmar_email, reenviar_email
from database import conectar

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

@app.route("/api/reenviar-codigo", methods=["POST"])
def reenvio():

    dadosv = request.json
    email = dadosv["email"]

    reenviar_email(email)

    return jsonify({
        "menagem": "Código reenviado com sucesso"
    }), 200


@app.route("/api/expiracao-codigo", methods=["POST"])
def expiracao_codigo():

    dadose = request.get_json()
    email = dadose["email"]

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT codigo_expira_em
        FROM usuarios
        WHERE email = ?
""", (email,))

    expiracao = cursor.fetchone()

    conexao.close()

    if not expiracao:
        return jsonify({"mensagem": "Email não encontrado"}), 404

    return jsonify({
        "expiracao": expiracao[0]
    }), 200

app.run(debug=True)