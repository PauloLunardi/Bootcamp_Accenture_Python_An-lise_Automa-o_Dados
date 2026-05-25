# Métricas de Avaliação em Ciência de Dados

## Introdução
As **métricas de avaliação** são fundamentais para medir a qualidade e a performance de modelos em ciência de dados.  
Cada tipo de modelo (regressão, classificação ou agrupamento) exige métricas específicas que refletem sua capacidade de generalização e precisão.

---

## Explicação de Modelos em Ciência de Dados
Um modelo de **ciência de dados** é uma representação matemática ou estatística que busca aprender padrões a partir dos dados.  
A avaliação correta garante que o modelo não apenas se ajuste bem ao conjunto de treino, mas também seja capaz de generalizar para novos dados.

Principais pontos:
- **[Validação](ca://s?q=Validacao_de_modelos_em_ciencia_de_dados)**: uso de dados de teste ou validação cruzada.  
- **[Overfitting](ca://s?q=Overfitting_em_modelos_de_ciencia_de_dados)**: quando o modelo aprende demais os dados de treino e perde capacidade de generalização.  
- **[Bias e Variância](ca://s?q=Bias_e_variancia_em_modelos)**: equilíbrio entre simplicidade e complexidade do modelo.  

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

- **[Acurácia](ca://s?q=Acuracia_em_classificacao)**: proporção de acertos totais.  
- **[Precisão](ca://s?q=Precisao_em_classificacao)**: proporção de positivos corretos entre os previstos.  
- **[Recall](ca://s?q=Recall_em_classificacao)**: proporção de positivos corretos entre os reais.  
- **[F1-Score](ca://s?q=F1_score_em_classificacao)**: média harmônica entre precisão e recall.  
- **[Matriz de Confusão](ca://s?q=Matriz_de_confusao_em_classificacao)**: tabela que mostra acertos e erros por classe.  
- **[ROC e AUC](ca://s?q=ROC_e_AUC_em_classificacao)**: curvas que avaliam desempenho em diferentes limiares.  

---

## Métricas de Modelos de Agrupamento
Modelos de agrupamento (clustering) buscam identificar grupos sem rótulos prévios.  
Principais métricas:

- **[Silhouette Score](ca://s?q=Silhouette_score_em_agrupamento)**: mede a separação e coesão dos clusters.  
- **[Davies-Bouldin Index](ca://s?q=Davies_Bouldin_index_em_agrupamento)**: avalia a similaridade entre clusters.  
- **[Calinski-Harabasz Index](ca://s?q=Calinski_Harabasz_index_em_agrupamento)**: mede a dispersão intra e inter-cluster.  
- **[Inércia](ca://s?q=Inercia_em_agrupamento)**: soma das distâncias dos pontos ao centro do cluster.  

---

## Conclusão
A escolha da métrica correta depende do tipo de modelo e do objetivo da análise.  
Avaliar bem é tão importante quanto treinar bem: métricas garantem que o modelo seja útil, confiável e aplicável em cenários reais.
