# Lendo JSON

with open("usuario.json", "r") as arquivo:
  dados = json.load(arquivo)

print(dados)

# Retorno
# {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}
