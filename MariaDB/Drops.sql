"Drops utilizados curante o processo"

"Erro gerado ao dropar uma fk, ao tentar criar outra ela impede, pois cria um registro de index e recria-la antes de remover o registro gerra erro"
-- Dropar a constraint antiga (não o índice):

-- Para fk_reservas_usuarios
ALTER TABLE Bootcamp_Accenture.reservas 
DROP FOREIGN KEY fk_reservas_usuarios;
-- Para fk_reservas_destinos
ALTER TABLE Bootcamp_Accenture.reservas 
DROP FOREIGN KEY fk_reservas_destinos;

-- Dropar o indice contendo registro da fk(erro gerado por uma das tentativas)

-- Para fk_reservas_usuarios
ALTER TABLE Bootcamp_Accenture.reservas DROP INDEX fk_reservas_usuarios;
-- Para fk_reservas_destinos
ALTER TABLE Bootcamp_Accenture.reservas DROP INDEX fk_reservas_destinos;
