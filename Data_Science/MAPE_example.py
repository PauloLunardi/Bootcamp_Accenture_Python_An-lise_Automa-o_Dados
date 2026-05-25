mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

mape

# -------------------------------
# Comentário:
# O MAPE (Mean Absolute Percentage Error) calcula o erro percentual médio absoluto.
# Fórmula: (100 / n) * Σ ( |y_i - ŷ_i| / |y_i| )
# - y_test: valores reais
# - y_pred: valores previstos pelo modelo

# Interpretação:
# - Mostra em média quanto o modelo erra em relação ao valor real, expresso em porcentagem.
# - Exemplo: MAPE = 7 → significa que o modelo erra em média 7% dos valores reais.
# - Quanto menor o MAPE, melhor o desempenho do modelo.
# Observação: se algum valor real for zero, o MAPE pode ficar indefinido ou distorcido.
