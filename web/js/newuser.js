document.getElementById("criar_btn").addEventListener("click", async () => {

    const username = document.getElementById("username").value
    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value

    localStorage.setItem("email", email)

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

    if (resposta.ok) {
        window.location.href = "verificar.html"
    }
})