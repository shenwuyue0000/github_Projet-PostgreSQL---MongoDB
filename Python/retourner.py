# 导入依赖包
# !/usr/bin/python3

def retourner(cur):
    sql = "select A.nom, A.prenom, P.*, R.titre, R.editeur, R.genre \
            from Pret as P, Adherent as A, Exemplaire as E, Ressource as R \
            where P.adherent=A.secu \
            AND P.id_exemplaire=E.id \
            AND E.ressource_code=R.code_unique"

    cur.execute(sql)
    res = cur.fetchall()

    print("nom|prenom| adherent|id_exemplaire|"
          "     date_pret       |       duree      |    titre    "
          "|     editeur      |       genre      |   ")
    for raw in res:
        print(raw)

    secu = input("Entrez votre numéro de secu: ")
    id_exemplaire=int(input("Entrez l'id_exemplaire que vous voulez retourner: "))
    sql = "select * from \
            Pret as P \
            where P.adherent='%s' \
            and P.id_exemplaire='%d'" %(secu,id_exemplaire)

    cur.execute(sql)
    res = cur.fetchall()

    for raw in res:
        print(raw)

    sql="delete from Pret \
        where id_exemplaire=%d \
        and adherent='%s'" %(id_exemplaire,secu)

    cur.execute(sql)
    res = cur.fetchall()

    print("resultat apres le retour\n:")
    for raw in res:
        print(raw)



