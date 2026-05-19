# df.dropna() remove todas as linhas que possuem valores nulos,
# criando um novo DataFrame sem dados faltantes.
df_limp = df.dropna()

# df.head() mostra as primeiras linhas do DataFrame,
# útil para inspecionar rapidamente como ficou após a limpeza.
df_limp.head()
