import sqlite3

conexao = sqlite3.connect("web/database/ronrom.db")
cursor = conexao.cursor()

gatos = [
    ("Mingau", "Laranja", "2 anos", "Macho", 4.2, 1, 1, 1, 0, 0, 0, "Dócil e brincalhão", "Resgatado de uma praça."),
    ("Luna", "Branca e Cinza", "1 ano", "Fêmea", 3.5, 1, 1, 1, 0, 0, 0, "Carinhosa e tranquila", "Encontrada próxima a uma residência."),
    ("Thor", "Tigrado", "3 anos", "Macho", 5.1, 1, 1, 1, 0, 0, 0, "Brincalhão e energético", "Resgatado ainda filhote."),
    ("Mel", "Rosa", "2 anos", "Fêmea", 3.8, 0, 1, 1, 0, 0, 0, "Calma e carinhosa", "Resgatada após ser encontrada sozinha."),
    ("Nino", "Preto", "1 ano", "Macho", 3.2, 0, 1, 1, 0, 0, 0, "Tímido, mas amigável", "Encontrado próximo a um abrigo."),
    ("Amora", "Laranja e Branca", "2 anos", "Fêmea", 4.0, 1, 1, 1, 0, 0, 0, "Dócil e sociável", "Resgatada de uma situação de abandono."),
    ("Simba", "Cinza e Branco", "1 ano", "Macho", 3.6, 1, 1, 1, 0, 0, 0, "Curioso e brincalhão", "Encontrado em uma área residencial."),
    ("Nala", "Tigrado", "2 anos", "Fêmea", 4.1, 1, 1, 1, 0, 0, 0, "Tranquila e carinhosa", "Resgatada junto de outros gatos."),
    ("Tom", "Tigrado e Branco", "3 meses", "Macho", 1.8, 0, 1, 1, 0, 0, 0, "Muito brincalhão", "Encontrado sozinho em uma caixa."),
    ("Mia", "Branca e Cinza", "1 ano", "Fêmea", 3.4, 1, 1, 1, 0, 0, 0, "Carinhosa e curiosa", "Resgatada de uma residência abandonada."),
    ("Bidu", "Preto e Branco", "5 anos", "Macho", 5.3, 1, 1, 1, 0, 0, 0, "Calmo e companheiro", "Resgatado das ruas."),
    ("Frida", "Tigrado", "2 anos", "Fêmea", 4.0, 1, 1, 1, 0, 0, 0, "Independente e tranquila", "Encontrada próxima a um parque."),
    ("Romeu", "Siamês", "1 ano", "Macho", 3.7, 0, 1, 1, 0, 0, 0, "Carinhoso e comunicativo", "Resgatado após ser encontrado sozinho."),
    ("Jade", "Laranja", "3 anos", "Fêmea", 4.5, 1, 1, 1, 0, 0, 0, "Dócil e brincalhona", "Resgatada de uma área residencial."),
    ("Oliver", "Tigrado", "4 anos", "Macho", 5.0, 1, 1, 1, 0, 0, 0, "Tranquilo e sociável", "Encontrado próximo a um comércio."),
    ("Lola", "Preta", "2 anos", "Fêmea", 3.9, 1, 1, 1, 0, 0, 0, "Carinhosa e tranquila", "Resgatada após abandono."),
    ("Theo", "Tigrado", "1 ano", "Macho", 3.5, 0, 1, 1, 0, 0, 0, "Energético e brincalhão", "Encontrado em uma praça."),
    ("Melody", "Preta e Branca", "3 anos", "Fêmea", 4.3, 1, 1, 1, 0, 0, 0, "Dócil e carinhosa", "Resgatada de uma colônia de gatos."),
    ("Toby", "Caramelo e Branco", "2 anos", "Macho", 4.4, 1, 1, 1, 0, 0, 0, "Brincalhão e amigável", "Encontrado próximo a uma escola."),
    ("Belinha", "Tricolor", "1 ano", "Fêmea", 3.3, 0, 1, 1, 0, 0, 0, "Meiga e tranquila", "Resgatada de uma situação de abandono."),
    ("Fred", "Preto", "4 anos", "Macho", 5.2, 1, 1, 1, 0, 0, 0, "Calmo e dócil", "Encontrado próximo a um estacionamento."),
    ("Nina", "Tricolor", "6 meses", "Fêmea", 2.5, 0, 1, 1, 0, 0, 0, "Brincalhona e curiosa", "Resgatada junto de sua ninhada."),
    ("Bento", "Branco e Preto", "2 anos", "Macho", 4.6, 1, 1, 1, 0, 0, 0, "Sociável e carinhoso", "Encontrado em uma residência abandonada."),
    ("Lili", "Laranja", "3 anos", "Fêmea", 4.1, 1, 1, 1, 0, 0, 0, "Tranquila e independente", "Resgatada de uma praça."),
    ("Zeca", "Cinza", "5 anos", "Macho", 5.7, 1, 1, 1, 0, 0, 0, "Calmo e companheiro", "Resgatado das ruas."),
    ("Cacau", "Branca e Cinza", "2 anos", "Fêmea", 3.9, 1, 1, 1, 0, 0, 0, "Carinhosa e brincalhona", "Encontrada próxima a uma residência."),
    ("Pipoca", "Branca e Preta", "1 ano", "Fêmea", 3.2, 0, 1, 1, 0, 0, 0, "Muito ativa e brincalhona", "Resgatada de uma área abandonada."),
    ("Chico", "Cinza", "3 anos", "Macho", 4.8, 1, 1, 1, 0, 0, 0, "Dócil e tranquilo", "Encontrado próximo a um mercado."),
    ("Fiona", "Preta e Branca", "2 anos", "Fêmea", 3.7, 1, 1, 1, 0, 0, 0, "Meiga e sociável", "Resgatada após ser encontrada sozinha."),
    ("Luke", "Preto", "3 meses", "Macho", 1.7, 0, 1, 1, 0, 0, 0, "Curioso e brincalhão", "Encontrado em uma caixa de papelão."),
    ("Sofia", "Branca e Cinza", "1 ano", "Fêmea", 3.6, 1, 1, 1, 0, 0, 0, "Carinhosa e calma", "Resgatada de uma residência abandonada."),
    ("Max", "Cinza", "2 anos", "Macho", 4.5, 1, 1, 1, 0, 0, 0, "Energético e brincalhão", "Encontrado próximo a um parque."),
    ("Maya", "Caramelo e Cinza", "3 anos", "Fêmea", 4.2, 1, 1, 1, 0, 0, 0, "Dócil e tranquila", "Resgatada das ruas."),
    ("Cookie", "Tricolor", "1 ano", "Macho", 3.4, 0, 1, 1, 0, 0, 0, "Brincalhão e sociável", "Encontrado próximo a uma escola."),
    ("Aurora", "Branca e Cinza", "2 anos", "Fêmea", 3.8, 1, 1, 1, 0, 0, 0, "Carinhosa e tranquila", "Resgatada junto de outros gatos."),
    ("Bruce", "Preto", "4 anos", "Macho", 5.5, 1, 1, 1, 0, 0, 0, "Calmo e protetor", "Encontrado próximo a um abrigo."),
    ("Cleo", "Branca", "6 meses", "Fêmea", 2.4, 0, 1, 1, 0, 0, 0, "Brincalhona e curiosa", "Resgatada junto de sua ninhada."),
    ("Boris", "Branco", "3 anos", "Macho", 4.9, 1, 1, 1, 0, 0, 0, "Dócil e amigável", "Encontrado próximo a uma residência."),
    ("Liz", "Branca e Cinza", "2 anos", "Fêmea", 3.9, 1, 1, 1, 0, 0, 0, "Carinhosa e sociável", "Resgatada após abandono."),
    ("Oscar", "Tricolor", "5 anos", "Macho", 5.4, 1, 1, 1, 0, 0, 0, "Tranquilo e companheiro", "Resgatado das ruas."),
    ("Malu", "Branca", "1 ano", "Fêmea", 3.1, 0, 1, 1, 0, 0, 0, "Meiga e brincalhona", "Encontrada próxima a um parque."),
    ("Pingo", "Preto", "2 anos", "Macho", 4.0, 1, 1, 1, 0, 0, 0, "Ativo e curioso", "Resgatado de uma situação de abandono."),
    ("Kira", "Siamês", "3 anos", "Fêmea", 4.3, 1, 1, 1, 0, 0, 0, "Carinhosa e comunicativa", "Encontrada próxima a uma residência."),
    ("Paco", "Laranja e Branco", "4 anos", "Macho", 5.0, 1, 1, 1, 0, 0, 0, "Dócil e brincalhão", "Resgatado de uma praça."),
    ("Estrela", "Laranja", "1 ano", "Fêmea", 3.5, 0, 1, 1, 0, 0, 0, "Curiosa e carinhosa", "Encontrada próxima a um comércio."),
    ("Billy", "Branco e Preto", "2 anos", "Macho", 4.2, 1, 1, 1, 0, 0, 0, "Sociável e energético", "Resgatado junto de outros gatos."),
    ("Meg", "Laranja", "3 anos", "Fêmea", 4.4, 1, 1, 1, 0, 0, 0, "Tranquila e carinhosa", "Encontrada em uma área residencial."),
    ("Felix", "Laranja", "5 anos", "Macho", 5.6, 1, 1, 1, 0, 0, 0, "Calmo e companheiro", "Resgatado das ruas."),
    ("Luma", "Branca", "2 anos", "Fêmea", 3.7, 1, 1, 1, 0, 0, 0, "Dócil e tranquila", "Resgatada de uma situação de abandono."),
    ("Mochi", "Preto", "1 ano", "Macho", 3.3, 0, 1, 1, 0, 0, 0, "Brincalhão e curioso", "Encontrado próximo a uma residência.")
]

for i, gato in enumerate(gatos, start=1):

    (
        nome,
        cor,
        idade,
        sexo,
        peso,
        castrado,
        vacinado,
        vermifugado,
        fiv,
        felv,
        deficiente,
        comportamento,
        historico_resgate
    ) = gato

    cursor.execute("""
        INSERT INTO gatos (
            nome,
            cor,
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        nome,
        cor,
        idade,
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
        f"gato{i}.jpg",
        1
    ))

conexao.commit()
conexao.close()
