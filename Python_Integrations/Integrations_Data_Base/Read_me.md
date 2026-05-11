Integração com SQLite em Python

Além de transformar dados obtidos em API em arquivos, podemos também armazenar em bancos de dados.

Um banco de dados te permite:

Armazenar grandes volumes de informações

Organizar dados em tabelas

Consultar dados rapidamente

Em Python podem ser usados diversos bancos de dados. Aqui no curso será utilizado o SQLite, que é leve, simples e não precisa de servidor.

📌 Comandos importantes

commit() → confirma alterações (INSERT, UPDATE, DELETE, CREATE, DROP).

close() → fecha a conexão e libera o arquivo do banco.

cursor.close() → encerra o cursor explicitamente (boa prática, mas não obrigatório).

Diferença entre modos de leitura

1. fetchall()

cursor.execute("SELECT * FROM usuarios_vip")
dados = cursor.fetchall()
print(dados)

Os dados são carregados todos de uma vez em memória e retornados como uma lista de tuplas.

Vantagem: simples de usar, você já tem todos os resultados disponíveis.

Desvantagem: se a tabela tiver milhares ou milhões de registros, pode consumir muita memória.

2. Iterar direto no cursor

cursor.execute("SELECT * FROM usuarios_vip")
for linha in cursor:
    print(linha)

O cursor vai entregando linha por linha conforme você percorre.

Vantagem: mais eficiente em consultas grandes, porque não precisa carregar tudo de uma vez.

Desvantagem: só percorre uma vez; se quiser manipular depois, precisa salvar manualmente.

3. fetchmany(n)

cursor.execute("SELECT * FROM usuarios_vip")
for bloco in cursor.fetchmany(2):  # lê 2 registros por vez
    print(bloco)

Os dados são lidos em blocos de N linhas por vez.

Vantagem: equilíbrio entre simplicidade e eficiência, útil para tabelas grandes.

Desvantagem: exige definir o tamanho do bloco e controlar a iteração.

📊 Comparativo dos métodos

Método

Como funciona

Vantagem principal

Desvantagem principal

fetchall

Carrega todas as linhas em memória

Simples, ótimo para tabelas pequenas

Pode pesar em tabelas grandes

Iteração no cursor

Lê linha por linha diretamente

Mais eficiente em tabelas grandes

Só percorre uma vez

fetchmany(n)

Lê blocos de N linhas por vez

Controle sobre quantidade lida

Precisa definir tamanho do bloco

📖 Conclusão

Use fetchall para tabelas pequenas ou quando quiser todos os dados de uma vez.

Use iterar no cursor para tabelas grandes, evitando sobrecarga de memória.

Use fetchmany quando precisar de um meio-termo, controlando quantas linhas são lidas por vez.
