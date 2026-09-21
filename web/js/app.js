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

    const foto = perfil.querySelector("img")
    foto.src = `../assets/${dados.foto_user}`
}

const perfil = document.getElementById("conta_btn")
const foto = perfil.querySelector("img");

if (localStorage.getItem("logado") === "true"){
    perfil.href = "userconfig.html"
    fotouser()
} else{
    perfil.href = "user.html"
    foto.src = "../assets/conta_default.png";
}