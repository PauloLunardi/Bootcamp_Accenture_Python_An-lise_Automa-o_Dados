import matplotlib.pyplot as plt

importancias = xgb.feature_importances_

plt.bar(range(len(importancias)), importancias)
plt.title("Importância das Variáveis")
plt.xlabel("Índice da Variável")
plt.ylabel("Importância")
plt.show()

# -------------------------------
# O código acima plota a importância das variáveis no modelo XGBoost:
#
# - xgb.feature_importances_ → retorna um array com a relevância de cada variável
#   usada pelo modelo. Quanto maior o valor, mais impacto aquela variável teve
#   nas decisões das árvores.
#
# - plt.bar(...) → cria um gráfico de barras mostrando a importância relativa
#   de cada variável pelo seu índice (posição no dataset).
#
# Interpretação:
# - As variáveis com maior importância são aquelas que mais contribuíram
#   para separar as classes (ex: fraude vs não fraude).
# - Esse gráfico ajuda a entender quais features são mais influentes,
#   trazendo mais explicabilidade ao modelo.
# - É útil para análise exploratória, seleção de variáveis e comunicação
#   dos resultados para stakeholders.
