const email = localStorage.getItem("email")
let favoritos = JSON.parse(localStorage.getItem("favoritos")) || []

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

const containergatos = document.getElementById("gatos")
const campopesquisa = document.querySelector(".pesquisa input")

async function carregargatos(pesquisa = ""){

    const resposta = await fetch(
        `http://127.0.0.1:5000/api/gatos?pesquisa=${encodeURIComponent(pesquisa)}`
    )

    const gatos = await resposta.json()

    containergatos.innerHTML = ""

    gatos.forEach(gato => {

        const card = document.createElement("div")
        card.classList.add("gato")

        card.innerHTML = `

        <img src="../assets/exemplos-gatos/${gato.foto}" alt="${gato.nome}" id="gatoimg">

        <div id="info_gato">
            <div id="dados_gato">
                <h3>${gato.nome}</h3>
                <p>${gato.cor}</p>
                <p>${gato.idade_aproximada}</p>
                <p>${gato.sexo}</p>
            </div>

            <button id="favorito_btn">
                <img src="../assets/botao_favoritos.png" id="img_fav">
            </button>
        </div>
        `

        containergatos.appendChild(card)
        card.addEventListener("click", () => {
            localStorage.setItem("gato_id", gato.id)
            window.location.href = "gato.html"
        })

        const fav = card.querySelector("#favorito_btn")
        const img_fav = fav.querySelector("img")

        if (favoritos.includes(gato.id)) {
            img_fav.src = "../assets/fav_ativo.png"
        }

        fav.addEventListener("click", (event) => {
            event.stopPropagation()

            if (favoritos.includes(gato.id)){

                favoritos = favoritos.filter(id => id !== gato.id)

                img_fav.src = "../assets/botao_favoritos.png"
            } else {

                favoritos.push(gato.id)

                img_fav.src = "../assets/fav_ativo.png"
            }

            localStorage.setItem("favoritos", JSON.stringify(favoritos))
        })
    })
}

campopesquisa.addEventListener("input", () => {
    carregargatos(campopesquisa.value)
})

carregargatos()