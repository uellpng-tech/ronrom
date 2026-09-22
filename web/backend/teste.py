import sqlite3
import os
import random

pasta = "web/assets/exemplos-gatos"

conexao = sqlite3.connect("web/database/ronrom.db")
cursor = conexao.cursor()

imagens = [
    arquivo for arquivo in os.listdir(pasta)
    if arquivo.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
]

nomes = [
    "Mingau", "Nina", "Luna", "Tom", "Mel",
    "Simba", "Nala", "Pipoca", "Chico", "Mimi"
]

for i, imagem in enumerate(imagens):
    cursor.execute("""
        INSERT INTO gatos (
            nome,
            idade_aproximada,
            sexo,
            peso,
            castrado,
            vacinado,
            vermifugado,
            fiv,
            felv,
            deficiente,
            comportamento,
            historico_resgate,
            foto,
            usuario_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        random.choice(nomes),
        f"{random.randint(1, 8)} anos",
        random.choice(["Macho", "Fêmea"]),
        round(random.uniform(2.5, 6.5), 1),
        random.randint(0, 1),
        random.randint(0, 1),
        random.randint(0, 1),
        0,
        0,
        0,
        "Brincalhão",
        "Resgatado",
        imagem,
        1
    ))

conexao.commit()
conexao.close()

print(f"{len(imagens)} gatos inseridos!")