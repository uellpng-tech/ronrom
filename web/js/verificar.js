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

let timer = null

function iniciartimer(){

    if (timer !== null) {
        return
    }

    let tempo = 60

    reenv_btn.disabled = true

    timer = setInterval(() => {
        
        tempo--

        reenv_btn.textContent = `Reenviar código (${tempo}s)`

        if (tempo <= 0) {
            clearInterval(timer)
            timer = null

            reenv_btn.disabled = false
            reenv_btn.textContent = "Reenviar código"
        }

    }, 1000)
}

const reenv_btn = document.getElementById("reenv_btn")

reenv_btn.addEventListener("click", async () => {

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

    iniciartimer()
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

    document.getElementById("tempo-expiracao").textContent = `Um código de verificação foi enviado para o email a cima, verifique o código e insira na caixa de texto abaixo para verificação do seu email. O código de verificação expira em (${restante}s).`

    if (restante <= 0){

        clearInterval(timeexpiracao)

        document.getElementById("tempo-expiracao").textContent = "o código expirou"

        document.getElementById("codigo").disabled = true
        document.getElementById("confirmar_btn").disabled = true
    }

}, 1000)

}

iniciarexpiracao()
iniciartimer()