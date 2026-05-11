# Inserindo os dados no banco

import sqlite3

conexao = sqlite3.connect("dados.db")

cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO usuarios_vip VALUES (?, ?)",
    ("Lunardi", 37)
)

conexao.commit()
cursor.close()
conexao.close()
