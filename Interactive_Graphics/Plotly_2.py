import pandas as pd
import plotly.express as px

# Lê o dataset "tips.csv" diretamente do repositório seaborn-data
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)  # carrega o dataset em um DataFrame

# Cria um gráfico de dispersão relacionando total da conta e gorjeta
fig = px.scatter(
    df,
    x="total_bill",          # eixo X = valor total da conta
    y="tip",                 # eixo Y = valor da gorjeta
    color="size",            # cores variam conforme o tamanho da mesa
    hover_data=["sex","time"], # mostra sexo e período da refeição ao passar o mouse
    title="Relação entre Conta e Gorjeta"  # título do gráfico
)

fig.show()  # exibe o gráfico interativo
