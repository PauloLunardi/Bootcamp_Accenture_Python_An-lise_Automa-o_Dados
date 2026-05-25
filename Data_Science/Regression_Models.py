import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

df = pd.read_csv(url)

df.head()

# Remove todas as linhas com valores nulos (NaN) do DataFrame.
# Isso evita problemas durante o treinamento do modelo.
df = df.dropna()

# Cria o conjunto de variáveis independentes (features).
# Aqui removemos a coluna "median_house_value", pois ela é o alvo (target).
x = df.drop("median_house_value", axis=1)

# Converte variáveis categóricas em variáveis numéricas (dummy variables).
# Exemplo: "ocean_proximity" vira colunas binárias como "ocean_proximity_NEAR BAY".
x = pd.get_dummies(x)

# Define a variável dependente (target) que queremos prever:
# o valor mediano das casas.
y = df["median_house_value"]

# Divide os dados em conjuntos de treino e teste.
# - x: variáveis independentes (features)
# - y: variável alvo (target)
# - test_size=0.2 → 20% dos dados vão para teste e 80% para treino
# - random_state=42 → garante reprodutibilidade (mesmo resultado em cada execução)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Esse passo é fundamental porque:
# O treino (x_train, y_train) serve para o modelo aprender os padrões.
# O teste (x_test, y_test) serve para avaliar se o modelo generaliza bem para dados novos.

# Assim você documenta diretamente no código o que está acontecendo.

