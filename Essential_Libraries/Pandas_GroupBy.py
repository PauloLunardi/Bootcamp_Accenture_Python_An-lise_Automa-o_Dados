import pandas as pd

dados = {
  "produto": ["Notebook", "Mouse", "Teclado", "Headset", "Teclado"],
  "preco": [4600, 170, 322, 110, 430]
}

df = pd.DataFrame(dados)

# a função 'groupby' agrupa os produtos e '.mean()' realiza a media dos produtos agrupados
df.groupby("produto").mean()
