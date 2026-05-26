threshold = 0.3

# Converte probabilidades em previsões binárias usando um limiar customizado.
# - Se a probabilidade da classe positiva (fraude, por exemplo) for maior que 0.3,
#   o modelo classifica como 1 (fraude).
# - Caso contrário, classifica como 0 (não fraude).
y_pred_custom = (y_probs > threshold).astype(int)

# Gera relatório de classificação com métricas (precision, recall, f1-score, support)
print(classification_report(y_test, y_pred_custom))

# -------------------------------
# Interpretação:
# - O threshold padrão da regressão logística é 0.5.
# - Ao reduzir para 0.3, o modelo fica mais "sensível" e passa a detectar mais casos positivos.
#   Isso tende a aumentar o recall (captura mais fraudes), mas pode reduzir a precisão
#   (mais falsos positivos).
# - Ajustar o threshold é uma técnica importante em cenários desbalanceados,
#   pois permite encontrar o ponto ótimo entre recall e precisão.
