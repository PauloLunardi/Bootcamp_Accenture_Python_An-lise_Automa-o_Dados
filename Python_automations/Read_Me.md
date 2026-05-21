# Automação de Processos e Análises com Python

## Introdução à automação

### Conceito de Automação

Automação é o processo de executar tarefas automaticamente utilizando programas e scripts.

Em vez de realizar tarefas manualmente, criamos aplicações que executam essas atividades de forma automática, repetitiva e organizada.

Isso permite:

- Economizar tempo
- Reduzir erros humanos
- Processar grandes volumes de dados
- Aumentar produtividade
- Padronizar processos

Python é uma das linguagens mais utilizadas para automação devido à sua simplicidade, legibilidade e vasta quantidade de bibliotecas.

---

### Cenários reais de automação

#### A automação é utilizada em diversas áreas:

- Geração automática de relatórios
- Coleta de dados na internet
- Processamento diário de arquivos
- Atualização de bancos de dados
- Monitoramento de sistemas
- Envio automático de e-mails
- Integração entre APIs
- Rotinas empresariais automatizadas

#### Exemplos práticos:

- Empresas automatizam relatórios financeiros diariamente
- Sistemas monitoram servidores automaticamente
- Scripts processam milhares de arquivos em segundos
- APIs fornecem dados em tempo real para aplicações

---

## Manipulação automatizada de arquivos

### Processamento automático de arquivos

Uma das automações mais comuns é o processamento automático de arquivos.

Com Python podemos:

- Ler arquivos automaticamente
- Modificar conteúdos
- Organizar documentos
- Gerar novos arquivos
- Processar grandes volumes de dados

---

### Exemplos de automação com arquivos

#### Por exemplo:

- Ler arquivos CSV
- Processar planilhas Excel
- Calcular métricas automaticamente
- Gerar relatórios
- Organizar arquivos em pastas
- Renomear arquivos em massa
- Criar backups automáticos

---

### Bibliotecas utilizadas

Python possui bibliotecas muito utilizadas para manipulação de arquivos:

- `os`
- `pathlib`
- `shutil`
- `csv`
- `pandas`
- `openpyxl`

Essas bibliotecas permitem trabalhar com arquivos e diretórios de forma prática e automatizada.

---

## Integração com APIs e Bancos

### O que são APIs?

APIs (Application Programming Interface) permitem que sistemas diferentes se comuniquem.

Com APIs podemos:

- Buscar dados externos
- Enviar informações
- Integrar sistemas
- Automatizar consultas

---

### Exemplos de uso de APIs

#### Algumas aplicações comuns:

- Consultar cotações de moedas
- Buscar dados climáticos
- Consumir APIs de redes sociais
- Integrar sistemas empresariais
- Consultar dados financeiros

---

### Integração com bancos de dados

Além de APIs, sistemas automatizados normalmente utilizam bancos de dados para armazenar informações.

Os bancos de dados permitem:

- Armazenar dados de forma organizada
- Realizar consultas rápidas
- Atualizar informações automaticamente
- Manter histórico de dados

Python pode se integrar com diversos bancos:

- SQLite
- MySQL
- PostgreSQL
- SQL Server
- Oracle

---

## Criação de tabelas utilizando cursor

### O que é um cursor?

O cursor é um objeto utilizado para executar comandos SQL dentro do banco de dados.

Com ele podemos:

- Criar tabelas
- Inserir registros
- Atualizar dados
- Remover informações
- Realizar consultas

---

### Exemplo de criação de tabela

```python
import sqlite3

conexao = sqlite3.connect("empresa.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    salario REAL
)
""")

conexao.commit()

conexao.close()
```

---

### Explicação do exemplo

#### O código realiza as seguintes etapas:

1. Cria conexão com o banco SQLite
2. Cria um cursor para executar SQL
3. Cria a tabela `funcionarios`
4. Confirma as alterações com `commit()`
5. Fecha a conexão com o banco

---

## Agendamentos de tarefas

### Scripts programados

Em sistemas reais, scripts podem ser executados automaticamente em horários específicos.

Isso permite:

- Automatizar rotinas diárias
- Executar backups
- Atualizar relatórios automaticamente
- Monitorar sistemas continuamente

---

### Cron Jobs

Em sistemas Linux utilizamos cron jobs para agendar tarefas automáticas.

---

### Exemplo de agendamento

#### Executar um script todos os dias às 08h:

```bash
0 8 * * * python scheduled_script.py
```

---

### Fluxo real de automação

#### Etapas comuns:

1. Criar o script Python
2. Testar o funcionamento manualmente
3. Configurar o cron job no servidor
4. Monitorar execuções automáticas
5. Registrar logs de execução

---

### Exemplo prático

#### Estrutura:

```bash
python scheduled_script.py
```

#### Cron job:

```bash
0 8 * * * python scheduled_script.py
```

O sistema executará automaticamente o script todos os dias às 08:00.

---

## Monitoramento

### Importância do monitoramento

Quando automatizamos processos, precisamos acompanhar se os scripts estão funcionando corretamente.

O monitoramento permite:

- Identificar erros rapidamente
- Evitar falhas em processos críticos
- Garantir estabilidade da automação
- Registrar execuções

---

### Logs

Uma das formas mais comuns de monitoramento é utilizando logs.

Logs registram:

- Horário de execução
- Erros encontrados
- Processos concluídos
- Informações importantes do sistema

---

### Exemplo simples de log

```python
with open("log.txt", "a") as arquivo:
    arquivo.write("Script executado com sucesso\n")
```

---

## Projeto prático de automação

### O que é um pipeline de dados?

Um pipeline de dados é um processo automatizado que executa várias etapas de processamento de informações.

---

### Etapas de um pipeline

#### Normalmente um pipeline executa:

1. Coleta de dados
2. Processamento dos dados
3. Limpeza das informações
4. Armazenamento dos dados
5. Análise dos dados
6. Geração de insights e resultados

---

### Onde pipelines são utilizados

Pipelines são muito utilizados em:

- Análise de dados
- Engenharia de dados
- Relatórios automáticos
- Business Intelligence (BI)
- Sistemas corporativos
- Machine Learning

---

### Exemplo de pipeline automatizado

#### Fluxo simplificado:

1. Buscar dados de uma API
2. Processar os dados com Python
3. Armazenar em banco SQLite
4. Gerar relatório automático
5. Agendar execução diária

---

### Benefícios de pipelines automatizados

#### Algumas vantagens:

- Redução de trabalho manual
- Processamento rápido de dados
- Menor índice de erros
- Escalabilidade
- Atualização automática de informações

---

## Conclusão

A automação com Python permite criar soluções capazes de executar tarefas repetitivas de forma rápida, eficiente e organizada.

Com integração entre:

- APIs
- Bancos de dados
- Arquivos
- Agendamentos automáticos

é possível desenvolver sistemas completos de automação e análise de dados.

Python se destaca por:

- Facilidade de aprendizado
- Grande quantidade de bibliotecas
- Flexibilidade
- Alto poder de automação

Por isso, é amplamente utilizado em:

- Engenharia de dados
- Automação de processos
- Desenvolvimento de sistemas
- Ciência de dados
- Business Intelligence
