from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

y_probs = model.predict_proba(x_test)[:,1]

fpr, tpr, _ = roc_curve(y_test, y_probs)

plt.plot(fpr, tpr)
plt.title("Roc Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()

print("AUC:", roc_auc_score(y_test, y_probs))

# -------------------------------
# O código acima avalia o modelo usando a curva ROC e o AUC:
#
# - predict_proba → retorna as probabilidades de cada classe. Selecionamos [:,1] para pegar
#   a probabilidade da classe positiva (fraude, por exemplo).
#
# - roc_curve → calcula os pontos da curva ROC, mostrando a relação entre:
#   * FPR (False Positive Rate) → taxa de falsos positivos
#   * TPR (True Positive Rate) → taxa de verdadeiros positivos
#
# - plt.plot(fpr, tpr) → plota a curva ROC, que ajuda a visualizar a capacidade do modelo
#   em distinguir entre classes.
#
# - roc_auc_score → calcula a área sob a curva ROC (AUC).
#   * AUC próximo de 1 → excelente desempenho
#   * AUC = 0.5 → modelo não melhor que um chute aleatório
#
# Em resumo: a curva ROC mostra o trade-off entre sensibilidade e especificidade,
# e o AUC resume esse desempenho em um único número.
