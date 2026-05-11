# Requisições HTTP em API

import requests

url = "https://api.agify.io/?name=Isabela"

resposta = requests.get(url)

dados = resposta.json()

print(dados)

# Retorno: {'count': 2190, 'name': 'Isabela', 'age': 42}
