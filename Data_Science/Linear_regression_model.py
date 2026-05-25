# Modelo de Regressão Linear
model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)


# Fórmula da Regressão Linear O modelo busca ajustar uma reta da forma:
#     𝑦 = 𝛽 0 + 𝛽 1 𝑥 + 𝜖

# 𝑦: variável dependente (target)
# 𝑥: variável independente (feature)
# 𝛽0: intercepto (valor de 𝑦 quando 𝑥=0)
# 𝛽1: coeficiente angular (quanto 𝑦 varia quando 𝑥 aumenta uma unidade)
# 𝜖: erro ou resíduo
