# Testes em Python

## Sobre esta pasta

Esta pasta contém materiais, exemplos e estudos relacionados a testes em Python, com foco em:

- Testes unitários
- Validação de integrações
- Testes de APIs
- Testes de processamento de dados
- Garantia de qualidade em automações

O objetivo é validar comportamentos, identificar erros e garantir estabilidade nas aplicações.

---

## Estrutura do conteúdo

```bash
testes/
│
├── unitarios/
├── integracoes/
├── dados/
├── mocks/
├── fixtures/
└── exemplos/
```

---

## O que são testes?

Testes são procedimentos utilizados para verificar se uma aplicação está funcionando corretamente.

Eles ajudam a:

- Detectar erros
- Validar regras de negócio
- Evitar falhas futuras
- Garantir estabilidade
- Facilitar manutenção do código

---

# Testes Unitários

## O que são?

Testes unitários validam pequenas partes isoladas do sistema, normalmente:

- Funções
- Métodos
- Classes

O objetivo é verificar se cada unidade do código funciona corretamente de forma independente.

---

## Exemplo simples

```python
def soma(a, b):
    return a + b
```

### Teste:

```python
def test_soma():
    assert soma(2, 3) == 5
```

---

## Principais características

- Testam pequenas partes do sistema
- São rápidos
- Possuem baixo custo
- Facilitam refatorações
- Ajudam na manutenção do código

---

## Frameworks utilizados

### Principais bibliotecas:

- `unittest`
- `pytest`

---

## Pytest

### Instalação

```bash
pip install pytest
```

---

### Executando testes

```bash
pytest
```

---

## Estrutura comum

```bash
tests/
│
├── test_api.py
├── test_database.py
├── test_processamento.py
└── test_utils.py
```

---

# Testes de Integração

## O que são?

Testes de integração verificam se diferentes partes do sistema funcionam corretamente juntas.

Exemplos:

- API + Banco de dados
- Sistema + Arquivos
- Aplicação + Serviços externos

---

## Objetivos

- Validar comunicação entre módulos
- Garantir fluxo correto dos dados
- Detectar falhas de integração
- Validar comportamento real do sistema

---

## Exemplos de integração

### APIs

- Requisições HTTP
- Autenticação
- Retorno JSON
- Status code

### Bancos de dados

- Inserção de dados
- Consultas SQL
- Atualizações
- Persistência

### Arquivos

- Leitura CSV
- Processamento Excel
- Geração de relatórios

---

## Exemplo de teste em API

```python
import requests

def test_api_status():

    response = requests.get(
        "https://api.exemplo.com"
    )

    assert response.status_code == 200
```

---

# Testes em Processamento de Dados

## Objetivo

Garantir que os dados estejam:

- Corretos
- Consistentes
- Sem perdas
- Dentro do formato esperado

---

## Exemplos de validação

- Valores nulos
- Duplicidades
- Tipos de dados
- Estrutura de DataFrames
- Conversões
- Regras de negócio

---

## Exemplo com Pandas

```python
import pandas as pd

def test_sem_valores_nulos():

    df = pd.read_csv("dados.csv")

    assert df.isnull().sum().sum() == 0
```

---

# Mocks e Simulações

## O que são mocks?

Mocks simulam comportamentos externos durante os testes.

São utilizados para evitar dependências reais como:

- APIs
- Bancos externos
- Serviços terceiros

---

## Benefícios

- Testes mais rápidos
- Menor dependência externa
- Mais controle dos cenários
- Facilidade de simulação

---

## Exemplo de mock

```python
from unittest.mock import patch
```

---

# Fixtures

## O que são fixtures?

Fixtures são estruturas utilizadas para preparar dados e ambientes de teste.

Elas ajudam a:

- Reutilizar código
- Padronizar cenários
- Organizar testes

---

## Exemplo com pytest

```python
import pytest

@pytest.fixture
def usuario():

    return {
        "nome": "Paulo",
        "idade": 25
    }
```

---

# Boas práticas

## Recomendações

- Criar testes pequenos
- Nomear testes claramente
- Evitar dependência entre testes
- Utilizar mocks quando necessário
- Automatizar execuções
- Validar cenários de erro
- Cobrir regras críticas

---

# Cobertura de testes

## O que é?

Cobertura mede quanto do código está sendo testado.

---

## Ferramenta comum

```bash
pip install coverage
```

---

## Executando cobertura

```bash
coverage run -m pytest
```

```bash
coverage report
```

---

# Integração contínua

## Objetivo

Executar testes automaticamente durante o desenvolvimento.

Ferramentas comuns:

- GitHub Actions
- GitLab CI/CD
- Jenkins

---

# Conclusão

Os testes são fundamentais para garantir:

- Qualidade
- Segurança
- Estabilidade
- Manutenção

Com testes unitários e de integração conseguimos validar desde pequenas funções até fluxos completos de processamento de dados e integração entre sistemas.
