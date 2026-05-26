### Interpretação dos resultados

#### Classe 0 (não fraude, por exemplo)
  - Precision = 1.00 → todas as previsões de classe 0 estavam corretas.
  - Recall = 1.00 → o modelo identificou todos os casos reais da classe 0.
  - F1-score = 1.00 → equilíbrio perfeito entre precisão e recall.
  
  👉 Isso mostra que o modelo está excelente para a classe majoritária.

#### Classe 1 (fraude, por exemplo)
  - Precision = 0.83 → quando o modelo prevê fraude, 83% das vezes está certo.
  - Recall = 0.63 → mas ele só consegue capturar 63% das fraudes reais.
  - F1-score = 0.72 → desempenho razoável, mas longe do ideal.
  
  👉 Aqui vemos a dificuldade em detectar a classe minoritária, típica em problemas desbalanceados.


#### Accuracy = 1.00
  - Parece perfeito, mas é enganoso: como a classe 0 domina (85.307 exemplos contra apenas 136 da classe 1), o modelo acerta quase tudo só por classificar corretamente a maioria.
  - Por isso, métricas como precision, recall e f1-score são mais relevantes que a acurácia em cenários desbalanceados.


#### Macro avg (0.92 / 0.82 / 0.86)
  - Média simples entre as classes. Mostra que o desempenho geral cai quando consideramos ambas as classes igualmente.


#### Weighted avg (≈1.00)
  - Média ponderada pelo número de exemplos. Como a classe 0 domina, o resultado fica próximo de 1.00, mascarando a dificuldade na classe 1.


#### Pontos de análise
  - O modelo está muito bom para a classe majoritária (0).
  - Está razoável para a classe minoritária (1), mas perde recall (não detecta todas as fraudes).
  - A acurácia alta é ilusória por causa do desbalanceamento.
  - O foco deve ser melhorar o recall da classe minoritária, sem perder muita precisão.


#### Próximos passos possíveis
  - Aplicar técnicas de balanceamento como oversampling, undersampling ou SMOTE.
  - Ajustar class weights na regressão logística para dar mais importância à classe minoritária.
  - Testar modelos avançados como Random Forest ou Gradient Boosting, que podem lidar melhor com desbalanceamento.
