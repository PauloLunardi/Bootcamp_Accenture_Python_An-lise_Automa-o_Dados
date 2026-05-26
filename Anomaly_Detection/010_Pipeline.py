from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ("scaler", StandardScaler()),                 # Etapa 1: padroniza os dados (média=0, desvio padrão=1)
    ("model", LogisticRegression(max_iter=1000))  # Etapa 2: aplica regressão logística com até 1000 iterações
])

# Treina o pipeline: primeiro aplica o StandardScaler nos dados de treino,
# depois ajusta o modelo de regressão logística.
pipeline.fit(x_train, y_train)

# Faz previsões no conjunto de teste.
# O pipeline garante que os mesmos passos de pré-processamento (scaler)
# sejam aplicados automaticamente antes da predição.
y_pred = pipeline.predict(x_test)

# -------------------------------
# Interpretação:
# - O Pipeline organiza o fluxo de trabalho em etapas sequenciais.
# - Isso evita erros de consistência, pois garante que o mesmo pré-processamento
#   usado no treino seja aplicado no teste e em novos dados.
# - É uma prática recomendada em machine learning, pois torna o código mais limpo,
#   reprodutível e fácil de manter.
