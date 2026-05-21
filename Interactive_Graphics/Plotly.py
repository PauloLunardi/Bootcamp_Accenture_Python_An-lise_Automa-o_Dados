import plotly.express as px
import plotly.io as pio

# Define o tema (template) para "plotly_dark"
pio.templates.default = "plotly_dark"

fig = px.scatter(
  df,
  x="total_bill",
  y="tip",
  color="day",
  title="Relação entre conta e gorjeta"
)

fig.show()


# Este script utiliza Plotly Express para criar um gráfico de dispersão (scatter).
# A coluna "day" do DataFrame é usada como variável de cor, atribuindo cores diferentes
  # para cada categoria (ex.: Sun, Sat, Thur, Fri).
# Importante: o parâmetro "color" não define tema visual (day/night),
  # apenas controla a coloração baseada nos dados.
  # Para alterar o estilo do gráfico (tema claro ou escuro),
  # deve-se usar plotly.io.templates (ex.: "plotly_dark").
