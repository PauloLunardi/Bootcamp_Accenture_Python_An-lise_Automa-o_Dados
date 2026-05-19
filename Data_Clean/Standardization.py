# Transformação de variáveis
# É utilizado quando precisamops transformar dados para facilitar a análise.

df["Age_log"] = df["Age"].apply(lambda x: x)

print(fd["Age_log"])

