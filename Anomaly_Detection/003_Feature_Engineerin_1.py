# Nesta etapa criamos(ou alteramos) variaveis para ajudar nosso modelo.
# seria como equilibrar os dados para que o modelo entenda melhor 

import numpy as np

df["Amount_log"] = np.log1p(df["Amount"])
