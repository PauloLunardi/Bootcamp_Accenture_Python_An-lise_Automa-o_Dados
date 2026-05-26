# 📊 Avaliação de Modelos e Técnicas Avançadas

Este módulo da pasta do projeto aborda duas frentes fundamentais em aprendizado de máquina:

1. **Avaliação e técnicas de balanceamento**  
2. **Modelos avançados e explicabilidade**

---

## 1. Avaliação e Técnicas de Balanceamento

### 🔎 Avaliação de Modelos
A avaliação de modelos de regressão e classificação é essencial para medir desempenho e identificar pontos de melhoria.  
As métricas mais comuns incluem:

- **[MAE](ca://s?q=MAE_em_regressao)** → erro médio absoluto  
- **[MSE](ca://s?q=MSE_em_regressao)** → erro médio ao quadrado  
- **[RMSE](ca://s?q=RMSE_em_regressao)** → raiz do erro médio ao quadrado  
- **[MAPE](ca://s?q=MAPE_em_regressao)** → erro percentual médio absoluto  
- **[R²](ca://s?q=Coeficiente_de_determinacao)** → coeficiente de determinação  

Essas métricas permitem comparar modelos e escolher o mais adequado para o problema.

### ⚖️ Técnicas de Balanceamento
Em problemas de **classificação desbalanceada**, é comum que uma classe tenha muito mais exemplos que outra.  
Para lidar com isso, utilizamos técnicas como:

- **[Oversampling](ca://s?q=Oversampling_em_machine_learning)** → duplicar exemplos da classe minoritária.  
- **[Undersampling](ca://s?q=Undersampling_em_machine_learning)** → reduzir exemplos da classe majoritária.  
- **[SMOTE](ca://s?q=SMOTE_em_machine_learning)** → gerar exemplos sintéticos para a classe minoritária.  
- **[Class Weights](ca://s?q=Class_weights_em_machine_learning)** → ajustar pesos das classes no treinamento.  

Essas abordagens ajudam a melhorar a performance e reduzir vieses.

---

## 2. Modelos Avançados e Explicabilidade

### 🚀 Modelos Avançados
Além de regressão linear e árvores de decisão, modelos mais sofisticados podem ser aplicados:

- **[Random Forest](ca://s?q=Random_Forest_em_machine_learning)**  
- **[Gradient Boosting](ca://s?q=Gradient_Boosting_em_machine_learning)**  
- **[XGBoost](ca://s?q=XGBoost_em_machine_learning)**  
- **[Redes Neurais](ca://s?q=Redes_neurais_em_machine_learning)**  

Esses modelos geralmente oferecem maior precisão, mas podem ser mais complexos de interpretar.

### 🧠 Explicabilidade
A interpretabilidade é crucial para entender **como** e **por que** um modelo toma decisões.  
Ferramentas e técnicas incluem:

- **[SHAP](ca://s?q=SHAP_em_machine_learning)** → valores de Shapley para explicar impacto das variáveis.  
- **[LIME](ca://s?q=LIME_em_machine_learning)** → explicações locais para previsões individuais.  
- **[Feature Importance](ca://s?q=Feature_importance_em_machine_learning)** → importância relativa das variáveis.  
- **[Partial Dependence Plots](ca://s?q=Partial_dependence_plots)** → mostram relação entre variáveis e previsão.  

Essas técnicas aumentam a confiança no modelo e ajudam na tomada de decisão.

---

## 📌 Conclusão
Este módulo reúne:
- **Métricas de avaliação** para medir desempenho.  
- **Técnicas de balanceamento** para lidar com dados desbalanceados.  
- **Modelos avançados** para maior precisão.  
- **Ferramentas de explicabilidade** para interpretar resultados.  

O objetivo é fornecer uma visão completa e prática sobre como avaliar, melhorar e explicar modelos de aprendizado de máquina.
