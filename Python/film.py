# 导入依赖包
# !/usr/bin/python3

def helloworld():
    print("helloworld")

def get_id(cur,table):     #retourner l'id de dernier enregistrement dans la table
    sql = "SELECT * FROM %s" %(table)
    cur.execute(sql)
    row = cur.fetchone()
    while (row):
        id = row[0]
        row = cur.fetchone()
    return id

def rechercheRealisateur(cur,nom, prenom):     #Fonction qui retourne l'id du compositeur s'il existe, 0 sinon
    sql = "SELECT id,nom, prenom FROM Contributeur WHERE nom='%s' and prenom='%s'"%(nom,prenom)
    cur.execute(sql)
    row = cur.fetchone()
    while (row):
        if (row[1] == nom and row[2] == prenom):
            return row[0]
        row = cur.fetchone()
    return 0

def rechercheActeur(cur,nom, prenom):     #Fonction qui retourne l'id du compositeur s'il existe, 0 sinon
    sql = "SELECT nom, prenom FROM Contributeur WHERE nom='%s' and prenom='%s'"%(nom,prenom)
    cur.execute(sql)
    row = cur.fetchone()
    while (row):
        if (row[1] == nom and row[2] == prenom):
            return row[0]
        row = cur.fetchone()
    return 0

def ajouter_film(cur):
    titre = input("Quel est le titre du film ?")
    titre="'"+titre+"'"
    date = input("Quel est la date d'apparition du film ?")
    date="'"+date+"'"
    editeur = input("Quel est l'éditeur du film ?")
    editeur="'"+editeur+"'"
    genre = input("Quel est le genre du film ?")
    genre="'"+genre+"'"

    duree = input("Quelle est la durée du film ?")
    duree="'"+duree+"'"

    code_classification=input("Quelle est le code_classification du film ?")
    code_classification=int(code_classification)
    code_unique = get_id(cur,"Ressource") + 1

    sql = "insert into Ressource values (%d,%s,%s,%s,%s,%d)" % (code_unique, titre, date, editeur, genre,code_classification)
    #code_classification?
    cur.execute(sql)

    sql = "insert into Musique values (%d, %s)" % (code_unique, duree)
    cur.execute(sql)
    k = int(input("Ajouter un compositeur ? 1 pour oui, 0 pour non: "))

    ## Ajout de realisateur
    while k == 1:
        realisateur_nom = input("Nom ?")
        realisateur_prenom = input("Prénom ?")
        realisateur_ddn = input("Date de naissance ?")
        realisateur_nat = input("Nationalité ?")
        test = rechercheCompositeur(realisateur_nom, realisateur_prenom)
        if (test == 0):   #il n'existe pas ce compositeur
            id = get_id("Contributeur") + 1
            sql = "insert into Contributeur values(%d,%s,%s,%s,%s);" % (id, realisateur_nom, realisateur_prenom, realisateur_ddn, realisateur_nat)
            cur.execute(sql)
            sql = "insert into Ressource_Contributeur values('realisateur',%d,%d);" % (code_unique, id)
            cur.execute(sql)
        else:   #il existe ce compositeur
            sql = "insert into Ressource_Contributeur values (%d,%d, 'realisateur');" % (code_unique, test)
        cur.execute(sql)

        k = int(input("Ajouter un autre realisateur ? 1 pour oui, 0 pour non"))

    p = int(input("Ajouter un acteur ? 1 pour oui, 0 pour non: "))

    ## Ajout d'un acteur
    while p == 1:
        acteur_nom = input("Nom ?")
        acteur_prenom = input("Prénom ?")
        acteur_ddn = input("Date de naissance ?")
        acteur_nat = input("Nationalité ?")
        test = rechercheActeur(acteur_nom, acteur_prenom)
        if (test == 0):  #il n'existe pas cet interprete
            id = id("Contributeur") + 1
            sql = "insert into Contributeur values(%d,%s,%s,%s,%s);" % (id, acteur_nom, acteur_prenom, acteur_ddn, acteur_nat)
            cur.execute(sql)
            sql = "insert into Ressource_Contributeur values('acteur',%d,%d);" % (code_unique, id)
            cur.execute(sql)
        else:   #il existe cet interprete
            sql = "insert into Ressource_Contributeur values (%d,%d, 'acteur');" % (code_unique, test)
        cur.execute(sql)

        p = int(input("Ajouter un autre acteur ? 1 pour oui, 0 pour non"))