CREATE TABLE Bootcamp_Accenture.usuarios(
    id INT,
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuario',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuario',
    endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do usuário',
    data_nasc DATE NOT NULL COMMENT 'Data de Nascimento do usuario'
);

CREATE TABLE Bootcamp_Accenture.destinos(
    id INT,
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do destino',
    descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

CREATE TABLE Bootcamp_Accenture.reservas(
    id INT COMMENT 'Identificador único da reserva',
    id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva',
    id_destino INT COMMENT ' Referência ao ID do destino da reserva',
    data DATE COMMENT 'Data da reserva',
    status VARCHAR(255) DEFAULT 'Pendente' COMMENT 'Staus da reserva (Confirmada, Pendente, Cancelada, etc,)'
);

CREATE TABLE Bootcamp_Accenture.usuarios_new(
    id INT,
    nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuario',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuario',
    endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do usuário',
    data_nasc DATE NOT NULL COMMENT 'Data de Nascimento do usuario'
);
