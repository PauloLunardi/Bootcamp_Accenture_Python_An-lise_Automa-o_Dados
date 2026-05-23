# Analisando qual é o sexo das pessoas que dão gorjetas

px.scatter(
  df,
  x="total_bill",
  y="tip",
  color="sex",
  size="size",
  animation_frame="day"
)

# Observação:
# Este script depende do dataset "tips.csv" disponível no repositório seaborn-data.
# Para garantir que os gráficos funcionem mesmo após reiniciar a sessão,
# é necessário carregar novamente os dados com pandas:
#
# import pandas as pd
# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
# df = pd.read_csv(url)
