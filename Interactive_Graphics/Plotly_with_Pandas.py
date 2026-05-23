# Analisando qual do horarios tem maior ganho de gorjetas pelo dia da semana
import pandas as pd
import plotly.express as px


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

df = pd.read_csv(url)

fig = px.scatter(
    df,
    x="total_bill",         
    y="tip",                 
    color="day",
    size="size",
    facet_col="time", 
    title="Análise de Gorjetas no restaurante"
)

fig.show()  

