CREATE VIEW v_exemplaire_livre_disponible AS
SELECT e.id, e.etat, r.titre, d->>'langue' AS langue, d->>'resume' AS resume
FROM ressource r, exemplaire e, JSON_ARRAY_ELEMENTS(r.detail) d
WHERE r.code_unique=e.ressource_code AND e.disponibilite=1 AND r.type='livre';

CREATE VIEW v_exemplaire_livre_indisponible AS
SELECT e.id, e.etat, r.titre, d->>'langue' AS langue, d->>'resume' AS resume
FROM ressource r, exemplaire e, JSON_ARRAY_ELEMENTS(r.detail) d
WHERE r.code_unique=e.ressource_code AND e.disponibilite=0 AND r.type='livre';

CREATE VIEW v_exemplaire_film_disponible AS
SELECT e.id, e.etat, r.titre, d->>'langue' AS langue, d->>'duree' AS duree, d->>'synopsis' AS synopsis
FROM ressource r, exemplaire e, JSON_ARRAY_ELEMENTS(r.detail) d
WHERE r.code_unique=e.ressource_code AND e.disponibilite=1 AND r.type='film';

CREATE VIEW v_exemplaire_film_indisponible AS
SELECT e.id, e.etat, r.titre, d->>'langue' AS langue, d->>'duree' AS duree, d->>'synopsis' AS synopsis
FROM ressource r, exemplaire e, JSON_ARRAY_ELEMENTS(r.detail) d
WHERE r.code_unique=e.ressource_code AND e.disponibilite=0 AND r.type='film';

CREATE VIEW v_exemplaire_musique_disponible AS
SELECT e.id, e.etat, r.titre, d->>'duree' AS duree
FROM ressource r, exemplaire e, JSON_ARRAY_ELEMENTS(r.detail) d
WHERE r.code_unique=e.ressource_code AND e.disponibilite=1 AND r.type='musique';

CREATE VIEW v_exemplaire_musique_indisponible AS
SELECT e.id, e.etat, r.titre, d->>'duree' AS duree
FROM ressource r, exemplaire e, JSON_ARRAY_ELEMENTS(r.detail) d
WHERE r.code_unique=e.ressource_code AND e.disponibilite=0 AND r.type='musique';

CREATE VIEW v_nb_total_exemplaire_livre AS
SELECT COUNT(*) AS nb_exemplaire_livre
FROM ressource r, exemplaire e
WHERE r.code_unique=e.ressource_code AND r.type='livre';

CREATE VIEW v_nb_total_exemplaire_film AS
SELECT COUNT(*) AS nb_exemplaire_film
FROM ressource r, exemplaire e
WHERE r.code_unique=e.ressource_code AND r.type='film';

CREATE VIEW v_nb_total_exemplaire_musique AS
SELECT COUNT(*) AS nb_exemplaire_musique
FROM ressource r, exemplaire e
WHERE r.code_unique=e.ressource_code AND r.type='musique';

CREATE VIEW v_nb_total_exemplaire AS
SELECT (l.nb_exemplaire_livre + f.nb_exemplaire_film + m.nb_exemplaire_musique) AS nb_total, l.nb_exemplaire_livre, f.nb_exemplaire_film, m.nb_exemplaire_musique
FROM v_nb_total_exemplaire_livre l, v_nb_total_exemplaire_film f, v_nb_total_exemplaire_musique m;

CREATE VIEW v_tous_les_editeurs AS
SELECT r.editeur
FROM ressource r;

CREATE VIEW v_tous_les_auteurs AS
SELECT c->>'id' AS id, c->>'nom' AS nom, c->>'prenom' AS prenom, c->>'ddn' AS ddn, c->>'nationalite' AS nationalite
FROM ressource r, JSON_ARRAY_ELEMENTS(r.contributeur) c
WHERE c->>'role'='auteur';

CREATE VIEW v_tous_les_realisateurs AS
SELECT c->>'id' AS id, c->>'nom' AS nom, c->>'prenom' AS prenom, c->>'ddn' AS ddn, c->>'nationalite' AS nationalite
FROM ressource r, JSON_ARRAY_ELEMENTS(r.contributeur) c
WHERE c->>'role'='realisateur';

CREATE VIEW v_tous_les_acteurs AS
SELECT c->>'id' AS id, c->>'nom' AS nom, c->>'prenom' AS prenom, c->>'ddn' AS ddn, c->>'nationalite' AS nationalite
FROM ressource r, JSON_ARRAY_ELEMENTS(r.contributeur) c
WHERE c->>'role'='acteur';

CREATE VIEW v_tous_les_compositeurs AS
SELECT c->>'id' AS id, c->>'nom' AS nom, c->>'prenom' AS prenom, c->>'ddn' AS ddn, c->>'nationalite' AS nationalite
FROM ressource r, JSON_ARRAY_ELEMENTS(r.contributeur) c
WHERE c->>'role'='compositeur';

CREATE VIEW v_tous_les_interpretes AS
SELECT c->>'id' AS id, c->>'nom' AS nom, c->>'prenom' AS prenom, c->>'ddn' AS ddn, c->>'nationalite' AS nationalite
FROM ressource r, JSON_ARRAY_ELEMENTS(r.contributeur) c
WHERE c->>'role'='interprete';







