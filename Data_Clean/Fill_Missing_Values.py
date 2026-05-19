# Substitui os valores nulos da coluna "Age" pela média da própria coluna,
# garantindo que não haja mais dados faltantes nessa variável.
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Verifica novamente a quantidade de valores nulos em "Age"
# para confirmar que todos foram preenchidos.
df["Age"].isnull().sum()
