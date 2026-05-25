# Etapa 1: cálculo dos resíduos
# Os resíduos representam a diferença entre os valores reais (y_test)
# e os valores previstos pelo modelo (y_pred).
# Fórmula: resíduo = y_real - y_previsto
residuos = y_test - y_pred


# Etapa 2: visualização dos resíduos
# Cria um gráfico de dispersão (scatter plot) dos resíduos em função dos valores previstos.
plt.figure(figsize=(6,5))               # Define o tamanho da figura
plt.scatter(y_pred, residuos)           # Plota os resíduos vs valores previstos
plt.axhline(0, color='red')             # Linha horizontal em y=0 para referência
plt.xlabel("Valores Preditivos")        # Rótulo do eixo X
plt.ylabel("Resíduos")                  # Rótulo do eixo Y
plt.title("Resíduos vs Valores Preditos") # Título do gráfico
plt.show()                              # Exibe o gráfico
