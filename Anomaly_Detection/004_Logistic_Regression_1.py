# Criando o modelo de Regressão Logística.
from sklearn.linear_model import LogisticRegression

# - max_iter=1000 → define o número máximo de iterações para o algoritmo convergir.
model = LogisticRegression(max_iter=1000)

# Treina o modelo usando os dados de treino (x_train, y_train).
# O modelo aprende a relação entre as variáveis independentes (X) e a variável alvo (y).
model.fit(x_train, y_train)

# Usa o modelo treinado para prever os valores da variável alvo no conjunto de teste.
# y_pred conterá as previsões feitas pelo modelo com base em x_test.
y_pred = model.predict(x_test)
