-- traz todos registros da tabela
SELECT * FROM usuarios;

-- conta registros na tabela usuarios
SELECT COUNT(*) FROM usuarios;

-- conta registros na tabela usuarios e  nomeia a coluna de retorno
SELECT COUNT(*) AS total_users FROM usuarios;

-- Retorna a qtd de usuarios onde ambos esstão nas 2 tabelas
SELECT COUNT(*) AS total_users FROM usuarios u
  INNER JOIN reservas r
  ON (u.id = r.id_usuario);

-- Qual é a maior idade d e um usuario
SELECT MAX(TIMESTAMPDIFF(YEAR, data_nasc, CURRENT_DATE())) AS Maior_Idade FROM usuarios;

-- Quantas reservas em tenho para um certo destino?
SELECT COUNT(*) AS Viagens_Total, id_destino
FROM reservas
  GROUP BY id_destino;

SELECT COUNT(*) AS qtd_reservas, id_destino
FROM reservas
  GROUP BY id_destino
  ORDER BY qtd_reservas DESC, id_destino DESC;

-- Pesquisa em indice de quantos registros possui o nome que informamos(executar novamente após a criação do index e verificar que precenhe as informações)
EXPLAIN 
  SELECT * FROM usuarios WHERE nome = "Paulo Lunardi";

-- Cria um index com referencia a coluna nome da tabela usuarios
CREATE INDEX idx_nome ON usuarios (nome);
  -- 
