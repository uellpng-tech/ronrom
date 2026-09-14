function emailmasc(email) {
    const [usuario, dominio] = email.split("@")

    const usuariomasc = usuario[0] + "*".repeat(usuario.length - 2) + usuario[usuario.length - 1]

    return usuariomasc + "@" + dominio
}

const email = localStorage.getItem("email")

document.getElementById("email-masc").textContent = emailmasc(email)

document.getElementById("confirmar_btn").addEventListener("click", async () => {

    const codigo = document.getElementById("codigo").value
    const email = localStorage.getItem("email")
    
    const verificacao = await fetch("http://127.0.0.1:5000/api/verificar-email", {

        method: "POST", 
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            codigo: codigo
        })
    }) 

    const dadosc = await verificacao.json()

    console.log(dadosc)

    if (verificacao.ok){
        console.log(dadosc.mensagem)
        window.location.href = "index.html"
    } else {
        console.log(dadosc.mensagem)
    }
})