from sklearn.metrics import mean_absolute_error

# Calcula o Mean Absolute Error (MAE) entre os valores reais (y_test)
# e os valores previstos pelo modelo (y_pred).
# Fórmula: MAE = (1/n) * Σ |y_i - ŷ_i|
# Interpretação: indica, em média, o quanto as previsões se afastam dos valores reais.
mae = mean_absolute_error(y_test, y_pred)

# Exibe o valor do MAE. Quanto menor, melhor o desempenho do modelo.
mae

#... 50413.43330810045
