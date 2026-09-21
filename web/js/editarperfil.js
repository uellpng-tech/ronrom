const fotos = document.querySelectorAll("#fotos img")
const fotoatual = localStorage.getItem("foto_user")
let fotoselec = localStorage.getItem("foto_user")

fotos.forEach(foto => {
    const nomefoto = foto.src.split("/").pop()

    if (nomefoto === fotoatual){
        foto.classList.add("selecionada")
    }

    foto.addEventListener("click", () => {

        fotos.forEach(f => {
            f.classList.remove("selecionada")
        })

        foto.classList.add("selecionada")
        fotoselec = foto.dataset.foto
    })
})

document.getElementById("salvar").addEventListener("click", async () => {

    const username = document.getElementById("username_input").value
    const email = document.getElementById("email_input").value
    const senha = document.getElementById("senha_input").value

    const consulta = await fetch("http://127.0.0.1:5000/api/editar_perfil", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email_atual: localStorage.getItem("email"),
            username: username,
            email: email,
            senha: senha,
            foto_user: fotoselec
        })
    })

    const dados = await consulta.json()

    console.log(dados)

    if (dados.ok){
        localStorage.setItem("email", dados.email)
        localStorage.setItem("foto_user", fotoselec)
        window.location.href = "userconfig.html"
    }
    if (consulta.status === 409){
        console.log(dados.mensagem)
        document.getElementById("status").textContent = "*username ou email já cadastrado*"
        return
    }
})