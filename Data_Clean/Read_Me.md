# Introdução á limpeza de dados

## Qualidade de dados
Antes de analisar dados, precisamos garantir que eles possuem boa qualidade.
  Dados de baixa qualidade podem gerar:
      - Análise incorretas
      - modelos imprecisos
      - Decições erradosa
  Por isso, uma etapa importante da análise de dados é a limpeza de dados(data cleaning).

  Problemas comuns em datasets
  
    Alguns Problemas são:
      - Valores ausentes
      - dados duplicados
      - valores incosistentes
      - formatos incorretos

### Resumo do df.info() em Pandas

O método `df.info()` fornece uma visão geral rápida da estrutura do DataFrame.

#### Informações retornadas
  - **Classe do objeto** → mostra que é um `pandas.core.frame.DataFrame`.  
  - **RangeIndex** → quantidade de linhas e intervalo de índices.  
  - **Colunas** → lista das colunas com:
  - Nome da coluna
  - Contagem de valores não nulos
  - Tipo de dado (`int64`, `float64`, `object`, etc.)
  - **Dtypes** → resumo dos tipos de dados presentes.  
  - **Memory usage** → estimativa da memória ocupada pelo DataFrame.

#### Entendimento
  ##### `df.info()` é útil para entender rapidamente:
    - Quantidade de registros e colunas.  
    - Presença de valores nulos.  
    - Tipos de dados de cada coluna.  
    - Consumo de memória.  
    
    Ideal para análise exploratória inicial antes de manipular os dados.

### Tratamento de valores ausentes
  #### NaN significa NOT a Number.
  Ele representa valores ausentes ou desconhecidos em um dataset.

### Documentação e Validação
  #### Reprodutibilidade
  Uma análise deve ser reproduzível.

    Isso significa que qualquer pessoa deve conseguir:
      - Executar o código
      - Obter os mesmos resultados

  #### Validação de Datasets
    Antes de usar um dataset, devemos verificar:
      - Valores ausentes
      - Tipos de dados
      - Consistência

### Remoção de valores ausentes

      
