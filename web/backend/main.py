import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
from usuarios import criar_user, veri_user_email, veri_cod, confirmar_email, reenviar_email, veri_login
from userconfig import editar_user, confirmar_senha_user, resetar_senha, alterar_senha_es
from database import conectar

app = Flask(__name__)
CORS(app)

@app.route("/api/cadastro", methods=["POST"])
def cadastro():

    dados = request.json

    username = dados["username"]
    email = dados["email"]
    senha = dados["senha"]

    resultadoc = criar_user(username, email, senha)

    if resultadoc != ["sucesso"]:
        return{"status": resultadoc}, 409

    threading.Thread(target=veri_user_email, args=(email,), daemon=True).start()

    return {"status": ["sucesso"]}, 201

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

@app.route("/api/consulta_login", methods=["POST"])
def login():

    dados = request.json

    email = dados["email"]
    senha = dados["senha"]

    ver = veri_login(email, senha)

    if ver:
        return {"ok": True}, 200

    return {"ok": False, "mensagem": "email ou senha inválidos"}, 401

@app.route("/api/username", methods=["POST"])
def consulta_username():

    dados = request.get_json()

    email = dados["email"]

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT username FROM usuarios WHERE email = ?",
        (email,)
    )

    usuario = cursor.fetchone()

    conexao.close()

    if not usuario:
        return jsonify({
            "ok": False,
            "mensagem": "usuário não encontrado"
        }), 404

    return jsonify({
        "ok": True,
        "username": usuario[0]
    }), 200

@app.route("/api/foto_usuario", methods=["POST"])
def foto_consulta():

    dados = request.get_json()

    email = dados.get("email")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT foto_user
    FROM usuarios
    WHERE email = ?
""", (email,))

    usuario = cursor.fetchone()

    conexao.close()

    if usuario is None:
        return jsonify({"erro": "usuario_nao_encontrado"}), 404

    return jsonify({
        "foto_user": usuario[0]
    }), 200

@app.route("/api/editar_perfil", methods=["POST"])
def editar_perfil():

    dados = request.get_json()

    email_atual = dados.get("email_atual")
    username = dados.get("username")
    email = dados.get("email")
    senha = dados.get("senha")
    foto_user = dados.get("foto_user")

    resultado = editar_user(username, email, senha, foto_user, email_atual)

    if not resultado:
        return jsonify({
            "ok": False,
            "mensagem": "Usuário não encontrado"
        }), 404

    if resultado == "usuario_ou_email_inexistente":
        return jsonify({
            "ok": False,
            "mesangem": "username ou email já cadastrado"
        }), 409

    return jsonify({
        "ok": True,
        "username": resultado["username"],
        "email": resultado["email"],
        "foto_user": resultado["foto_user"],
        "mensagem": "Perfil atualizado com sucesso"
    }), 200

@app.route("/api/confirmar_senha", methods=["POST"])
def confirmar_senha():

    dados = request.get_json()

    email = dados.get("email")
    senha = dados.get("senha")

    resultado = confirmar_senha_user(email, senha)

    if resultado:
        return jsonify({
            "ok": True
        }), 200

    return jsonify({
        "ok": False,
        "mensagem": "senha incorreta"
    }), 401


@app.route("/api/resetar_senha", methods=["POST"])
def reset_senha():

    dados = request.get_json()

    email = dados.get("email")
    senha = dados.get("senha")
    senha_nova = dados.get("senha_nova")

    resultado = resetar_senha(email, senha, senha_nova)

    if resultado == "senha_incorreta":
        return jsonify({
            "ok": False,
            "mensagem": "senha atual incorreta"
        }), 401

    if not resultado:
        return jsonify({
            "ok": False,
            "mensagem": "usuário não encontrado"
        }), 404

    return jsonify({
        "ok": True,
        "mensagem": "senha alterada com sucesso"
    }), 200

@app.route("/api/alterar_senha_reset", methods=["POST"])
def esqueci_senha():

    dados = request.get_json()

    email = dados.get("email")
    senha = dados.get("senha")

    resultado = alterar_senha_es(email, senha)

    if not resultado:
        return jsonify({
            "mensagem": "usuário não encontrado"
        }), 404

    return jsonify({
        "ok": True,
        "mensagem": "usuário alterado com sucesso"
    }), 200

@app.route("/api/gatos", methods=["GET"])
def listar_gatos():

    pesquisa = request.args.get("pesquisa", "")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, cor, idade_aproximada, sexo, foto
        FROM gatos
        WHERE nome LIKE ?
        OR cor LIKE ?
        OR idade_aproximada LIKE ?
        OR sexo LIKE ?
""", (
    f"%{pesquisa}%",
    f"%{pesquisa}%",
    f"%{pesquisa}%",
    f"%{pesquisa}%"
))

    gatos = cursor.fetchall()

    conexao.close()

    lista_gatos = []

    for gato in gatos:
        lista_gatos.append({
            "id": gato[0],
            "nome": gato[1],
            "cor": gato[2],
            "idade_aproximada": gato[3],
            "sexo": gato[4],
            "foto": gato[5]
        })

    return jsonify(lista_gatos)
    
app.run(debug=True)