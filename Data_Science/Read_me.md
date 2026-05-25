# Métricas de Avaliação em Ciência de Dados

## Introdução
As **métricas de avaliação** são fundamentais para medir a qualidade e a performance de modelos em ciência de dados.  
Cada tipo de modelo (regressão, classificação ou agrupamento) exige métricas específicas que refletem sua capacidade de generalização e precisão.

---

## Explicação de Modelos em Ciência de Dados
Um modelo de **ciência de dados** é uma representação matemática ou estatística que busca aprender padrões a partir dos dados.  
A avaliação correta garante que o modelo não apenas se ajuste bem ao conjunto de treino, mas também seja capaz de generalizar para novos dados.

### Conceitos importantes
- **[Overfitting](ca://s?q=Overfitting_em_modelos_de_ciencia_de_dados)**: quando o modelo aprende demais os detalhes e ruídos dos dados de treino, perdendo capacidade de generalização.  
- **[Underfitting](ca://s?q=Underfitting_em_modelos_de_ciencia_de_dados)**: quando o modelo é muito simples e não consegue capturar os padrões relevantes dos dados.  
- **[Bias e Variância](ca://s?q=Bias_e_variancia_em_modelos)**: equilíbrio entre simplicidade e complexidade do modelo.  
- **[Validação](ca://s?q=Validacao_de_modelos_em_ciencia_de_dados)**: uso de dados de teste ou validação cruzada para medir desempenho real.  

---

## Análise de Erro vs Resíduo

### Definições
- **Erro (\(e_i\))**: diferença entre o valor previsto pelo modelo (\(\hat{y}_i\)) e o valor real (\(y_i\)).  
  

\[
  e_i = \hat{y}_i - y_i
  \]



- **Resíduo (\(r_i\))**: diferença entre o valor observado (\(y_i\)) e o valor ajustado pelo modelo (\(\hat{y}_i\)).  
  

\[
  r_i = y_i - \hat{y}_i
  \]



👉 Note que **erro e resíduo são numericamente iguais, mas com sinais opostos**.  
- O **erro** é visto do ponto de vista da previsão.  
- O **resíduo** é visto do ponto de vista da observação.

### Interpretação
- Resíduos próximos de zero indicam bom ajuste.  
- Resíduos sistematicamente positivos ou negativos podem indicar **viés** no modelo.  
- A análise gráfica dos resíduos ajuda a identificar problemas como **heterocedasticidade** ou **não linearidade**.

---

## Métricas de Modelos de Regressão
Modelos de regressão buscam prever valores contínuos.  
Principais métricas:
- **[MAE](ca://s?q=MAE_em_regressao)** (*Mean Absolute Error*): média dos erros absolutos.  
- **[MSE](ca://s?q=MSE_em_regressao)** (*Mean Squared Error*): penaliza erros grandes ao elevar ao quadrado.  
- **[RMSE](ca://s?q=RMSE_em_regressao)** (*Root Mean Squared Error*): raiz quadrada do MSE, mais interpretável.  
- **[R²](ca://s?q=R2_em_regressao)** (*Coeficiente de Determinação*): indica proporção da variância explicada pelo modelo.  

---

## Métricas de Modelos de Classificação
Modelos de classificação buscam prever categorias.  
Principais métricas:
- **[Acurácia](ca://s?q=Acuracia_em_classificacao)**  
- **[Precisão](ca://s?q=Precisao_em_classificacao)**  
- **[Recall](ca://s?q=Recall_em_classificacao)**  
- **[F1-Score](ca://s?q=F1_score_em_classificacao)**  
- **[Matriz de Confusão](ca://s?q=Matriz_de_confusao_em_classificacao)**  
- **[ROC e AUC](ca://s?q=ROC_e_AUC_em_classificacao)**  

---

## Métricas de Modelos de Agrupamento
Modelos de agrupamento (clustering) buscam identificar grupos sem rótulos prévios.  
Principais métricas:
- **[Silhouette Score](ca://s?q=Silhouette_score_em_agrupamento)**  
- **[Davies-Bouldin Index](ca://s?q=Davies_Bouldin_index_em_agrupamento)**  
- **[Calinski-Harabasz Index](ca://s?q=Calinski_Harabasz_index_em_agrupamento)**  
- **[Inércia](ca://s?q=Inercia_em_agrupamento)**  

---

## Conclusão
A escolha da métrica correta depende do tipo de modelo e do objetivo da análise.  
Além disso, a **análise de erro vs resíduo** é essencial para interpretar o ajuste do modelo e identificar possíveis problemas de generalização.
