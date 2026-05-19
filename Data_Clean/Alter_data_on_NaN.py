# Tratamento simplista da coluna "Cabin":
# Substitui valores ausentes (NaN) por "Unknown",
# garantindo que não haja linhas com NaN e mantendo a coluna original.
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Conferir novamente se ainda existem valores ausentes
print(df.isnull().sum())
