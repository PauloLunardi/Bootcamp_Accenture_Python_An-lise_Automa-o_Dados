import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(
  df,
  x="gdpPercap",
  y="lifeExp",
  size="pop",
  color="continent",
  hover_name="country",
  log_x=True,
  animation_frame="year",
  title="Evolução de PIB e Expectativa de Vida"
)

fig.show()

# Observação:
# Este script depende do dataset "tips.csv" disponível no repositório seaborn-data.
# Para garantir que os gráficos funcionem mesmo após reiniciar a sessão,
# é necessário carregar novamente os dados com pandas:
#
# import pandas as pd
# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
# df = pd.read_csv(url)
