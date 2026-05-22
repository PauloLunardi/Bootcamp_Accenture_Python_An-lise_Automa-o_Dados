fig, ax = plt.subplots(1,2, figsize=(10,4))

sns.histplot(df["total_bill"], ax=ax[0])
ax[0].set_title("Distibuição da Conta")

sns.boxplot(data=df, x="day", y="tip", ax=ax[1])
ax[1].set_title("Gorjetas por dia")

plt.show()
