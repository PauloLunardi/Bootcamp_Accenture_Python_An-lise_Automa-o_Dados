# Este script cria um arquivo "vendas.txt" com valores de vendas,
# lê cada linha, converte para inteiro e soma os valores.
# Ao final, imprime o total de vendas processado.

import csv

total = 0

with open("vendas.txt","w") as f:
  f.write("100\n200\n150\n300")

with open("vendas.txt","r") as f:
   for linha in f:
    valor = int(linha.strip())
    total += valor

print("Total de vendas:", total)
