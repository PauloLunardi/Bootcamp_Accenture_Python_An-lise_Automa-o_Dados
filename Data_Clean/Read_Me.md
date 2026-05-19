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

### Remoção de valores ausentes NaN
#### Tratamento de valores ausentes – Cabin

Nesta etapa, a coluna **Cabin** foi ajustada para lidar com os registros ausentes (NaN).  
Como mais de 75% dos valores estavam faltando, optamos por uma abordagem **simplista e transparente**:  
substituir todos os valores ausentes por `"Unknown"`.  

```python
# Substitui valores ausentes (NaN) da coluna "Cabin" por "Unknown"
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Verifica novamente se ainda existem valores ausentes
print(df.isnull().sum())
```

### Considerações adicionais sobre limpeza de dados

#### Importância da documentação
Cada etapa de limpeza deve ser registrada de forma clara.  
  
    Isso garante que qualquer pessoa que consulte o repositório entenda:
    - Qual foi o problema identificado.  
    - Qual técnica foi aplicada para resolver.  
    - Qual o impacto esperado no dataset.  

#### Boas práticas
- **Consistência** → manter o mesmo padrão de tratamento para colunas semelhantes.  
- **Transparência** → sempre indicar quando valores foram substituídos por categorias como `"Unknown"`.  
- **Reprodutibilidade** → incluir exemplos de código e saídas esperadas (`df.isnull().sum()`) para validar.  

#### Próximos passos
Após a limpeza inicial:
  - Verificar se ainda existem valores ausentes em outras colunas.  
  - Avaliar se há necessidade de normalização ou padronização adicional.  
  - Preparar o dataset para análise exploratória ou modelagem preditiva.  

### Conclusão
Com as etapas documentadas, o dataset agora está:
  - Livre de valores ausentes críticos.  
  - Mais consistente e confiável para análises.  
  - Pronto para ser utilizado em estudos exploratórios ou em modelos de machine learning.  

👉 Essa organização por tópicos e subtópicos (`###` e `####`) facilita a leitura e deixa claro o fluxo de operações realizadas.

