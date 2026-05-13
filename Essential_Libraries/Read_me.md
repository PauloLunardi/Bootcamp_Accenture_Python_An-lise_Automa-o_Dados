# Essential Libraries em Python

Esta pasta reúne exemplos e explicações sobre as bibliotecas essenciais do Python, utilizadas em projetos de integração, análise de dados e desenvolvimento de aplicações.

---

## 📌 Objetivo
- Demonstrar como importar e utilizar bibliotecas fundamentais.  
- Mostrar casos práticos de uso em diferentes contextos.  
- Servir como referência rápida para estudo e consulta.

---

## 📚 Bibliotecas abordadas

### 1. [os](ca://s?q=Explicar_biblioteca_os_em_Python)
- Manipulação de arquivos e diretórios.  
- Acesso a variáveis de ambiente.  
- Execução de comandos do sistema.

### 2. [sys](ca://s?q=Explicar_biblioteca_sys_em_Python)
- Interação com o interpretador Python.  
- Controle de argumentos de linha de comando.  
- Gerenciamento de módulos e saída do programa.

### 3. [math](ca://s?q=Explicar_biblioteca_math_em_Python)
- Funções matemáticas básicas e avançadas.  
- Operações com números, trigonometria e logaritmos.

### 4. [datetime](ca://s?q=Explicar_biblioteca_datetime_em_Python)
- Manipulação de datas e horários.  
- Cálculo de intervalos de tempo.  
- Formatação e conversão de datas.

### 5. [json](ca://s?q=Explicar_biblioteca_json_em_Python)
- Leitura e escrita de dados em formato JSON.  
- Conversão entre objetos Python e JSON.  
- Integração com APIs.

---

## ⚙️ Introdução às bibliotecas de dados
Python possui muitas bibliotecas para trabalhar com dados.

  ### As três bibliotecas mais utilizadas são:
- NumPy - computação numérica e arrays.  
- Pandas - Manipulação de dados em tabelas.  
- Matplotlib - criação de gráficos.  

## ⚙️ O que é NumPy?
Numpy é uma biblioteca usada para trabalhar com arrays e operações matemática eficientes.
Ela é muito mais rápida que listas comuns do Python para operarações numéricas.

## ⚙️ O que é Pandas?
Pandas é usado para manipular dados estruturados, como tabelas.
A principal estrutura de dados é o DataFrame, que funciona como uma planilha.

### Resumo do df.describe() em Pandas
  O método `df.describe()` gera estatísticas descritivas para colunas numéricas do DataFrame.  
  
#### Exemplo de saída para a coluna **preco**:

    | Métrica | Explicação |
    |---------|------------|
    | **count** | Número de valores não nulos (quantos registros foram considerados). |
    | **mean** | Média aritmética dos valores. |
    | **std** | Desvio padrão, mostra a dispersão dos dados em relação à média. |
    | **min** | Valor mínimo encontrado na coluna. |
    | **25%** | Primeiro quartil (25% dos dados estão abaixo deste valor). |
    | **50%** | Mediana (metade dos dados estão abaixo e metade acima). |
    | **75%** | Terceiro quartil (75% dos dados estão abaixo deste valor). |
    | **max** | Valor máximo encontrado na coluna. |

### 📖 Conclusão
- `df.describe()` é útil para ter uma visão rápida da distribuição dos dados.  
- Ele mostra **tendência central** (mean, median), **dispersão** (std, quartis) e **extremos** (min, max).  
- Ideal para análise exploratória inicial de datasets numéricos.

## ⚙️ O que é Matplotlib?
Matplotlib é uma biblioteca usada pareea criar graficos e visualizações de dados.

## 📖 Conclusão
Essas bibliotecas são a base para trabalhar com **arquivos, sistema operacional, cálculos, datas e formatos de dados**.  
Dominar essas ferramentas é essencial para qualquer desenvolvedor Python que queira evoluir em projetos reais.
