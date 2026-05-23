fig, ax = plt.subplots(2,2, figsize=(12,8))

sns.histplot(df["total_bill"], ax=ax[0,0])
ax[0,0].set_title("Distribuição das contas")

sns.boxplot(data=df, x="day", y="tip", ax=ax[0,1])
ax[0,1].set_title("Grojetas por dia")

sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax[1,0])
ax[1,0].set_title("Conta vs Gorjeta")

sns.countplot(data=df, x="day", ax=ax[1,1])
ax[1,1].set_title("Quantidade de clientes por dia")

plt.tight_layout()
                  
plt.show()

# Observação:
# Este script depende do dataset "tips.csv" disponível no repositório seaborn.py.
# Para garantir que os gráficos funcionem mesmo após reiniciar a sessão,
# é necessário carregar novamente os dados com pandas:
#
# import pandas as pd
# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
# df = pd.read_csv(url)
