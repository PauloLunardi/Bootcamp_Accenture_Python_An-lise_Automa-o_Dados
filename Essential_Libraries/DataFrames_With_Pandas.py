import pandas as pd

dados = {
  "produto": ["Notebook", "Mouse", "Teclado", "Headset"],
  "preco": [4600, 170, 322, 110]
}

df = pd.DataFrame(dados)
print(df)
