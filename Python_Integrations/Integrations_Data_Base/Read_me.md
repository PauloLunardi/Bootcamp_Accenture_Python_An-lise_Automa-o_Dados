# Integração de banco de dados 

Além de tranformar dados obtido em API emm arquivo, podemos também armazenar em bancos de dados.

Um bando de dados te permite:
  - Armazenar grandes volume de dados(informações)
  - Organizar dados em tabelas
  - Consultar dados rapidamente

    Em Python pode se usar diversos bancos de dados.

    Aqui no curso sera utilizado o SQLite

### Explicativos sobre comandos 

    commit() → serve para confirmar alterações (INSERT, UPDATE, DELETE, CREATE, DROP).
  
    close() → fecha a conexão e libera o arquivo do banco.
  
    cursor.close() → encerra o cursor explicitamente (boa prática, mas não obrigatório).

## Diferença entre fetchall() e iterar direto no cursor

### fetchall(): carrega todas as linhas de uma vez em memória e devolve uma lista.

    Vantagem: simples de usar, você já tem todos os resultados disponíveis.

    Desvantagem: se a tabela tiver milhares ou milhões de registros, isso pode consumir muita memória de uma vez.

### Iterar direto no cursor (for linha in cursor:): o cursor vai entregando linha por linha conforme você percorre.

    Vantagem: mais eficiente em consultas grandes, porque não precisa carregar tudo de uma vez.

    Desvantagem: você só consegue percorrer uma vez; se quiser manipular depois, precisa armazenar manualmente.
