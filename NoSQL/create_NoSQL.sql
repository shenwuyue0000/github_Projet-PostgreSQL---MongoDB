CREATE TABLE Ressource(
 code_unique INT PRIMARY KEY,
 titre VARCHAR NOT NULL,
 date_apparition DATE NOT NULL,
 editeur VARCHAR NOT NULL,
 genre VARCHAR NOT NULL,
 code_classification INT NOT NULL,
 type VARCHAR check(type in ('livre','film','musique')),
 detail json,
 contributeur json
);

CREATE TABLE Exemplaire(
 id INT PRIMARY KEY,
 etat VARCHAR check(etat in ('neuf','bon','abime','perdu')),
 disponibilite INT check(disponibilite=0 OR disponibilite=1),
 ressource_code INT,
 FOREIGN KEY(ressource_code) REFERENCES Ressource(code_unique)
);

