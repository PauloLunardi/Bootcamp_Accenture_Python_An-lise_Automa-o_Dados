import shap   # importa a biblioteca SHAP
explainer = shap.Explainer(xgb)              # Cria o explicador SHAP para o modelo treinado
shap_values = explainer(x_test[:100])        # Calcula os valores SHAP para 100 amostras do conjunto de teste

shap.plots.bar(shap_values)                  # Plota gráfico de barras com a importância média das variáveis

# -------------------------------
# O SHAP é uma técnica de interpretabilidade que mostra quanto cada variável contribui
# para a previsão do modelo em cada exemplo.
#
# - shap.Explainer(xgb) → cria um objeto que sabe como calcular os valores SHAP para o modelo XGBoost.
# - shap_values → contém os valores SHAP, que representam a contribuição de cada feature
#   para a saída do modelo em cada amostra.
# - shap.plots.bar → gera um gráfico de barras mostrando a importância média das variáveis
#   (quanto elas influenciam positivamente ou negativamente nas previsões).
#
# Interpretação:
# - Variáveis com barras maiores são as que mais impactam as decisões do modelo.
# - Esse gráfico ajuda a entender quais features são mais relevantes para explicar
#   as previsões, trazendo transparência e confiança ao modelo.
