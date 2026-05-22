import matplotlib.pyplot as plt

# Cria a figura com tamanho definido
plt.figure(figsize=(8,5))

# Gera o gráfico de barras: eixo X = dia, eixo Y = gorjeta
# O parâmetro color define a cor das barras
plt.bar(df["day"], df["tip"], color="green")

# Adiciona título e rótulos dos eixos
plt.title("Gorjetas por dia")
plt.xlabel("Dia")
plt.ylabel("Gorjeta")

# Exibe o gráfico
plt.show()
