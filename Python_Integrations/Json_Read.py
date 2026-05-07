import json

dados = {
  "nome": "Ana",
  "idade": 25,
  "cidade": "São Paulo"
}

with open("usuario.json", "w") as arquivo:
  json.dump(dados, arquivo)

# recomendações utilizar UTF-8 e indent 4
"""import json

dados = {"nome": "Paulo", "idade": 37}

with open("usuario.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)  # indent deixa o JSON mais legível
"""
