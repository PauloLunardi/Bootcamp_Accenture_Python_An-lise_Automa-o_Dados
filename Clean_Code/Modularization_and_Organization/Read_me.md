# Modularização e Organização em Python

## Introdução
A modularização é essencial para manter o código limpo e organizado.  
Em projetos Python que envolvem **bancos de dados** ou **automações**, separar responsabilidades em módulos e arquivos distintos facilita a manutenção, a reutilização e a escalabilidade.

## Boas práticas
- **[Separar responsabilidades](ca://s?q=Separar_responsabilidades_em_Python)**: cada módulo deve ter uma função clara (ex.: conexão com banco, utilidades, automação).  
- **[Nomes descritivos](ca://s?q=Nomes_descritivos_em_Python)**: arquivos e funções devem indicar sua finalidade.  
- **[Consistência](ca://s?q=Consistencia_em_Python)**: seguir padrões de estilo como PEP8.  
- **[Documentação](ca://s?q=Documentacao_em_Python)**: comentários e docstrings ajudam na compreensão.  

## Exemplo de Estrutura de Pastas
Uma organização simples pode ser feita assim:

|
|-src/                # pasta principal do código
||-main.py            # ponto de entrada do programa
||-utils.py           # funções auxiliares e utilitários
||-banco.py           # funções de conexão e manipulação de banco de dados
||-automacao.py       # scripts de automação (envio de e-mails, tarefas recorrentes)


## Exemplo prático
```python
# utils.py
def formatar_valor(valor):
    return f"R$ {valor:.2f}"

# banco.py
def conectar_banco():
    # lógica de conexão
    pass

# automacao.py
def enviar_relatorio():
    # lógica de envio automático
    pass

# main.py
from banco import conectar_banco
from automacao import enviar_relatorio

conectar_banco()
enviar_relatorio()

