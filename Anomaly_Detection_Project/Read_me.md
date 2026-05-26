# Projeto de Machine Learning com Dados de Futebol

Este projeto tem como objetivo aplicar técnicas de **análise de dados** e **modelagem preditiva** em um dataset público de futebol, explorando desde a análise inicial até a explicabilidade dos modelos.

---

## 📂 Etapas do Projeto

### 1. Importação e Análise Inicial
- Carregar dados com **pandas**.
- Explorar estatísticas básicas (gols, cartões, posse de bola).
- Verificar **classificação** e **desbalanceamento** das classes.

### 2. Feature Engineering
- Criar variáveis derivadas (diferença de gols, desempenho em casa vs fora).
- Normalizar ou padronizar variáveis numéricas.

### 3. Preparação dos Dados
- Dividir em treino e teste (`train_test_split`).
- Escalar dados com **StandardScaler**.

### 4. Modelagem Inicial
- Treinar **Regressão Logística**.
- Gerar **classification_report** para avaliar precisão, recall e f1-score.

### 5. Curvas de Avaliação
- Plotar **ROC Curve** e calcular **ROC AUC Score**.
- Plotar **Precision-Recall Curve** para avaliar trade-off.

### 6. Balanceamento
- Aplicar **undersampling** (reduzir classe majoritária).
- Aplicar **oversampling/SMOTE** (gerar exemplos sintéticos da classe minoritária).

### 7. Modelos Avançados
- Treinar **Random Forest** com `class_weight="balanced"`.
- Criar **Pipeline** com pré-processamento + modelo.
- Ajustar **threshold** para melhorar recall.

### 8. XGBoost
- Treinar com `scale_pos_weight`.
- Gerar novo relatório de classificação.
- Avaliar **importância das variáveis** (`feature_importances_`).
- Ajustar hiperparâmetros com **GridSearchCV**.

### 9. Explicabilidade
- Usar **SHAP** para entender a contribuição de cada variável.
- Plotar gráficos de importância e summary plots.

---

## ⚖️ Comparação de Técnicas

| Etapa | Objetivo | Ferramenta |
|-------|----------|------------|
| [Logistic Regression](ca://s?q=Regressao_Logistica_em_machine_learning) | Modelo baseline | Simples, interpretável |
| [Random Forest](ca://s?q=Random_Forest_em_machine_learning) | Modelo robusto | Lida bem com não linearidades |
| [XGBoost](ca://s?q=XGBoost_em_machine_learning) | Modelo otimizado | Alta performance em dados tabulares |
| [Undersampling](ca://s?q=Undersampling_em_machine_learning) | Balancear classes | Remove dados da majoritária |
| [Oversampling/SMOTE](ca://s?q=SMOTE_em_machine_learning) | Balancear classes | Cria exemplos sintéticos |
| [SHAP](ca://s?q=SHAP_em_machine_learning) | Explicabilidade | Mostra impacto das variáveis |

---

## 🚀 Resultado Esperado
- Pipeline completo de **análise exploratória → modelagem → avaliação → explicabilidade**.
- Insights sobre variáveis que mais influenciam resultados de partidas.
- Comparação clara entre diferentes técnicas de balanceamento e modelos.
- Visualizações (ROC, Precision-Recall, SHAP) para comunicar resultados.

