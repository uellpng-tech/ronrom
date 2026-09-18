const perfil = document.getElementById("conta_btn")

if (localStorage.getItem("logado") === "true"){
    perfil.href = "userconfig.html"
} else{
    perfil.href = "user.html"
}