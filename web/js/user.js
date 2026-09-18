document.getElementById("entrar_btn").addEventListener("click", async () => {

    const status = document.getElementById("status")
    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value
    
    const consulta = await fetch("http://127.0.0.1:5000/api/consulta_login", {

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

    if(dados.ok){
        console.log(dados)
        localStorage.setItem("logado", "true")
        window.location.href = "index.html"
    } else{
        status.textContent = `*${dados.mensagem}*`
    }
})
