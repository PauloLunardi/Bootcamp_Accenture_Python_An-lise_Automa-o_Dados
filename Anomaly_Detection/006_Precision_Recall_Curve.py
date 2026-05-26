from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

precision, recall, _ = precision_recall_curve(y_test, y_probs)

plt.plot(recall, precision)
plt.title("Precision-Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.show()

# -------------------------------
# O código acima gera a curva Precision-Recall:
#
# - precision_recall_curve → calcula os pontos da curva mostrando a relação entre:
#   * Precision (precisão): entre todas as previsões positivas, quantas estavam corretas.
#   * Recall (revocação/sensibilidade): entre todos os casos positivos reais, quantos foram identificados corretamente.
#
# - plt.plot(recall, precision) → plota a curva Precision-Recall, útil para visualizar
#   o trade-off entre capturar mais positivos (recall) e manter previsões corretas (precision).
#
# Interpretação:
# - Uma curva mais próxima do canto superior direito indica melhor desempenho.
# - É especialmente relevante em cenários desbalanceados (como fraude), onde a acurácia
#   pode ser enganosa e precisamos avaliar o equilíbrio entre precisão e recall.
