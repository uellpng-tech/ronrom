document.getElementById("logout_btn").addEventListener("click", () => {
    localStorage.clear()
    window.location.href = "index.html"
})

function emailmasc(email) {
    const [usuario, dominio] = email.split("@")

    const usuariomasc = usuario[0] + "*".repeat(usuario.length - 2) + usuario[usuario.length - 1]

    return usuariomasc + "@" + dominio
}

const email = localStorage.getItem("email")

document.getElementById("email").textContent = emailmasc(email)

async function buscaruser(){

    const consulta = await fetch("http://127.0.0.1:5000/api/username", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email:email
        })
    })

    const dados = await consulta.json()

    if (!consulta.ok){
        console.log(dados)
        return
    }

    document.getElementById("username").textContent = dados.username
}

buscaruser()