from sklearn.metrics import r2_score

# R² = coeficiente de determinação
# Mede a proporção da variabilidade dos dados explicada pelo modelo.
# Fórmula: R² = 1 - (SS_res / SS_tot)

# Interpretação:
# - R² = 0 → modelo não explica nada
# - R² = 1 → modelo explica toda a variabilidade
# Quanto maior o R², melhor o ajuste do modelo.
r2 = r2_score(y_test, y_pred)

r2
