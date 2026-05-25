# Cria um DataFrame com todas as métricas de avaliação do modelo.
# Cada chave do dicionário vira uma coluna (MAE, MSE, RMSE, MAPE, R2),
# e os valores calculados são organizados em uma única linha.

metrics = pd.DataFrame({
    "MAE":[mae],
    "MSE":[mse],
    "RMSE":[rmse],
    "MAPE":[mape],
    "R2":[r2]
})
