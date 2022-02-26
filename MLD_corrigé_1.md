# **Modèle Logique de Données**



**Ressource** (#code_unique : integer, titre : string, date_apparition : date, editeur : string, genre : string, code_classification : integer)

<u>Contrainte</u> :

- Titre, date_apparition, editeur, genre, code_classification NOT NULL

&emsp;

**Contributeur** (#id : integer, nom : string, prenom : string, ddn : date, nationalite : string)

<u>Contrainte</u> :

- nom, prenom, ddn, nationalite NOT NULL

- ddn est entre (1900,2021)

&emsp;

**Ressource-Contributeur** (#ressource_code => Ressource.code_unique, #contributeur_id => Contributeur.id, role={auteur, realisateur, acteur, compositeur, interprete})

<u>Contrainte</u> :

- role NOT NULL

- NOT (role = auteur AND Ressource.type = (film OR musique))

- NOT (role = (realisateur OR acteur) AND Ressource.type = (livre OR musique))

- NOT (role = (compositeur OR interprete) AND Ressource.type = (livre OR film))

&emsp;

**Exemplaire** (#id : integer, etat : {neuf, bon, abime, perdu}, disponible : {0,1}, ressource_code => Ressource.code_unique)

<u>Contrainte</u> :

- etat, disponible, ressource_code NOT NULL

&emsp;

**Livre** (#res_code => Ressource.code_unique, isbn : integer, resume : string, langue : string)

<u>Contrainte</u> :

- isbn UNIQUE NOT NULL

&emsp;

**Film** (#res_code => Ressource.code_unique, langue : string, duree : interval, synopsis : string)

&emsp;

**Musique** (#res_code => Ressource.code_unique, duree : interval)

&emsp;

**Compte** (#login : string, mdp : string)

<u>Contrainte</u> :

- mdp NOT NULL

&emsp;

**Compte_Adherent** (#login => Compte.login)

&emsp;

**Compte_Personnel** (#login => Compte.login)

&emsp;

**Adherent** (#sécu : string, nom : string, pernom : string, adresse : text, mail : string, ddn : date, telephone : integer, etat : {0,1}, login_adherent => Compte_Adherent.login)

<u>Contrainte</u> :

- nom, prenom, adresse, mail, ddn, telephone, etat NOT NULL

- login_adherent UNIQUE NOT NULL

- Projection (Compte_Adherent, login) = Projection (Adherent, login_adherent)

- ddn est entre (1900,2020)

- etat = 0 ou 1, 0=>passée, 1=>actuelle

&emsp;

**Personnel** (#sécu : string, nom : string, prenom : string, adresse : text, mail : string, login_personnel => Compte_Personnel.login)

<u>Contrainte</u> :

- nom, prenom, adresse, mail NOT NULL

- login_personnel UNIQUE NOT NULL

- Projection (Compte_Personnel, login) = Projection (Personnel, login_personnel)

&emsp;

**Pret** (#adherent => adherent.secu, #id_exemplaire => Exemplaire.id, date_pret : date , duree : interval)

