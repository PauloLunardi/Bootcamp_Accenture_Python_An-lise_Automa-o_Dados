# Integrando as 2 librarias (Pandas + Matplotlib)
import pandas as md
import matplotlib.pyplot as plt

dados = {
  "produto": ["Notebook","Mouse","Teclado","Headset"],
  "vendas": [11,84,92,45]
}

df = pd.DataFrame(dados)

plt.bar(df["produto"], df["vendas"])

plt.show()
