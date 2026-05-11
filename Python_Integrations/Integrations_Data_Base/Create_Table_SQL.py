import sqlite3

# criando ou conectando ao banco

conexao = sqlite3.connect("dados.db")

cursos = conexao.cursor()

cursos.execute("""
  CREATE TABLE usuarios_vip (
    nome TEXT,
    idade INTEGER
    )
  """)

conexao.commit


