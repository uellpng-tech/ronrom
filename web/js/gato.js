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

function criar_caixa(elemento, titulo, valor){
    const verdadeiro = valor === 1 || valor === true;

    elemento.classList.add("caixa");
    elemento.innerHTML = `
        <span class="caixa-titulo">${titulo}</span>
        <span class="caixa-valor">${verdadeiro ? "Sim" : "Não"}</span>
    `
}

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
    criar_caixa(castrado, "Castrado", dados.castrado)
    criar_caixa(vacinado, "Vacinado", dados.vacinado)
    criar_caixa(vermifulgado, "Vermifugado", dados.vermifulgado)
    criar_caixa(fiv, "FIV", dados.fiv)
    criar_caixa(felv, "FeLV", dados.felv)
    criar_caixa(deficiente, "Deficiente", dados.deficiente) 
    comportamento.textContent = dados.comportamento
    historico.textContent = dados.historico_resgate
    gato_foto = dados.foto
    fotoga = document.getElementById("fotog")
    fotoga.src = `../assets/exemplos-gatos/${gato_foto}`
}

carregarinfo()