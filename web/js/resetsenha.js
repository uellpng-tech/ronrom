const senha = document.getElementById("senha")
const senhanova = document.getElementById("senha_nova")
const senhanovac = document.getElementById("senha_novac")

document.getElementById("confirmar_btn").addEventListener("click", async () => {

    const status = document.getElementById("status")
    const senhaatual = senha.value
    const senhanova = senhanova.value
    const confirmarsenha = senhanovac.value

    if (!senhaatual || !senhanova || !confirmarsenha){
        status.textContent = "*preencha todos os campos*"
        return
    }

    if (senhanova !== confirmarsenha){
        status.textContent = "*as senhas novas não coincidem*"
        return
    }

    const email = localStorage.getItem("email")

    

})