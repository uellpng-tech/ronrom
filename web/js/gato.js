const email = location.getItem("email")

async function carregarinfo(){
    const consulta = await fetch('http://127.0.0.1/5000/api/gatos_info', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({email:email})
    })

    const dados = await consulta.json()

    
}