CREATE TYPE Etat AS ENUM ('neuf','bon','abime','perdu');

CREATE TABLE Ressource(
 code_unique INT PRIMARY KEY,
 titre VARCHAR NOT NULL,
 date_apparition DATE NOT NULL,
 editeur VARCHAR NOT NULL,
 genre VARCHAR NOT NULL,
 code_classification INT NOT NULL
 );

CREATE TYPE Role AS ENUM ('auteur','realisateur','acteur','compositeur','interprete');


CREATE TABLE Contributeur(
 id INT PRIMARY KEY,
 nom VARCHAR NOT NULL,
 prenom VARCHAR NOT NULL,
 ddn DATE ,
 nationalite VARCHAR
);

CREATE TABLE Ressource_Contributeur(
 role Role,
 ressource_code INT,
 id_contributeur INT,
 FOREIGN KEY(ressource_code) REFERENCES Ressource(code_unique),
 FOREIGN KEY(id_contributeur) REFERENCES Contributeur(id),
 PRIMARY KEY(ressource_code,id_contributeur)

);

CREATE TABLE Exemplaire(
  id INT PRIMARY KEY,
  ressource_code INT,
  etat Etat,
  disponible INT,
  CHECK(disponible=0 OR disponible=1),
  FOREIGN KEY(ressource_code)REFERENCES Ressource(code_unique)
);

CREATE TABLE Livre(
  isbn INT PRIMARY KEY,
  resume VARCHAR,
  langue VARCHAR,
  auteur_id INT NOT NULL,
  FOREIGN KEY(auteur_id) REFERENCES Contributeur(id)
)inherits(Ressource);

CREATE TABLE Film(
  langue VARCHAR,
  duree  INTERVAL,
  synopsis  VARCHAR,
  realisateur_id INT NOT NULL,
  acteur_id  INT NOT NULL,
  FOREIGN KEY(realisateur_id) REFERENCES Contributeur(id),
  FOREIGN KEY(acteur_id) REFERENCES Contributeur(id)
)inherits(Ressource);

CREATE TABLE Musique(
 duree INTERVAL,
 compositeur_id INT NOT NULL,
 interprete_id INT NOT NULL,
 FOREIGN KEY(compositeur_id) REFERENCES Contributeur(id),
 FOREIGN KEY(interprete_id) REFERENCES Contributeur(id)
)inherits(Ressource);

CREATE TABLE Compte(
  login VARCHAR,
  mdp VARCHAR NOT NULL
);

CREATE TABLE Compte_Adherent(
  PRIMARY KEY(login)
)inherits(Compte);

CREATE TABLE Compte_Personnel(
  PRIMARY KEY(login)
)inherits(Compte);

CREATE TABLE Adherent(
  secu VARCHAR PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  adresse VARCHAR,
  email VARCHAR,
  ddn DATE,
  telephone INT,
  etat INT NOT NULL,
  login_adherent VARCHAR UNIQUE NOT NULL,
  FOREIGN KEY(login_adherent) REFERENCES Compte_Adherent(login),
  CHECK(etat=0 OR etat=1)
);

CREATE VIEW Histoire as
select distinct A.nom,A.prenom,R.titre,E.id,P.date_pret,P.duree
from Adherent as A
join Pret as P on A.login_adherent=P.compte_adherent
join Exemplaire as E on P.id_exemplaire=E.id
join Ressource as R on E.ressource_code=R.code_unique


CREATE TABLE Personnel(
  secu VARCHAR PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  adresse VARCHAR,
  email VARCHAR,
  login_personnel VARCHAR UNIQUE NOT NULL,
  FOREIGN KEY(login_personnel) REFERENCES Compte_Personnel(login)
);

CREATE TABLE Pret(
  compte_adherent VARCHAR,
  id_exemplaire INT,
  date_pret DATE,
  duree INTERVAL,
  FOREIGN KEY(compte_adherent) REFERENCES Adherent(login_adherent),
  FOREIGN KEY(id_exemplaire) REFERENCES Exemplaire(id)
);
