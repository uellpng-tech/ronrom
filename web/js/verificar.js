function emailmasc(email) {
    const [usuario, dominio] = email.split("@")

    const usuariomasc = usuario[0] + "*".repeat(usuario.length - 2) + usuario[usuario.length - 1]

    return usuariomasc + "@" + dominio
}

const email = localStorage.getItem("email")

document.getElementById("email-masc").textContent = emailmasc(email)