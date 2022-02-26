insert into Contributeur values(1,'Antoine de','Saint-Exupery',
  '1900-06-29','francaise');
insert into Contributeur values(2,'Antoine de2','Saint-Exupery2',
  '1901-06-29','francaise');
insert into Contributeur values(3,'Antoine de3','Saint-Exupery3',
  '1902-06-29','francaise');
insert into Contributeur values(11,'Olivier','Nakache',
  '1973-04-14','francaise');
insert into Contributeur values(12,'Francois','Cluzet',
  '1955-09-21','francaise');
insert into Contributeur values(21,'Helene','Rolles',
  '1966-12-20','francaise');
insert into Contributeur values(22,'Gerard','Salesses',
  '1949-08-10','francaise');

insert into Livre values(0001,'le petit prince','1943-04-06',
  'Gallimard Jeunesse','le conte pour enfants',0001,
  978314046,'Toujours en quête d_amis, le petit prince arrive sur Terre, et c_est encore la solitude et l_absurdité de l_existence qu_il va découvrir : sa rencontre avec le serpent qui ne parle que par énigmes (il « les résout toutes »), celle d_une fleur « à trois pétales », l_écho des montagnes.',
  'francaise',1);
insert into Livre values(0002,'le petit prince','1944-04-06',
  'Gallimard Jeunesse','le conte pour enfants',0001,
  978314047,'resume',
  'francaise',2);
insert into Livre values(0003,'le petit prince','1945-04-06',
  'Gallimard Jeunesse','le conte pour enfants',0001,
  978314048,'resume',
  'francaise',3);

insert into Film values(0011,'Intouchable','2011-11-02',
  'Les Intouchables','comedy-drama',0011,
  'francaise','1 hour 52 minutes','synopsis',11,12);

insert into Musique values(0021,'Je m_appelle Helene','1993-10-01',
  'Montjoie GF','chanson sentimentale',0021,
  '3 minutes 49 seconds',21,22);

'''
  insert into Ressource values(0001,'le petit prince','1943-04-06',
    'Gallimard Jeunesse','le conte pour enfants',0001);
  insert into Ressource values(0002,'le petit prince','1944-04-06',
    'Gallimard Jeunesse','le conte pour enfants',0001);
  insert into Ressource values(0003,'le petit prince','1945-04-06',
    'Gallimard Jeunesse','le conte pour enfants',0001);
  insert into Ressource values(0011,'Intouchable','2011-11-02',
    'Les Intouchables','comedy-drama',0011);
  insert into Ressource values(0021,'Je m_appelle Helene','1993-10-01',
    'Montjoie GF','chanson sentimentale',0021);
'''

  insert into Exemplaire values(0001,0001,'neuf',1);
  insert into Exemplaire values(0002,0001,'bon',1);
  insert into Exemplaire values(0003,0001,'abime',1);
  insert into Exemplaire values(0004,0001,'perdu',1);

  insert into Exemplaire values(0005,0002,'neuf',0);
  insert into Exemplaire values(0006,0003,'neuf',0);
  insert into Exemplaire values(0007,0011,'neuf',0);
  insert into Exemplaire values(0008,0021,'neuf',0);



insert into Ressource_Contributeur values('auteur',1,1);
insert into Ressource_Contributeur values('auteur',2,2);
insert into Ressource_Contributeur values('auteur',3,3);
insert into Ressource_Contributeur values('auteur',11,11);
insert into Ressource_Contributeur values('auteur',11,12);
insert into Ressource_Contributeur values('auteur',21,21);
insert into Ressource_Contributeur values('auteur',21,22);


insert into Compte_Personnel values('wangsong','mdp');
insert into Compte_Personnel values('zhuhongy','mdp');
insert into Compte_Adherent values('shenqiao','mdp');
insert into Compte_Adherent values('vaursdam','mdp');

insert into Personnel values(547654,'WANG','Songyang',
  'Compiegne','songyang.wang@etu.utc.fr','wangsong');
insert into Personnel values(321423,'ZHU','Hongyi',
  'Compiegne','hongyi.zhu@etu.utc.fr','zhuhongy');
insert into Adherent values(241411,'SHEN','Qiaodan',
  'Compiegne','qiaodan.shen@etu.utc.fr',
  '2000-01-01','0600000000',1,'shenqiao');
insert into Adherent values(223223,'DAMIEN','Vaurs',
  'Compiegne','damien.vaurs@etu.utc.fr',
  '2000-01-01','0600000000',1,'vaursdam');

insert into Pret values('shenqiao',1,'2021-10-23','10 days');
insert into Pret values('vaursdam',2,'2021-10-24','20 days');
