import json

dados = {
  "nome": "Ana",
  "idade": 25,
  "cidade": "São Paulo"
}

with open("usuario.json", "w") as arquivo:
  json.dump(dados, arquivo)
