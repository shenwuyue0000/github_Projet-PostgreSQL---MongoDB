# 导入依赖包
# !/usr/bin/python3

def ajouter_exemplaire(cur):
    id = input("Quel est l'id de l'exemplaire' ?")
    res_code = input("Quel est le ressource_code de l'exemplaire' ?")
    res_code = "'" + res_code + "'"
    etat = input("Quel est l'etat de l'exemplaire' ?")
    etat = "'" + etat + "'"
    disponible = input("Quel est la disponibilite de l'exemplaire' ?")

    sql = "insert into Exemplaire values (%d,%s,%s,%d)" % (id, res_code, etat, disponible)
    cur.execute(sql)