# Preparando os dados para treinar o modelo

from sklearn.model_selection import train_test_split

# Define as variáveis independentes (X) e a variável alvo (y).
# - X: todas as colunas do DataFrame, exceto "Class"
# - y: a coluna "Class", que representa a variável que queremos prever
x = df.drop("Class", axis=1)
y = df["Class"]

# Divide os dados em conjuntos de treino e teste.
# - x_train, y_train: usados para treinar o modelo
# - x_test, y_test: usados para avaliar o modelo
# - test_size=0.3 → 30% dos dados vão para teste e 70% para treino
# - random_state=42 → garante reprodutibilidade, sempre a mesma divisão
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
