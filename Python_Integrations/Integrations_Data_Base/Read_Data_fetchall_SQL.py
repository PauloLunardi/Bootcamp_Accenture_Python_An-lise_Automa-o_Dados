# Leitura com fetchall()
# Lendo todos os resultados de uma vez
import sqlite3

conexao = sqlite3.connect("dados.db")

cursor = conexao.cursor()

cursor.execute("Select * FROM usuarios_vip")

# retorna uma lista com todas as linhas(em Tuplas)
dados = cursor.fetchall()

print(dados)

cursor.close()
conexao.close()
