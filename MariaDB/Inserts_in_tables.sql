"Inserts na tabela USUARIOS" 

INSERT INTO Bootcamp_Accenture.usuarios(id, nome, email, data_nasc, endereco) 
VALUES (1, "Paulo Lunardi", "Teste@teste.com", "1992-10-04", "Av das Aves, 100 - Bairro Alto Matão/SP"); 

INSERT INTO Bootcamp_Accenture.usuarios(id, nome, email, data_nasc, endereco) 
VALUES (2, "Maria Oliveira", "maria.oliveira@email.com", "1988-03-12", "Rua das Flores, 250 - Centro/SP");

INSERT INTO Bootcamp_Accenture.usuarios(id, nome, email, data_nasc, endereco) 
VALUES (3, "Lucas Fernandes", "lucas.fernandes@email.com", "1995-07-22", "Av Brasil, 1450 - Jardim Paulista/SP");

INSERT INTO Bootcamp_Accenture.usuarios(id, nome, email, data_nasc, endereco) 
VALUES (4, "Ana Souza", "ana.souza@email.com", "1990-11-05", "Rua das Palmeiras, 78 - Vila Mariana/SP");

INSERT INTO Bootcamp_Accenture.usuarios(id, nome, email, data_nasc, endereco) 
VALUES (5, "Pedro Gonçalves", "pedro.goncalves@email.com", "1985-01-30", "Av Independência, 500 - Campinas/SP");

INSERT INTO Bootcamp_Accenture.usuarios(id, nome, email, data_nasc, endereco) 
VALUES (6, "Camila Ribeiro", "camila.ribeiro@email.com", "1998-09-14", "Rua Bela Vista, 320 - Sorocaba/SP");


"Inserts na tabela DESTINOS" 

INSERT INTO Bootcamp_Accenture.destinos(id, nome, descricao) 
VALUES (1, "Rio de Janeiro", "Cidade maravilhosa com praias e pontos turísticos famosos");

INSERT INTO Bootcamp_Accenture.destinos(id, nome, descricao) 
VALUES (2, "São Paulo", "Centro financeiro e cultural do Brasil");

INSERT INTO Bootcamp_Accenture.destinos(id, nome, descricao) 
VALUES (3, "Salvador", "Capital da Bahia, conhecida pelo carnaval e cultura afro-brasileira");

INSERT INTO Bootcamp_Accenture.destinos(id, nome, descricao) 
VALUES (4, "Florianópolis", "Ilha com belas praias e vida noturna agitada");

INSERT INTO Bootcamp_Accenture.destinos(id, nome, descricao) 
VALUES (5, "Foz do Iguaçu", "Cidade famosa pelas Cataratas do Iguaçu");


"Inserts na tabela RESERVAS" 

INSERT INTO Bootcamp_Accenture.reservas(id, id_usuario, id_destino, data, status) 
VALUES (1, 2, 1, "2026-06-15", "Confirmada");

INSERT INTO Bootcamp_Accenture.reservas(id, id_usuario, id_destino, data, status) 
VALUES (2, 3, 2, "2026-07-10", "Pendente");

INSERT INTO Bootcamp_Accenture.reservas(id, id_usuario, id_destino, data, status) 
VALUES (3, 4, 3, "2026-08-05", "Cancelada");

INSERT INTO Bootcamp_Accenture.reservas(id, id_usuario, id_destino, data, status) 
VALUES (4, 5, 4, "2026-09-20", "Confirmada");

INSERT INTO Bootcamp_Accenture.reservas(id, id_usuario, id_destino, data, status) 
VALUES (5, 6, 5, "2026-10-02", "Pendente");

