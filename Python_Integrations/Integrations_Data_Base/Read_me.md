# Integração com SQLite em Python

Além de transformar dados obtidos em API em arquivos, podemos também armazenar em bancos de dados.

Um banco de dados permite:

- Armazenar grandes volumes de informações
- Organizar dados em tabelas
- Consultar dados rapidamente

Em Python podem ser usados diversos bancos de dados.  
Aqui no curso será utilizado o **SQLite**, que é leve, simples e não precisa de servidor.

---

# Comandos importantes

## `commit()`

Confirma alterações realizadas no banco de dados.

Usado após comandos como:

- INSERT
- UPDATE
- DELETE
- CREATE
- DROP

Exemplo:

```python
conexao.commit()
```

---

## `close()`

Fecha a conexão com o banco e libera o arquivo.

Exemplo:

```python
conexao.close()
```

---

## `cursor.close()`

Encerra o cursor explicitamente.

Boa prática, mas não obrigatório.

Exemplo:

```python
cursor.close()
```

---

# Diferença entre modos de leitura

## 1. `fetchall()`

```python
cursor.execute("SELECT * FROM usuarios_vip")

dados = cursor.fetchall()

print(dados)
```

Os dados são carregados todos de uma vez em memória e retornados como uma lista de tuplas.

### ✅ Vantagens

- Simples de usar
- Todos os resultados ficam disponíveis imediatamente

### ❌ Desvantagens

- Pode consumir muita memória em tabelas grandes

---

## 2. Iterar diretamente no cursor

```python
cursor.execute("SELECT * FROM usuarios_vip")

for linha in cursor:
    print(linha)
```

O cursor entrega os dados linha por linha conforme a iteração acontece.

### ✅ Vantagens

- Mais eficiente para grandes volumes de dados
- Não carrega tudo em memória

### ❌ Desvantagens

- O cursor só pode ser percorrido uma vez
- Se quiser reutilizar os dados, precisa armazená-los manualmente

---

## 3. `fetchmany(n)`

```python
cursor.execute("SELECT * FROM usuarios_vip")

for bloco in cursor.fetchmany(2):
    print(bloco)
```

Os dados são lidos em blocos de N linhas por vez.

### ✅ Vantagens

- Equilíbrio entre desempenho e simplicidade
- Bom para tabelas grandes

### ❌ Desvantagens

- Necessário definir o tamanho do bloco
- Exige mais controle da leitura

---

# Comparativo dos métodos

| Método | Como funciona | Vantagem principal | Desvantagem principal |
|---|---|---|---|
| `fetchall()` | Carrega todas as linhas em memória | Simples e ótimo para tabelas pequenas | Pode consumir muita memória |
| Iteração no cursor | Lê linha por linha diretamente | Mais eficiente para tabelas grandes | Só percorre uma vez |
| `fetchmany(n)` | Lê blocos de N linhas por vez | Controle sobre quantidade lida | Precisa definir o tamanho do bloco |

---

# Conclusão

## Quando usar `fetchall()`

Use quando:

- a tabela for pequena
- você precisar de todos os dados de uma vez

---

## Quando iterar diretamente no cursor

Use quando:

- estiver trabalhando com tabelas grandes
- quiser economizar memória

---

## Quando usar `fetchmany(n)`

Use quando:

- precisar de um meio-termo
- quiser controlar quantas linhas serão carregadas por vez

---

# Resumo Final

| Situação | Método recomendado |
|---|---|
| Poucos dados | `fetchall()` |
| Muitos dados | Iteração no cursor |
| Controle de blocos | `fetchmany(n)` |
