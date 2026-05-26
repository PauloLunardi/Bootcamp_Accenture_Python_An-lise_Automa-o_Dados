# Random Forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=50,        # número de árvores na floresta
    max_depth=10,           # profundidade máxima de cada árvore
    class_weight="balanced",# ajusta os pesos das classes para compensar desbalanceamento
    n_jobs=-1,              # usa todos os núcleos disponíveis para acelerar o treino
    random_state=42         # garante reprodutibilidade dos resultados
)

# Treina o modelo com os dados de treino
rf.fit(x_train, y_train)

# Faz previsões no conjunto de teste
y_pred_rf = rf.predict(x_test)

# Gera relatório de classificação com métricas (precision, recall, f1-score, support)
print(classification_report(y_test, y_pred_rf))

# -------------------------------
# Interpretação:
# - O Random Forest combina várias árvores de decisão para melhorar a precisão e reduzir overfitting.
# - O parâmetro class_weight="balanced" é crucial em cenários desbalanceados (como fraude),
#   pois dá mais importância à classe minoritária durante o treino.
# - O classification_report mostra como o modelo performa em cada classe:
#   * Precision → quão confiáveis são as previsões positivas
#   * Recall → quão bem o modelo captura os casos positivos reais
#   * F1-score → equilíbrio entre precisão e recall
#   * Support → quantidade de exemplos reais de cada classe
#
# Esse setup ajuda a melhorar a detecção da classe minoritária sem perder desempenho na majoritária.
