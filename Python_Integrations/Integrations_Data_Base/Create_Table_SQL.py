import sqlite3

# criando ou conectando ao banco

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS usuarios_vip (
    nome TEXT,
    idade INTEGER
    )
  """)

conexao.commit()
cursor.close()
conexao.close()
