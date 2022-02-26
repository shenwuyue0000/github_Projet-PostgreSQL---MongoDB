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

def rechercheAuteur(cur,nom, prenom):     #Fonction qui retourne l'id du acteur s'il existe, 0 sinon
    sql = "SELECT id,nom, prenom FROM Contributeur WHERE nom='%s' and prenom='%s'"%(nom,prenom)
    cur.execute(sql)
    row = cur.fetchone()
    while (row):
        if (row[1] == nom and row[2] == prenom):
            return row[0]
        row = cur.fetchone()
    return 0


def ajouter_livre(cur):
    titre = input("Quel est le titre du livre ?")
    titre="'"+titre+"'"
    date = input("Quel est la date d'apparition du livre ?")
    date="'"+date+"'"
    editeur = input("Quel est l'éditeur du livre ?")
    editeur="'"+editeur+"'"
    genre = input("Quel est le genre du livre ?")
    genre="'"+genre+"'"

    duree = input("Quelle est la durée du livre ?")
    duree="'"+duree+"'"

    code_classification=input("Quelle est le code_classification du livre ?")
    code_classification=int(code_classification)
    code_unique = get_id(cur,"Ressource") + 1

    sql = "insert into Ressource values (%d,%s,%s,%s,%s,%d)" % (code_unique, titre, date, editeur, genre,code_classification)
    #code_classification?
    cur.execute(sql)

    sql = "insert into Musique values (%d, %s)" % (code_unique, duree)
    cur.execute(sql)
    k = int(input("Ajouter un auteur ? 1 pour oui, 0 pour non: "))

    ## Ajout de auteur
    while k == 1:
        auteur_nom = input("Nom ?")
        auteur_prenom = input("Prénom ?")
        auteur_ddn = input("Date de naissance ?")
        auteur_nat = input("Nationalité ?")
        test = rechercheAuteur(auteur_nom, auteur_prenom)
        if (test == 0):   #il n'existe pas ce auteur
            id = get_id("Contributeur") + 1
            sql = "insert into Contributeur values(%d,%s,%s,%s,%s);" % (id, auteur_nom, auteur_prenom, auteur_ddn, auteur_nat)
            cur.execute(sql)
            sql = "insert into Ressource_Contributeur values('auteur',%d,%d);" % (code_unique, id)
            cur.execute(sql)
        else:   #il existe ce auteur
            sql = "insert into Ressource_Contributeur values (%d,%d, 'auteur');" % (code_unique, test)
        cur.execute(sql)

        k = int(input("Ajouter un autre auteur ? 1 pour oui, 0 pour non"))

