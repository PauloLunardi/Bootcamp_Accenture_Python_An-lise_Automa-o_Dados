# Criando arquivo CSV
import csv

dados = [
  ["nome", "idade", "cidade"],
  ["Ana", 25, "São Paulo"],
  ["Carlos", "30", "Rio de Janeiro"],
  ["Maria", "28", "Belo Horizonte"]
]

with open("pessoas.csv", "w", newline="") as arquivo:
  writer = csv.writer(arquivo)
  writer.writerows(dados)
