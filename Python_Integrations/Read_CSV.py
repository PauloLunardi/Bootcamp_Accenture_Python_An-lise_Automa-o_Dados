# Lendo um arquivo CSV
import csv


with open("pessoas.csv", "r") as arquivo:
  leitor = csv.reader(arquivo)
  
  for linha in leitor:
    print(linha)
