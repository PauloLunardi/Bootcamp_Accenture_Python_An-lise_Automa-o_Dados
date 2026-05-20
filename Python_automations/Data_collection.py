import requests

url = "https://api.agify.io/?name=ana"

resposta = requests.get(url)

dados = resposta.json()

print(dados)
