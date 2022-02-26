# **Modèle Logique de Données**



**Ressource** (#code_unique : integer, titre : string, date_apparition : date, editeur : string, genre : string, code_classification : integer, type : {livre, film, musique}, isbn : integer, resume : text, langue : string, duree : date, synopsis : text)

<u>Contrainte</u> :

- Titre, date_apparition, editeur, genre, code_classification, etat, type NOT NULL

- Isbn UNIQUE

- NOT (type = livre AND (duree OR synopsis))

- NOT (type = film AND (isbn OR resume))

- NOT (type = musique AND (isbn OR resume OR langue OR synopsis))

&emsp;

**Contributeur** (#id : integer, nom : string, prenom : string, ddn : date, nationalite : string)

<u>Contrainte</u> :

- nom, prenom, ddn, nationalite NOT NULL

- ddn est entre (1900,2021)

&emsp;

**Ressource-Contributeur** (#ressource_code => Ressource.code_unique, #contributeur_id => Contributeur.id)

<u>Contrainte</u> :

- role NOT NULL

- NOT (role = auteur AND Ressource.type = (film OR musique))

- NOT (role = (realisateur OR acteur) AND Ressource.type = (livre OR musique))

- NOT (role = (compositeur OR interprete) AND Ressource.type = (livre OR film))

&emsp;

**Compte_Adherent** (#login : string, mdp : string)

<u>Contrainte</u> :

- mdp NOT NULL

&emsp;

**Compte_Personnel** (#login : string, mdp : string)

<u>Contrainte</u> :

- mdp NOT NULL

&emsp;

**Personnel** (#sécu : string, nom : string, prenom : string, adresse : text, mail : string, login_personnel => Compte_Personnel.login)

<u>Contrainte</u> :

- nom, prenom, adresse, mail NOT NULL

- login_personnel UNIQUE NOT NULL

- Projection (Compte_Personnel, login) = Projection (Personnel, login_personnel)

&emsp;

**Adherent** (#sécu : string, nom : string, pernom : string, adresse : text, mail : string, ddn : date, telephone : numeric, etat : {0,1}, login_adherent => Compte_Adherent.login)

<u>Contrainte</u> :

- nom, prenom, adresse, mail, ddn, telephone, etat NOT NULL

- login_adherent UNIQUE NOT NULL

- Projection (Compte_Adherent, login) = Projection (Adherent, login_adherent)

- ddn est entre (1900,2020)

- etat = 0 ou 1, 0=>passée, 1=>actuelle

&emsp;

**Exemplaire** (#exemplaire_id : integer, etat : {neuf, bon, abime, perdu}, disponible : {0,1}, date_pret : date, duree : date, ressource_code => Ressource.code_unique, adherent => secu)

<u>Contrainte</u> :

- etat, disponible, ressource_code NOT NULL

- NOT (disponible = 0 AND (NOT (date_pret OR duree)))

- date < date d’aujourd’hui

- durée > 0 mins

&emsp;

**Pret** (#adherent => adherent.secu, #exemplaire => Exemplaire.exemplaire_id, date_pret : date , duree : date)

<u>Contrainte</u> :

- date_pret, duree NOT NULL

- date_pret <= date d’aujourd’hui

- duree > 0 mins

