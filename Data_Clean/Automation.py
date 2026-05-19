# Automação de pré-Processamento

# Um pipeline de dados executa várias etapas automaticamente:
  # 1. Carregar dados
  # 2. Limpar os dados
  # 3. Transformar os dados
  # 4. Gerar dataset final

def limpar_dados(df):
  df["Age"].fillna(df["Age"].mean(), inplace=True)

  df["Fare_normalized"] = (
    df["Fare"] - df["Fare"].min()
  ) / (df["Fare"].max() - df["Fare"].min())

  return df

#Retornar o DataFrame
df = limpar_dados(df)

df.head()
