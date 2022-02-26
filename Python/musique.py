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

def rechercheCompositeur(cur,nom, prenom):     #Fonction qui retourne 1 si le compositeur existe, 0 sinon
    sql = "SELECT id,nom, prenom FROM Contributeur WHERE compositeur"%(nom,prenom)
    cur.execute(sql)
    row = cur.fetchone()
    while (row):
        if (row[1] == nom and row[2] == prenom):
            return row[0]
        row = cur.fetchone()
    return 0

def rechercheInterprete(cur,nom, prenom):     #Fonction qui retourne 1 si le compositeur existe, 0 sinon
    sql = "SELECT nom, prenom FROM Contributeur WHERE interprete"
    cur.execute(sql)
    row = cur.fetchone()
    while (row):
        if (row[1] == nom and row[2] == prenom):
            return row[0]
        row = cur.fetchone()
    return 0

def ajouter_musique(cur):
    titre = input("Quel est le titre de la musique ?")
    titre="'"+titre+"'"
    date = input("Quel est la date d'apparition de la musique ?")
    date="'"+date+"'"
    editeur = input("Quel est l'éditeur de la musique ?")
    editeur="'"+editeur+"'"
    genre = input("Quel est le genre de la musique ?")
    genre="'"+genre+"'"

    duree = input("Quelle est la durée de la musique ?")
    duree="'"+duree+"'"

    code_classification=input("Quelle est le code_classification de la musique ?")
    code_classification=int(code_classification)
    code_unique = get_id(cur,"Ressource") + 1

    sql = "insert into Ressource values (%d,%s,%s,%s,%s,%d)" % (code_unique, titre, date, editeur, genre,code_classification)
    #code_classification?
    cur.execute(sql)

    sql = "insert into Musique values (%d, %s)" % (code_unique, duree)
    cur.execute(sql)
    k = int(input("Ajouter un compositeur ? 1 pour oui, 0 pour non: "))

    ## Ajout de compositeur
    while k == 1:
        compositeur_nom = input("Nom ?")
        compositeur_prenom = input("Prénom ?")
        compositeur_ddn = input("Date de naissance ?")
        compositeur_nat = input("Nationalité ?")
        test = rechercheCompositeur(compositeur_nom, compositeur_prenom)
        if (test == 0):   #il n'existe pas ce compositeur
            id = get_id("Contributeur") + 1
            sql = "insert into Contributeur values(%d,%s,%s,%s,%s);" % (id, compositeur_nom, compositeur_prenom, compositeur_ddn, compositeur_nat)
            cur.execute(sql)
            sql = "insert into Ressource_Contributeur values('compositeur',%d,%d);" % (code_unique, id)
            cur.execute(sql)
        else:   #il existe ce compositeur
            sql = "insert into Ressource_Contributeur values (%d,%d, 'compositeur');" % (code_unique, test)
        cur.execute(sql)

        k = int(input("Ajouter un autre compositeur ? 1 pour oui, 0 pour non"))

    p = int(input("Ajouter un interprète ? 1 pour oui, 0 pour non: "))

    ## Ajout d'interprete
    while p == 1:
        interprete_nom = input("Nom ?")
        interprete_prenom = input("Prénom ?")
        interprete_ddn = input("Date de naissance ?")
        interprete_nat = input("Nationalité ?")
        test = rechercheInterprete(interprete_nom, interprete_prenom)
        if (test == 0):  #il n'existe pas cet interprete
            id = id("Contributeur") + 1
            sql = "insert into Contributeur values(%d,%s,%s,%s,%s);" % (id, interprete_nom, interprete_prenom, interprete_ddn, interprete_nat)
            cur.execute(sql)
            sql = "insert into Ressource_Contributeur values('interprete',%d,%d);" % (code_unique, id)
            cur.execute(sql)
        else:   #il existe cet interprete
            sql = "insert into Ressource_Contributeur values (%d,%d, 'interprete');" % (code_unique, test)
        cur.execute(sql)

        p = int(input("Ajouter un autre interprete ? 1 pour oui, 0 pour non"))