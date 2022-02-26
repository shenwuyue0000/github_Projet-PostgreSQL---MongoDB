INSERT INTO Ressource VALUES(1,'le petit prince','1943-04-06',
  'Gallimard Jeunesse','le conte pour enfants',1,'livre',
  '[
    {
      "isbn":978314046,
      "resume": "Le petit prince...",
      "langue":"francaise"
    }
  ]' , 
  '[
    {
      "role":"auteur",
      "id":1,
      "nom":"Antoine de",
      "prenom":"Saint-Exupery",
      "ddn":"1900-06-29",
      "nationalite":"francaise"
    }, 
    {
      "role":"auteur",
      "id":2,
      "nom":"test 2e auteur",
      "prenom":"test",
      "ddn":"1900-06-29",
      "nationalite":"francaise"
    }
  ]'
);

INSERT INTO Ressource VALUES(11,'Intouchable','2011-11-02',
  'editeur intouchable','comedy-drama',11,'film',
  '[
    {
      "synopsis":"synopsis hello im here",
      "langue":"francaise",
      "duree":"1 hour 52 minutes"
    }
  ]' ,
  '[
    {
      "role":"realisateur",
      "id":11,
      "nom":"Olivier",
      "prenom":"Nakache",
      "ddn":"1900-06-20",
      "nationalite":"francaise"
    },
    {
      "role":"acteur",
      "id":11,
      "nom":"Olivier",
      "prenom":"Nakache",
      "ddn":"1900-06-20",
      "nationalite":"francaise"
    }
  ]'
);

INSERT INTO Ressource VALUES(21,'Je m_appelle Helene','2011-11-03',
  'Helene','chanson sentimentale',21,'musique',
  '[
    {
      "duree": "3 minutes 49 seconds"
    }
  ]' ,
  '[
    {
      "role":"interprete",
      "id":21,
      "nom":"Helene",
      "prenom":"Rolles",
      "ddn":"1900-06-20",
      "nationalite":"francaise"
    }
  ]'
);

INSERT INTO Exemplaire VALUES(1,'neuf',1,1);
INSERT INTO Exemplaire VALUES(2,'neuf',0,1);
INSERT INTO Exemplaire VALUES(3,'bon',1,1);
INSERT INTO Exemplaire VALUES(4,'neuf',0,1);
INSERT INTO Exemplaire VALUES(5,'perdu',0,1);

INSERT INTO Exemplaire VALUES(6,'bon',0,11);
INSERT INTO Exemplaire VALUES(7,'neuf',0,11);
INSERT INTO Exemplaire VALUES(8,'neuf',0,11);
INSERT INTO Exemplaire VALUES(9,'neuf',1,11);
INSERT INTO Exemplaire VALUES(10,'perdu',0,11);
INSERT INTO Exemplaire VALUES(11,'perdu',0,11);

INSERT INTO Exemplaire VALUES(12,'bon',1,21);
INSERT INTO Exemplaire VALUES(13,'bon',1,21);
INSERT INTO Exemplaire VALUES(14,'bon',1,21);
INSERT INTO Exemplaire VALUES(15,'bon',0,21);
INSERT INTO Exemplaire VALUES(16,'bon',1,21);
INSERT INTO Exemplaire VALUES(17,'neuf',1,21);
INSERT INTO Exemplaire VALUES(18,'neuf',1,21);

