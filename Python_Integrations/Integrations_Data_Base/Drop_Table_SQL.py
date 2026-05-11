import sqlite3

# Dropando tabela do banco

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute("""
  DROP TABLE IF EXISTS usuarios_vip
  """)

conexao.commit()
cursor.close()
conexao.close()
