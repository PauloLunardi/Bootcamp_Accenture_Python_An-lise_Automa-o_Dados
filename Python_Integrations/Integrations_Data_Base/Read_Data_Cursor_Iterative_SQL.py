# Leitura iterativa no cursor
# Lendo linha por linha diretamente do cursor
import sqlite3

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios_vip")
for linha in cursor:
    print(linha)

cursor.close()
conexao.close()
