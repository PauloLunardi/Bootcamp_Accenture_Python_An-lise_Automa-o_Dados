# Oversampling com SMOTE
from imblearn.over_sampling import SMOTE

smote = SMOTE()

# Aplica o SMOTE para gerar exemplos sintéticos da classe minoritária.
# - x_res: variáveis independentes após o balanceamento
# - y_res: variável alvo após o balanceamento
x_res, y_res = smote.fit_resample(x, y)

# -------------------------------
# O SMOTE (Synthetic Minority Over-sampling Technique) cria novos exemplos da classe minoritária
# em vez de apenas duplicar os existentes. Ele gera pontos sintéticos interpolando entre
# exemplos reais próximos.
#
# Vantagens:
# - Ajuda a reduzir o desbalanceamento sem descartar dados da classe majoritária.
# - Melhora a capacidade do modelo de aprender padrões da classe minoritária.
#
# Pontos de atenção:
# - Pode introduzir exemplos artificiais que não representam perfeitamente a realidade.
# - É importante avaliar se o modelo não passa a "superajustar" aos dados sintéticos.
