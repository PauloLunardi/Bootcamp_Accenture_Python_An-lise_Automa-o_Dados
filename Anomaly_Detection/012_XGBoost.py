from xgboost import XGBClassifier

xgb = XGBClassifier(
    scale_pos_weight=10,       # ajusta o peso da classe minoritária para lidar com desbalanceamento
    use_label_encoder=False,   # evita warnings relacionados ao encoder interno do XGBoost
    eval_metric="logloss"      # métrica de avaliação usada durante o treino (log loss)
)

# Treina o modelo com os dados de treino
xgb.fit(x_train, y_train)

# Faz previsões no conjunto de teste
y_pred_xgb = xgb.predict(x_test)

# -------------------------------
# Interpretação:
# - O XGBClassifier é baseado em Gradient Boosting, combinando várias árvores de decisão
#   de forma sequencial para melhorar a performance.
# - O parâmetro scale_pos_weight=10 é usado para dar mais importância à classe minoritária
#   (fraudes, por exemplo). Esse valor geralmente é definido como a razão entre
#   a quantidade de exemplos da classe majoritária e da minoritária.
# - eval_metric="logloss" mede a perda logarítmica, útil para avaliar classificadores binários.
#
# Vantagens:
# - XGBoost costuma ter alta performance em dados tabulares.
# - É robusto contra overfitting e oferece várias opções de regularização.
# - Permite lidar bem com desbalanceamento via scale_pos_weight.
