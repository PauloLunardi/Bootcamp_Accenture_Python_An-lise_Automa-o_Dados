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

