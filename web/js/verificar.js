function emailmasc(email) {
    const [usuario, dominio] = email.split("@")

    const usuariomasc = usuario[0] + "*".repeat(usuario.length - 2) + usuario[usuario.length - 1]

    return usuariomasc + "@" + dominio
}

const email = localStorage.getItem("email")

document.getElementById("email-masc").textContent = emailmasc(email)

const errocod = document.getElementById("errocod")

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

    const status = document.getElementById("status")

    if (verificacao.ok){
        console.log(dadosc.mensagem)
        localStorage.setItem("email", email)
        localStorage.setItem("logado", "true")
        window.location.href = "index.html"
    } else {
        console.log(dadosc.mensagem)
        status.textContent = `*${dadosc.mensagem}*`
    }

})

function iniciartimer(){

    const fim = Date.now() + 60 * 1000

    localStorage.setItem("reenviar_fim", fim)

    atualizartimer()
}

function atualizartimer(){

    const botao = document.getElementById("reenv_btn")
    const fim = Number(localStorage.getItem("reenviar_fim"))

    if (!fim) {
        botao.disabled = false
        botao.textContent = "Reenviar código"
        return
    }

    const restante = fim - Date.now()

    if (restante <= 0){
        localStorage.removeItem("reenviar_fim")

        botao.disabled = false
        botao.textContent = "Reenviar código"

        return
    }

    const segundos = Math.ceil(restante / 1000)

    botao.disabled = true
    botao.textContent = `Reenviar código (${segundos}s)`


    setTimeout(atualizartimer, 1000)
}

const reenv_btn = document.getElementById("reenv_btn")

reenv_btn.addEventListener("click", async () => {

    iniciartimer()

    const reenvio = await fetch("http://127.0.0.1:5000/api/reenviar-codigo", {

        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email
        })
    })

    const dadosv = await reenvio.json()

    if (!reenvio.ok) {
        console.log(dadosv)
        return
    }

}) 

async function iniciarexpiracao() {

    const expiracaor = await fetch("http://127.0.0.1:5000/api/expiracao-codigo", {

        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email
        })
    })

    const dadose = await expiracaor.json()

    if (!expiracaor.ok){
        console.log(dadose)
        return
    }

    const expiracao = new Date(dadose.expiracao).getTime()

    const timeexpiracao = setInterval(() => {  
        
    const agora = new Date().getTime()
    const restante = Math.floor((expiracao - agora) / 1000)

    document.getElementById("tempo-expiracao").textContent = `Um código de verificação foi enviado para o email a cima, verifique o código e insira na caixa de texto abaixo para verificação do seu email. O código de verificação expira em ${restante}s.`

    if (restante <= 0){

        clearInterval(timeexpiracao)

        document.getElementById("status").textContent = "*O código expirou*"
        document.getElementById("codigo").disabled = true
        document.getElementById("confirmar_btn").disabled = true

        errocod.textContent = ""
    }

}, 1000)

}

iniciarexpiracao()
atualizartimer()