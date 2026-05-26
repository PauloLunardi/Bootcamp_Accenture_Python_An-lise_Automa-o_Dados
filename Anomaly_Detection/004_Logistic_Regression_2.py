# Relatório de classificação com várias métricas importantes para avaliar o desempenho do modelo
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

# -------------------------------
# O classification_report retorna um resumo com métricas de avaliação do modelo de classificação:
# - precision (precisão): entre todas as previsões positivas, quantas estavam corretas.
# - recall (revocação/sensibilidade): entre todos os casos positivos reais, quantos foram identificados corretamente.
# - f1-score: média harmônica entre precisão e recall, equilibrando as duas métricas.
# - support: número de ocorrências reais de cada classe no conjunto de teste.
#
# Interpretação:
# - Valores próximos de 1 indicam bom desempenho.
# - O relatório mostra essas métricas para cada classe separadamente,
#   além de médias (macro, weighted) que resumem o desempenho geral.
