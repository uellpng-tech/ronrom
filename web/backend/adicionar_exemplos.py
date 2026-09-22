import sqlite3

conexao = sqlite3.connect("web/database/ronrom.db")
cursor = conexao.cursor()

gatos = [
    ("Mingau", "Laranja", "2 anos", "Macho"),
    ("Luna", "Branca e Cinza", "1 ano", "Fêmea"),
    ("Thor", "Tigrado", "3 anos", "Macho"),
    ("Mel", "Rosa", "2 anos", "Fêmea"),
    ("Nino", "Preto", "1 anos", "Macho"),
    ("Amora", "Laranja e Branca", "2 anos", "Fêmea"),
    ("Simba", "Cinza e Branco", "1 ano", "Macho"),
    ("Nala", "Tigrado", "2 anos", "Fêmea"),
    ("Tom", "Tigrado e Branco", "3 meses", "Macho"),
    ("Mia", "Branca e Cinza", "1 ano", "Fêmea"),
    ("Bidu", "Preto e Branco", "5 anos", "Macho"),
    ("Frida", "Tigrado", "2 anos", "Fêmea"),
    ("Romeu", "Siamês", "1 ano", "Macho"),
    ("Jade", "Laranja", "3 anos", "Fêmea"),
    ("Oliver", "Tigrado", "4 anos", "Macho"),
    ("Lola", "Preta", "2 anos", "Fêmea"),
    ("Theo", "Tigrado", "1 ano", "Macho"),
    ("Melody", "Preta e Branca", "3 anos", "Fêmea"),
    ("Toby", "Caramelo e Branco", "2 anos", "Macho"),
    ("Belinha", "Tricolor", "1 ano", "Fêmea"),
    ("Fred", "Preto", "4 anos", "Macho"),
    ("Nina", "Tricolor", "6 meses", "Fêmea"),
    ("Bento", "Branco e Preto", "2 anos", "Macho"),
    ("Lili", "Laranja", "3 anos", "Fêmea"),
    ("Zeca", "Cinza", "5 anos", "Macho"),
    ("Cacau", "Branca e Cinza", "2 anos", "Fêmea"),
    ("Pipoca", "Branca e Preta", "1 ano", "Fêmea"),
    ("Chico", "Cinza", "3 anos", "Macho"),
    ("Fiona", "Preta e Branca", "2 anos", "Fêmea"),
    ("Luke", "Preto", "3 meses", "Macho"),
    ("Sofia", "Branca e Cinza", "1 ano", "Fêmea"),
    ("Max", "Cinza", "2 anos", "Macho"),
    ("Maya", "Caramelo e Cinza", "3 anos", "Fêmea"),
    ("Cookie", "Tricolor", "1 ano", "Macho"),
    ("Aurora", "Branca e Cinza", "2 anos", "Fêmea"),
    ("Bruce", "Preto", "4 anos", "Macho"),
    ("Cleo", "Branca", "6 meses", "Fêmea"),
    ("Boris", "Branco", "3 anos", "Macho"),
    ("Liz", "Branca e Cinza", "2 anos", "Fêmea"),
    ("Oscar", "Tricolor", "5 anos", "Macho"),
    ("Malu", "Branca", "1 ano", "Fêmea"),
    ("Pingo", "Preto", "2 anos", "Macho"),
    ("Kira", "Siamês", "3 anos", "Fêmea"),
    ("Paco", "Laranja e Branco", "4 anos", "Macho"),
    ("Estrela", "Laranja", "1 ano", "Fêmea"),
    ("Billy", "Branco e Preto", "2 anos", "Macho"),
    ("Meg", "Laranja", "3 anos", "Fêmea"),
    ("Felix", "Laranja", "5 anos", "Macho"),
    ("Luma", "Branca", "2 anos", "Fêmea"),
    ("Mochi", "Preto", "1 ano", "Macho"),
]

for i, gato in enumerate(gatos, start=1):

    nome, cor, idade, sexo = gato

    cursor.execute("""
        INSERT INTO gatos (
            nome,
            cor,
            idade_aproximada,
            sexo,
            foto,
            usuario_id
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nome,
        cor,
        idade,
        sexo,
        f"gato{i}.jpg",
        1
    ))

conexao.commit()
conexao.close()