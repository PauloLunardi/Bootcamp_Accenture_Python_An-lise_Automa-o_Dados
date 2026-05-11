# Lendo os dados

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute("Select * FROM usuarios_vip")

dados = cursor.fetchall()

print(dados)

cursor.close()
conexao.close()

