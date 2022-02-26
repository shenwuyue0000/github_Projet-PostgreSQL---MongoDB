# Note De Clarification

* Cahier de Charge (Contexte)
* NDC (classes, attributs et contraintes)
* Membre de Projet : Songyang WANG, Qiaodan SHEN, Hongyi ZHU, Damien VAURS

## **Système de gestion d'une bibliothèque**

Vous êtes chargés de concevoir un système de gestion pour une bibliothèque municipale qui souhaite informatiser ses activités : catalogage, consultations, gestion des utilisateurs, prêts, etc.

La bibliothèque offre un accès à un large choix de ressources de différents types (livres, films, et enregistrement musicaux). Une ressource, quelque soit son type, a un code unique, un titre, une liste de contributeurs, une date d'apparition, un éditeur, un genre et un code de classification qui permet de la localiser dans la bibliothèque. Un contributeur est caractérisé par son nom, son prénom, sa date de naissance et sa nationalité. Dans le cas d'un livre, les contributeurs sont les auteurs du document. Dans le cas d'une œuvre musicale, on distinguera compositeurs et interprètes. De même, on distinguera les réalisateurs et les acteurs pour les films. On souhaite également conserver des informations spécifiques suivant le type du document, par exemple : l'ISBN d'un livre et son résumé, la langue des documents écrits et des films, la longueur d'un film ou d'une œuvre musicale, le synopsis d'un film, etc. Enfin, les ressources dont dispose la bibliothèque peuvent être disponibles en plusieurs exemplaires, chacun dans un état différent : neuf, bon, abîmé ou perdu.

Chaque membre du personnel de la bibliothèque dispose d'un compte utilisateur (login et mot de passe) qui lui permet d'accéder aux fonctions d'administration du système. Chaque membre est caractérisé par son nom, son prénom, son adresse et son adresse e-mail.

Les adhérents de la bibliothèque disposent, eux aussi, d'un compte utilisateur (login et mot de passe) ainsi que d'une carte d'adhérent qui leur permettent d'emprunter des documents. Un adhérent est caractérisé par son nom, prénom, date de naissance, adresse, adresse e-mail et numéro de téléphone. La bibliothèque souhaite garder trace de toutes les adhésions, actuelles et passées.

Pour pouvoir emprunter un document, un adhérent à besoin de s'authentifier. Chaque prêt est caractérisé par une date de prêt et une durée de prêt. Un document ne peut être emprunté que s'il est disponible et en bon état. Un adhèrent ne peut emprunter simultanément qu'un nombre limité d'œuvres, chacune pour une durée limitée. Un adhérent sera sanctionné pour les retards dans le retour d'un ouvrage, ainsi que s'il dégrade l'état de celui-ci. Tout retard dans la restitution des documents empruntés entraîne une suspension du droit de prêt d'une durée égale au nombre de jours de retard. En cas de perte ou détérioration grave d'un document, la suspension du droit de prêt est maintenue jusqu'à ce que l'adhérent rembourse le document. Enfin, la bibliothèque peut choisir de blacklister un adhérent en cas de sanctions répétées.

## NDC

### Classes | Attributs | Contraintes

 1. Ressource <<abstrait>>

    code_unique : int {KEY} ; titre : text ; date_apparition : date ; editeur : text ; genre : text ; code_classification : int ; etat : {neuf, bon, abime, perdu}
    * Tous les attributs sont NOT NULL sauf la clé
 2. Contributeur

    id : int {KEY} ;  nom : text ; prenom : text  ; ddn : date ; nationalite : text
    * Tous les attributs sont NOT NULL sauf la clé
    * ddn est entre (1900,2021)
 3. Ressource-Contributeur

    ressource_code -> Ressource.code_unique {KEY}; contributeur_id -> Contributeur.id {KEY}
    * Tous les attributs sont NOT NULL sauf la clé
 4. Livre (fille de ressource)

    isbn : int {KEY} ; resume : text ; langue : text ; auteur -> contributeur.id
    * Tous les attributs sont NOT NULL sauf la clé
    * //Projection(Livre, auteur) = Projection(Contributeur, id)
 5. Musique (fille de ressource)

    duree : date ; compositeur -> Contributeur.id ; interprete -> Contributeur.id
    * Tous les attributs sont NOT NULL sauf la clé
    * // ( Projection(Musique, compositeur) UNION Projection(Musique, interprete) ) = Projection(Contributeur, id)
 6. Film (fille de ressource)

    langue : text ; duree : date ; synopsis : text ; realisateur -> Contributeur.id ; acteur -> Contributeur.id
    * Tous les attributs sont NOT NULL sauf la clé
    * // ( Projection(film, realisateur) UNION Projection(film, acteur) ) = Projection(Contributeur, id)
 7. Compte

    login : text {KEY} ; mdp : text
    * Tous les attributs sont NOT NULL sauf la clé
    * ( Projection(personnel, compte) UNION Projection(adherent, compte) ) = Projection(compte, login)
 8. Personnel

    compte -> compte.login {KEY} ; nom : text ; prenom : text ; adresse : text ; mail : text
    * Tous les attributs sont NOT NULL sauf la clé
 9. Adherent

    compte -> compte.login {KEY} ; nom:text ; pernom : text ; adresse : text ; mail : text ; ddn : date ; telephone : int ; etat : {0,1}
    * Tous les attributs sont NOT NULL sauf la clé
    * ddn est entre (1900,2020)
    * etat = 0 ou 1, 0=>passée, 1=>actuelle
10. Pret

    compte_adherent -> adherent.compte ; ressource_code -> Ressource.code_unique ; date_pret : date ; duree : date
    * Tous les attributs sont NOT NULL sauf la clé
    * date < date d’aujourd’hui
    * durée >0 mins
