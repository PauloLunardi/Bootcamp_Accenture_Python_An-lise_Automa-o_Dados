# Usando o Matplotlib para criar grafico de barras
import matplotlib.pyplot as plt

produtos = ["Notebook","Mouse","Teclado","Headset"]
vendas = [11,84,92,45]

plt.bar(produtos,vendas)
plt.show()

# Usando o Matplotlib para criar grafico de dispersão
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,5,4,7]

plt.scatter(x,y)
plt.show()
