const perfil = document.getElementById("conta_btn")

if (localStorage.getItem("logado") === "true"){
    perfil.href = "userconfig.html"
} else{
    perfil.href = "user.html"
}

const email = localStorage.getItem("email")

async function fotouser(){
    const consulta = await fetch("http://127.0.0.1:5000/api/foto_usuario", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({email:email})
    })

    const dados = await consulta.json()

    localStorage.setItem("foto_user", dados.foto_user)
}