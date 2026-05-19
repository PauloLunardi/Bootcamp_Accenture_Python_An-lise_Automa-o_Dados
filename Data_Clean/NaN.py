# NaN representa valores ausentes ou desconhecidos em um dataset.

import pandas as pd

# df.isnull().sum() retorna a quantidade de valores nulos em cada coluna do DataFrame.
# Útil para identificar rapidamente onde há dados faltantes e decidir como tratá-los.
df.isnull().sum()
