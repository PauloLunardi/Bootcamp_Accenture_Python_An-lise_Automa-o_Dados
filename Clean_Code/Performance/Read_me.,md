# Redução de Complexidade e Performance em Python

## Sobre esta pasta

Esta pasta contém conteúdos, exemplos e estudos relacionados à otimização de código Python com foco em:

- Redução de complexidade
- Melhoria de performance
- Otimização de processamento
- Manipulação eficiente de dados
- Performance em análise de dados
- Escrita de código escalável

O objetivo é desenvolver soluções mais rápidas, organizadas e eficientes para projetos de automação, análise e processamento de dados.

---

## O que é complexidade?

Complexidade representa o custo computacional necessário para executar um algoritmo.

Ela normalmente é analisada em relação a:

- Tempo de execução
- Consumo de memória
- Escalabilidade

### Complexidade de tempo

A complexidade de tempo mede quanto um algoritmo cresce conforme o volume de dados aumenta.

### Big O Notation

A notação Big O é utilizada para representar a eficiência de algoritmos.

#### Exemplos comuns:

| Complexidade | Descrição |
|---|---|
| O(1) | Constante |
| O(log n) | Logarítmica |
| O(n) | Linear |
| O(n²) | Quadrática |
| O(2ⁿ) | Exponencial |

### Exemplo simples

```python
for numero in lista:
    print(numero)
```

Esse algoritmo possui complexidade:

```python
O(n)
```

Pois percorre todos os elementos da lista.

### Complexidade de memória

Refere-se à quantidade de memória utilizada pelo algoritmo durante sua execução.

Em análise de dados isso é extremamente importante devido ao grande volume de informações processadas.

---

## Performance em Python

### Objetivo

Melhorar performance significa:

- Executar código mais rápido
- Consumir menos memória
- Reduzir processamento desnecessário
- Escalar aplicações

### Boas práticas de otimização

#### Recomendações

- Evitar loops desnecessários
- Reutilizar variáveis
- Utilizar estruturas eficientes
- Reduzir operações repetidas
- Processar apenas dados necessários
- Evitar consultas excessivas
- Trabalhar com vetorização

### Estruturas de dados eficientes

A escolha da estrutura impacta diretamente a performance.

| Estrutura | Melhor uso |
|---|---|
| List | Sequências ordenadas |
| Set | Busca rápida e remoção de duplicados |
| Dict | Acesso rápido por chave |
| Tuple | Dados imutáveis |

### Exemplo com Set

```python
numeros = {1, 2, 3, 4}
```

Busca em `set` normalmente é mais rápida que em listas.

### Loops e otimização

Loops excessivos aumentam o custo computacional.

#### Exemplo menos eficiente

```python
resultado = []

for numero in numeros:
    resultado.append(numero * 2)
```

#### Exemplo otimizado

```python
resultado = [numero * 2 for numero in numeros]
```

List comprehensions costumam ser mais rápidas e legíveis.

### Funções built-in do Python

Funções internas do Python normalmente possuem melhor performance.

#### Exemplos:

- `sum()`
- `max()`
- `min()`
- `map()`
- `filter()`
- `zip()`

---

## Performance em análise de dados

### Trabalhando com grandes volumes de dados

#### Desafios comuns

- Alto consumo de memória
- Lentidão em processamento
- Gargalos em leitura de arquivos
- Operações repetitivas

### Pandas e performance

Pandas é muito utilizado em análise de dados, mas algumas práticas podem melhorar bastante a performance.

#### Boas práticas no Pandas

- Evitar loops com `iterrows()`
- Utilizar operações vetorizadas
- Filtrar dados antes de processar
- Selecionar apenas colunas necessárias
- Utilizar tipos de dados corretos

### Exemplo vetorizado

```python
df["total"] = df["quantidade"] * df["valor"]
```

Muito mais eficiente que loops linha por linha.

### NumPy e vetorização

NumPy é uma biblioteca otimizada para cálculos numéricos.

Ela permite:

- Operações rápidas
- Vetorização
- Menor consumo de memória
- Processamento eficiente

### Exemplo

```python
import numpy as np

numeros = np.array([1, 2, 3, 4])

resultado = numeros * 2
```

### Leitura eficiente de arquivos

#### Estratégias importantes

- Ler arquivos em partes
- Evitar carregar tudo em memória
- Utilizar chunks
- Processar dados gradualmente

### Exemplo com chunks

```python
import pandas as pd

for bloco in pd.read_csv(
    "dados.csv",
    chunksize=1000
):
    print(bloco)
```

---

## Banco de dados e consultas eficientes

### Reduzindo custo de consultas

Boas práticas:

- Utilizar índices
- Filtrar registros
- Evitar `SELECT *`
- Limitar resultados
- Utilizar joins corretamente

### Performance em integrações

#### APIs

- Reduzir chamadas desnecessárias
- Trabalhar com paginação
- Utilizar cache
- Processar respostas de forma eficiente

#### Automações

- Evitar abrir arquivos repetidamente
- Reduzir operações de I/O
- Utilizar processamento em lote
- Automatizar validações

---

## Profiling e análise de performance

### O que é profiling?

Profiling é o processo de identificar partes lentas do código.

### Ferramentas comuns

- `time`
- `timeit`
- `cProfile`
- `memory_profiler`

### Exemplo com time

```python
import time

inicio = time.time()

# código

fim = time.time()

print(fim - inicio)
```

### Paralelismo e concorrência

Executar tarefas simultaneamente pode melhorar performance em determinados cenários.

#### Bibliotecas comuns

- `threading`
- `multiprocessing`
- `asyncio`

### Cache e reutilização

Cache evita recalcular informações repetidas.

### Exemplo

```python
from functools import lru_cache

@lru_cache
def calcular():
    pass
```

---

## Escalabilidade e boas práticas

### O que significa escalar?

Escalar significa manter boa performance mesmo com aumento de dados ou usuários.

### Aplicações reais

#### Onde otimização é importante?

- Engenharia de dados
- Machine Learning
- APIs
- ETL
- Dashboards
- Automação
- Sistemas corporativos

### Recomendações finais

- Escrever código legível
- Medir performance antes de otimizar
- Evitar otimizações prematuras
- Priorizar clareza e eficiência
- Validar impacto das melhorias

---

## Conclusão

A redução de complexidade e otimização de performance são fundamentais para aplicações Python modernas.

Com boas práticas e ferramentas adequadas é possível criar sistemas:

- Mais rápidos
- Mais escaláveis
- Mais eficientes
- Mais econômicos em recursos

Esses conceitos são essenciais principalmente em projetos de:

- Automação
- Engenharia de dados
- Ciência de dados
- Processamento de grandes volumes
- Integrações
- APIs
