from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Cria uma nova coluna "Amount_scaled" com os valores da coluna "Amount" padronizados.
# O StandardScaler transforma os dados para que tenham:
# - média = 0
# - desvio padrão = 1
# Isso garante que a variável "Amount" fique na mesma escala das demais,
# evitando que valores muito grandes ou muito pequenos distorçam o treinamento do modelo.
df["Amount_scaled"] = scaler.fit_transform(df[["Amount"]])
