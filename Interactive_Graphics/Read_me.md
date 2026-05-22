# Visualização de Dados com Python

## Introdução à visualização de dados

### O que é visualização de dados?

Visualização de dados é o processo de representar informações de forma gráfica para facilitar análises, interpretações e tomada de decisões.

Com gráficos conseguimos:

- Identificar padrões
- Detectar tendências
- Comparar informações
- Facilitar análises
- Melhorar apresentações de dados

A visualização é uma das etapas mais importantes da análise de dados.

---

## Bibliotecas de visualização em Python

### Principais bibliotecas

Python possui diversas bibliotecas para criação de gráficos e dashboards.

As mais utilizadas são:

- Matplotlib
- Seaborn
- Plotly

Cada uma possui características e objetivos diferentes.

---

## Matplotlib

### O que é Matplotlib?

Matplotlib é uma das bibliotecas de visualização mais utilizadas no Python.

Ela permite criar:

- Gráficos de linha
- Barras
- Dispersão
- Histogramas
- Pizza
- Subplots

É considerada a base da visualização de dados em Python.

### Instalação

```bash
pip install matplotlib
```

### Importação

```python
import matplotlib.pyplot as plt
```

### Exemplo simples

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.show()
```

### Principais funções

- `plt.plot()`
- `plt.bar()`
- `plt.scatter()`
- `plt.hist()`
- `plt.pie()`
- `plt.title()`
- `plt.xlabel()`
- `plt.ylabel()`

---

## Seaborn

### O que é Seaborn?

Seaborn é uma biblioteca construída sobre o Matplotlib.

Seu foco é criar gráficos:

- Mais modernos
- Mais bonitos visualmente
- Estatísticos
- Mais simples de configurar

É muito utilizada em análise exploratória de dados.

### Instalação

```bash
pip install seaborn
```

### Importação

```python
import seaborn as sns
```

### Exemplo simples

```python
import seaborn as sns
import matplotlib.pyplot as plt

dados = [10, 20, 30, 40]

sns.lineplot(x=[1, 2, 3, 4], y=dados)

plt.show()
```

### Gráficos populares no Seaborn

- `lineplot()`
- `barplot()`
- `histplot()`
- `boxplot()`
- `heatmap()`
- `pairplot()`

### Vantagens do Seaborn

- Visual moderno
- Menos código
- Melhor integração com Pandas
- Gráficos estatísticos avançados

---

## Plotly

### O que é Plotly?

Plotly é uma biblioteca focada em gráficos interativos.

Com Plotly podemos criar:

- Dashboards
- Gráficos interativos
- Visualizações modernas
- Análises dinâmicas

Muito utilizado em:

- Business Intelligence
- Dashboards Web
- Ciência de Dados
- Aplicações analíticas

### Instalação

```bash
pip install plotly
```

### Importação

```python
import plotly.express as px
```

### Exemplo simples

```python
import plotly.express as px

grafico = px.line(
    x=[1, 2, 3, 4],
    y=[10, 20, 30, 40]
)

grafico.show()
```

### Recursos do Plotly

- Interatividade
- Zoom
- Hover em gráficos
- Exportação HTML
- Dashboards
- Integração Web


## Comparação entre bibliotecas

| Biblioteca | Característica principal |
|---|---|
| Matplotlib | Base da visualização em Python |
| Seaborn | Visual estatístico e moderno |
| Plotly | Gráficos interativos |

---

## Tipos de gráficos

### Gráfico de linha

Utilizado para:

- Tendências
- Séries temporais
- Evolução de dados

### Gráfico de barras

Utilizado para:

- Comparações
- Rankings
- Categorias

### Histograma

Utilizado para:

- Distribuição de dados
- Frequência
- Análise estatística

### Scatter Plot

Utilizado para:

- Correlação
- Relação entre variáveis
- Identificação de padrões
---

## Personalização de gráficos

### Elementos importantes

Podemos personalizar:

- Título
- Eixos
- Cores
- Legendas
- Tamanho da figura
- Estilo visual

### Exemplo de personalização

```python
plt.title("Vendas Mensais")

plt.xlabel("Meses")

plt.ylabel("Vendas")
```
---

## Integração com Pandas

### Visualização com DataFrames

As bibliotecas de visualização funcionam muito bem com Pandas.

Exemplo:

```python
import pandas as pd

df = pd.read_csv("dados.csv")
```

Os dados podem ser utilizados diretamente nos gráficos.

---

## Boas práticas

### Recomendações

- Utilizar títulos claros
- Evitar excesso de informação
- Escolher o gráfico correto
- Destacar informações importantes
- Manter consistência visual

---

## Aplicações reais

### Onde a visualização de dados é utilizada?

- Business Intelligence
- Relatórios executivos
- Dashboards
- Ciência de Dados
- Machine Learning
- Engenharia de Dados
- Sistemas corporativos

---

## Storytelling com dados
Storytelling com dados significa usar visualizações para contar uma história.
O objetivo não é apenas mostrar gráficos, mas comunicar insights.

Um bom sttorytelling deve:
    * Mostrar o contexto
    * destacar padrões
    * explicar os resultados

---

## Conclusão

A visualização de dados é fundamental para transformar informações em análises compreensíveis.

Com Python e bibliotecas como:

- Matplotlib
- Seaborn
- Plotly

é possível criar gráficos profissionais, interativos e eficientes para análise e apresentação de dados.
