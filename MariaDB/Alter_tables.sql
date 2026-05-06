"Alter Tables utilizando durante a manipulaçãop do banco"

-- Adicionando o id como chave primaria(msm após inserts)
ALTER TABLE Bootcamp_Accenture.usuarios
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Ajustar tabela destinos
ALTER TABLE Bootcamp_Accenture.destinos
ADD PRIMARY KEY (id);

-- criar as FKs
ALTER TABLE Bootcamp_Accenture.reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES Bootcamp_Accenture.usuarios(id);

ALTER TABLE Bootcamp_Accenture.reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino) REFERENCES Bootcamp_Accenture.destinos(id);

-- alterar as FKs adicionando Cascade (delete e update)
ALTER TABLE Bootcamp_Accenture.reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario) REFERENCES Bootcamp_Accenture.usuarios(id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE Bootcamp_Accenture.reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino) REFERENCES Bootcamp_Accenture.destinos(id)
ON DELETE CASCADE
ON UPDATE CASCADE;

"Remodelando os campos da tabela usuarios"
-- Adicionando e removendo campos.
  -- Sugestão: usar id_endereco_user e criar uma outra tabela para armazenar as infomações de endereço vinculado pelo id
ALTER TABLE usuarios
	ADD rua VARCHAR(100),
	ADD numero VARCHAR(10),
  ADD cidade VARCHAR(50),
  ADD estado VARCHAR(20),
	DROP COLUMN endereco;

-- Correção do nome "estado" que tinha ficado em caixa alta
ALTER TABLE Bootcamp_Accenture.usuarios CHANGE ESTADO estado VARCHAR(20);
-- ou use
ALTER TABLE Bootcamp_Accenture.usuarios RENAME COLUMN ESTADO TO estado;


