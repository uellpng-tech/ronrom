const senha = document.getElementById("senha")
const novasenha = document.getElementById("senha_nova")
const senhanovac = document.getElementById("senha_novac")

document.getElementById("confirmar_btn").addEventListener("click", async () => {

    const status = document.getElementById("status")
    const senhaatual = senha.value
    const senhanova = novasenha.value
    const confirmarsenha = senhanovac.value

    if (!senhaatual || !senhanova || !confirmarsenha){
        status.textContent = "*preencha todos os campos*"
        return
    }

    if (senhanova !== confirmarsenha){
        status.textContent = "*as senhas novas não coincidem*"
        return
    }

    const email = localStorage.getItem("email")

    const reset = await fetch("http://127.0.0.1:5000/api/resetar_senha", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            senha: senhaatual,
            senha_nova: senhanova
        })
    })

    const dados = await reset.json()

    if (!reset.ok){
        status.textContent = `*${dados.mensagem}*`
        return
    }

    window.location.href = "userconfig.html"
})