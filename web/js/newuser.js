function dominio_email_valido(email){

    const dominio_per = [
        "gmail.com",
        "outlook.com",
        "hotmail.com",
        "yahoo.com",
        "live.com",
        "uol.com.br"
    ]

    const part = email.toLowerCase().split("@")

   if (part.length !== 2 || part[0] === ""){
        return false
    }
    return dominio_per.includes(part[1])
}

document.getElementById("criar_btn").addEventListener("click", async () => {

    const username = document.getElementById("username").value
    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value
    const status = document.getElementById("status")

    const erros = []

    if (!dominio_email_valido(email)){
        erros.push("email inválido")
    }

    if (erros.length > 0){
        status.textContent = "*" + erros.join("|") + "*"
        return
    }

    const resposta = await fetch("http://127.0.0.1:5000/api/cadastro", {
        
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            email: email,
            senha: senha
        })
    })

    const dados = await resposta.json()

    console.log(dados)

    if (dados.status.includes("username_em_uso")){
        erros.push("Username em uso")
    }

    if (dados.status.includes("email_em_uso")){
        erros.push("Email em uso")
    }

    if (erros.length > 0){
        status.textContent = "*" + erros.join("|") + "*"
        return
    }

    if (dados.status.includes("sucesso")) {
    localStorage.setItem("email", email)

    const fim = Date.now() + 60 * 1000
    localStorage.setItem("reenviar_fim", fim)

    window.location.href = "verificar.html"}
})
