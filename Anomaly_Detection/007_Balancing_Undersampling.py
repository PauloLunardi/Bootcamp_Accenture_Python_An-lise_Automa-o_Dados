# Undersampling
fraudes = df[df["Class"] == 1]   # Seleciona todas as linhas da classe 1 (fraudes)
normais = df[df["Class"] == 0].sample(len(fraudes), random_state=42)
# Seleciona aleatoriamente a mesma quantidade de linhas da classe 0 (normais)
# que existe na classe 1, garantindo equilíbrio entre as classes.

df_under = pd.concat([fraudes, normais])
# Junta os dois subconjuntos (fraudes + normais) em um novo DataFrame balanceado.
#
# Interpretação:
# - O undersampling reduz a quantidade de exemplos da classe majoritária (normais),
#   para igualar ao número da classe minoritária (fraudes).
# - Isso ajuda o modelo a não ficar enviesado para a classe dominante.
# - Porém, como descartamos dados da classe majoritária, podemos perder informação.
# - É uma técnica útil quando o dataset é muito desbalanceado e grande.
