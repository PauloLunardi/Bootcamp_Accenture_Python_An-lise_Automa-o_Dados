# Normalização da coluna "Fare":
# Transforma os valores para uma escala entre 0 e 1,
# usando a fórmula (valor - mínimo) / (máximo - mínimo).
# Isso garante que todos os dados fiquem na mesma escala,
# facilitando comparações e evitando distorções em análises ou modelos.
df["Fare_normalized"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())

# Visualiza as primeiras linhas para conferir o resultado da normalização.
df.head()
