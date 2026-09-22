document.getElementById("confirmar_btn").addEventListener("click", async () => {

    const senha = document.getElementById("senha_nova").value 
    const senhaconf = document.getElementById("senha_novac").value
    const status = document.getElementById("status")
    const email = localStorage.getItem("email")

    if (senha !== senhaconf){
        status.textContent = "*as senhas não coincidem*"
        return
    }

    if (senha === ""){
        status.textContent = "*digite uma senha*"
        return
    }

    const resposta = await fetch("http://127.0.0.1:5000/api/alterar_senha_reset", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            senha: senha
        })
    })

    const dados = await resposta.json()

    if (!resposta.ok){
        status.textContent = `*${dados.mensagem}*`
        return
    }

    window.location.href = "userconfig.html"
})