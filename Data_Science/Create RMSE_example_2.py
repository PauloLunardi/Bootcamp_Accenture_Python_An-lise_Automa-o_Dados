from sklearn.metrics import mean_squared_error
import numpy as np

# Cálculo do RMSE entre valores reais (y_test) e previstos (y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("RMSE:", rmse)
