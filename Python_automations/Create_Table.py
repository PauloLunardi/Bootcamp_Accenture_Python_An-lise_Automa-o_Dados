import sqlite3

# criando ou conectando ao banco

conm = sqlite3.connect("dados.db")
cursor = conmexao.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS new_user (
    nome TEXT,
    idade INTEGER
    )
  """)


conm.commit()
print("Tabela criada com sucesso...")

cursor.close()
conm.close()
