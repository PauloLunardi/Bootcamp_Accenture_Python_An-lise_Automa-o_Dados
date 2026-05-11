# Depois de coletar dadops da API, podemos salvar esses dados em um arquivo JSON

import json
import requests

url = "https://api.agify.io/?name=Ana"

resposta = requests.get(url)

dados = resposta.json()

with open("dados_api.json", "w") as arquivo:
  json.dump(dados, arquivo)
