document.getElementById("confirmar_btn").addEventListener("click", async () => {

    const senha = document.getElementById("senha").value
    const email = localStorage.getItem("email")

    const consulta = await fetch("http://127.0.0.1:5000/api/confirmar_senha", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        email: email,
        senha: senha
        })
    })

    const dados = await consulta.json()

    if (!consulta.ok){
        document.getElementById("status").textContent = `*${dados.mensagem}*`
        console.log(dados)
        return
    }

    if (dados.ok){
        window.location.href = "editarperfil.html"
    } 
})