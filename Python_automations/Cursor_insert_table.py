# Inserindo dados em uma tabela
cursor.execute(
  "INSERT INTO  usuarios VALUES (?,?)",
  ("Ana", 25)
)

conm.commit()
print("Usuarios inseridos no banco de dados")

cursor.close()
conm.close()
