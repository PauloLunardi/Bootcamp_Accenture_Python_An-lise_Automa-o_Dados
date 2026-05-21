import matplotlib.pyplot as plt

plt.scatter(df["total_bill"], df["tip"])

plt.xlabel("Conta total")
plt.ylabel("Valor da gorjeta")

plt.title('Relação entre conta e gorjeta')

plt.show()
