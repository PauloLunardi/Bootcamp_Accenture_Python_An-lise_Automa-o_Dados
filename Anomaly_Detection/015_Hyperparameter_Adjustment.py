from sklearn.model_selection import GridSearchCV

param_grid = {
    "max_depth": [3, 5],        # profundidade máxima das árvores
    "n_estimators": [50, 100]   # número de árvores no ensemble
}

grid = GridSearchCV(
    XGBClassifier(eval_metric="logloss"), # modelo base
    param_grid,                           # grade de parâmetros a testar
    scoring="recall",                     # métrica usada para escolher o melhor modelo
    cv=3                                  # validação cruzada com 3 folds
)

# Treina o GridSearchCV: testa todas as combinações de parâmetros
# e escolhe a que maximiza o recall.
grid.fit(x_train, y_train)

print("Best Model:", grid.best_params_)

# -------------------------------
# Interpretação:
# - O GridSearchCV percorre todas as combinações de parâmetros definidos em param_grid.
# - Para cada combinação, ele treina o modelo e avalia usando validação cruzada (cv=3).
# - O parâmetro scoring="recall" indica que queremos maximizar o recall,
#   ou seja, capturar o maior número possível de casos positivos (fraudes).
# - grid.best_params_ retorna os hiperparâmetros que tiveram melhor desempenho.
#
# Vantagens:
# - Automatiza a busca por hiperparâmetros ideais.
# - Garante que a escolha seja baseada em métricas relevantes (nesse caso, recall).
# - Ajuda a melhorar o desempenho do modelo sem precisar de ajustes manuais.
