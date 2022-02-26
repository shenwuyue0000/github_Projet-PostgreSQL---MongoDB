# !/usr/bin/python3

import datetime

import psycopg2

def conseil_pour_adherent(conn):
    cur = conn.cursor()

    print(("Pour quel adherent souhaitez-vous proposer un conseil ?\n"))
    # affiche tous les adherent.
    sql = "SELECT A.login_adherent, A.prenom, A.nom \
        FROM Adherent A \
        ORDER BY A.login_adherent desc;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\nCompte | Prenom | Nom ")
    for raw in res :
        print("%s | %s | %s" %(raw[0],raw[1],raw[2]))
    # choisir un adherent.
    identite = input("Saisissez le nom de compte, svp.\n")
    exist = False
    for raw in res :
        if identite == raw[0]:
            exist = True
            break
    while exist == False :
        goon_or_not = input("\nCe compte n'existe pas. \nVoulez-vouz réessayer? \n(Y|N) \n")
        if goon_or_not == 'Y' or goon_or_not == 'y' :
            identite = input("Saisissez encore une fois le nom de compte, svp.\n")
            for raw in res :
                if identite == raw[0]:
                    exist = True
                    break
        elif goon_or_not == 'N' or goon_or_not == 'n':
            break
        else :
            break
    # On retire l'exemplaire qu'il a emprunté le plus long temps.
    try:
        sql = "SELECT P.id_examplaire, P.duree \
            FROM Pret P \
            WHERE P.compte_adherent='%s' \
            ORDER BY P.duree desc;" %identite
        cur.execute(sql)
        res = cur.fetchone() [0]
    # Si il n'y a pas d'enregistrement pour cette personne, on ne peut pas lui donner un conseil.
    except psycopg2.IndentationError as e :
        print ("On a aucun enregistrement pour cette personne.")
    # Dans ce cas on choisit l'exemplaire le plus demandé commme une reference.
        sql = "SELECT P.id_examplaire, P.duree \
            FROM Pret P \
            ORDER BY P.duree desc;"
        cur.execute(sql)
        res = cur.fetchone() [0]
    # A l'aide du genre d'exemplaire qu'il aime beaucoup,
    sql = "SELECT E.genre \
        FROM Examplaire E \
        WHERE E.id=res;"
    cur.execute(sql)
    res = cur.fetchone()
    #On lui propose tous les exemplaires du même genre.
    sql = "SELECT E.titre \
        FROM Examplaire E \
        WHERE E.genre='%s';" %res
    cur.execute(sql)
    res = cur.fetchall()
    print("Voici des exemplaires du meme genre que ce que préfère l'adherent: \n")
    for raw in res :
        print("%s" %raw)
