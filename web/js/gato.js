const gato_id = localStorage.getItem("gato_id")
const nome = document.getElementById("nome")
const idade = document.getElementById("idade")
const sexo = document.getElementById("sexo")
const cor = document.getElementById("cor")
const peso = document.getElementById("peso")
const castrado = document.getElementById("castrado")
const vacinado = document.getElementById("vacinado")
const vermifulgado = document.getElementById("vermifulgado")
const fiv = document.getElementById("fiv")
const felv = document.getElementById("felv")
const deficiente = document.getElementById("deficiente")
const comportamento = document.getElementById("comportamento")
const historico = document.getElementById("historico")

async function carregarinfo(){
    const consulta = await fetch('http://127.0.0.1:5000/api/gatos_info', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({gato_id: gato_id})
    })

    const dados = await consulta.json()

    console.log(dados)

    nome.textContent = dados.nome
    idade.textContent = dados.idade_aproximada
    sexo.textContent = dados.sexo
    cor.textContent = dados.cor
    peso.textContent = dados.peso
    castrado.textContent = dados.castrado
    vacinado.textContent = dados.vacinado
    vermifulgado.textContent = dados.vermifulgado
    fiv.textContent = dados.fiv
    felv.textContent = dados.felv
    deficiente.textContent = dados.deficiente
    comportamento.textContent = dados.comportamento
    historico.textContent = dados.historico_resgate 
}

carregarinfo()