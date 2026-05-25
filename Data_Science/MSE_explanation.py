from sklearn.metrics import mean_squared_error

# MSE = média dos erros ao quadrado
# Mede o quanto, em média, as previsões se afastam dos valores reais,
# penalizando mais fortemente erros grandes.
mse = mean_squared_error(y_test, y_pred)

mse
