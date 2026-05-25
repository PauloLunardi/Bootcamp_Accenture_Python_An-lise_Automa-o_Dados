# Métricas de Avaliação em Ciência de Dados

## Introdução
As **métricas de avaliação** são fundamentais para medir a qualidade e a performance de modelos em ciência de dados.  
Cada tipo de modelo (regressão, classificação ou agrupamento) exige métricas específicas que refletem sua capacidade de generalização e precisão.

## Explicação de Modelos em Ciência de Dados
Um modelo de **ciência de dados** é uma representação matemática ou estatística que busca aprender padrões a partir dos dados.  
A avaliação correta garante que o modelo não apenas se ajuste bem ao conjunto de treino, mas também seja capaz de generalizar para novos dados.

### Conceitos importantes
- **[Overfitting](ca://s?q=Overfitting_em_modelos_de_ciencia_de_dados)**: quando o modelo aprende demais os detalhes e ruídos dos dados de treino, perdendo capacidade de generalização.  
- **[Underfitting](ca://s?q=Underfitting_em_modelos_de_ciencia_de_dados)**: quando o modelo é muito simples e não consegue capturar os padrões relevantes dos dados.  
- **[Bias e Variância](ca://s?q=Bias_e_variancia_em_modelos)**: equilíbrio entre simplicidade e complexidade do modelo.  
- **[Validação](ca://s?q=Validacao_de_modelos_em_ciencia_de_dados)**: uso de dados de teste ou validação cruzada para medir desempenho real.  

---

# Análise de Erro vs Resíduo

## Definições

- **Erro (\(e_i\))**: diferença entre o valor previsto pelo modelo e o valor real:

$$
e_i = \hat{y}_i - y_i
$$

- **Resíduo (\(r_i\))**: diferença entre o valor observado e o valor ajustado pelo modelo:

$$
r_i = y_i - \hat{y}_i
$$

👉 Note que **erro e resíduo são numericamente iguais, mas com sinais opostos**:
- O **erro** é visto do ponto de vista da previsão.  
- O **resíduo** é visto do ponto de vista da observação.

## Interpretação

- Resíduos próximos de zero indicam bom ajuste.  
- Resíduos sistematicamente positivos ou negativos podem indicar **viés** no modelo.  
- A análise gráfica dos resíduos ajuda a identificar problemas como **heterocedasticidade** ou **não linearidade**.

## Exemplo em Python

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados fictícios
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([1.2, 1.9, 3.1, 3.9, 5.2])

# Modelo
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Cálculo de erros e resíduos
erro = y_pred - y
residuo = y - y_pred

print("Erro:", erro)
print("Resíduo:", residuo)

# Plot dos resíduos
plt.scatter(X, residuo)
plt.axhline(y=0, color="red", linestyle="--")
plt.title("Análise de Resíduos")
plt.xlabel("X")
plt.ylabel("Resíduo")
plt.show()
```

## Métricas de Modelos de Regressão
Modelos de regressão buscam prever valores contínuos.  
Principais métricas:
- **[MAE](ca://s?q=MAE_em_regressao)** (*Mean Absolute Error*): média dos erros absolutos.  
- **[MSE](ca://s?q=MSE_em_regressao)** (*Mean Squared Error*): penaliza erros grandes ao elevar ao quadrado.  
- **[RMSE](ca://s?q=RMSE_em_regressao)** (*Root Mean Squared Error*): raiz quadrada do MSE, mais interpretável.  
- **[R²](ca://s?q=R2_em_regressao)** (*Coeficiente de Determinação*): indica proporção da variância explicada pelo modelo.

### Mean Absolute Error
O **Mean Absolute Error (MAE)** é uma métrica usada para avaliar modelos de regressão.  
Ele mede a média dos erros absolutos entre os valores previstos (\(\hat{y}_i\)) e os valores reais (\(y_i\)).

#### Fórmula

\[
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
\]

- \(n\): número de observações  
- \(y_i\): valor real da observação \(i\)  
- \(\hat{y}_i\): valor previsto pelo modelo para a observação \(i\)  
- \(|y_i - \hat{y}_i|\): erro absoluto da previsão  

#### Interpretação
- O MAE indica **quanto, em média, as previsões se afastam dos valores reais**.  
- Quanto menor o MAE, melhor o desempenho do modelo.  
- É uma métrica **robusta** porque não eleva os erros ao quadrado (diferente do MSE), sendo menos sensível a outliers.  

#### Exemplo em Python
```python
from sklearn.metrics import mean_absolute_error

# Suponha valores reais e previstos
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Cálculo do MAE
mae = mean_absolute_error(y_true, y_pred)
print("MAE:", mae)
```
## Mean Squared Error
O **Mean Squared Error (MSE)** é uma métrica usada para avaliar modelos de regressão.  
Ele calcula a média dos erros ao quadrado entre os valores previstos (\(\hat{y}_i\)) e os valores reais (\(y_i\)).

#### Fórmula Simplificada
MSE = (1 / n) * Σ (yᵢ - ŷᵢ)²

- n → número de observações  
- yᵢ → valor real da observação i  
- ŷᵢ → valor previsto pelo modelo para a observação i  
- (yᵢ - ŷᵢ)² → erro ao quadrado da previsão

#### Interpretação
- O MSE indica **quanto, em média, os erros quadráticos se afastam dos valores reais**.  
- Quanto menor o MSE, melhor o desempenho do modelo.  
- Penaliza mais fortemente erros grandes, pois cada diferença é elevada ao quadrado.  
- É útil quando queremos destacar desvios grandes que não podem ser ignorados.

#### Exemplo em Python
```python
from sklearn.metrics import mean_squared_error

# Cálculo do MSE entre valores reais (y_test) e previstos (y_pred)
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)
```

## Métricas de Modelos de Classificação
Modelos de classificação buscam prever categorias.  
Principais métricas:
- **[Acurácia](ca://s?q=Acuracia_em_classificacao)**  
- **[Precisão](ca://s?q=Precisao_em_classificacao)**  
- **[Recall](ca://s?q=Recall_em_classificacao)**  
- **[F1-Score](ca://s?q=F1_score_em_classificacao)**  
- **[Matriz de Confusão](ca://s?q=Matriz_de_confusao_em_classificacao)**  
- **[ROC e AUC](ca://s?q=ROC_e_AUC_em_classificacao)**  

## Métricas de Modelos de Agrupamento
Modelos de agrupamento (clustering) buscam identificar grupos sem rótulos prévios.  
Principais métricas:
- **[Silhouette Score](ca://s?q=Silhouette_score_em_agrupamento)**  
- **[Davies-Bouldin Index](ca://s?q=Davies_Bouldin_index_em_agrupamento)**  
- **[Calinski-Harabasz Index](ca://s?q=Calinski_Harabasz_index_em_agrupamento)**  
- **[Inércia](ca://s?q=Inercia_em_agrupamento)**  

## Conclusão
A escolha da métrica correta depende do tipo de modelo e do objetivo da análise.  
Além disso, a **análise de erro vs resíduo** é essencial para interpretar o ajuste do modelo e identificar possíveis problemas de generalização.
