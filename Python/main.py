# 导入依赖包
# !/usr/bin/python3

import psycopg2
#from musique import helloworld
#from musique import get_id
#from musique import rechercheCompositeur
#from musique import rechercheInterprete
from musique import ajouter_musique
from film import ajouter_film
from livre import ajouter_livre
from exemplaire import ajouter_exemplaire
from gestion_donnee_utilisateur import gestion_donnee_utilisateur
from gestion_pret_retard_reservation import gestion_pret_retard_reservation
from conseil_pour_adherent import conseil_pour_adherent
from retourner import retourner


#
conn = psycopg2.connect(database="postgres", user="postgres", password="101200", host="localhost", port="5432")
cur = conn.cursor()  #

print("\n")
print("Bienvenue dans le systeme de la gestion de la Biblio !!!")
auth=input("Êtes-vous un personnel ou un adherent? (Tapez p/a): ")
if(auth=='p'):
    '''
    personnel_login=input("Entrez votre login personnel: ")

    cur.execute("SELECT * FROM Compte WHERE login='%s'" %(personnel_login))
    results = cur.fetchall()
    if(results==[]):
        print("Ce login n'existe pas, Veuillez réessayer")
        exit()
    personnel_mdp = input("Entrez votre mot de passe personnel: ")
    cur.execute("SELECT mdp FROM Compte WHERE login='%s'" %(personnel_login))
    mdp=cur.fetchone()
    mdp=mdp[0]
    #print("mdp::",mdp)
    if(mdp!=personnel_mdp):
        print("Le mot de passe n'est pas correct, Veuillez réessayer")
        exit()
    '''

    #helloworld()

    print("Commencer Opération\n")
    print("Qu'est-ce que vous voulez faire?")
    print("1:Voir toute la table Ressource-Contributeur\t2:Voir toute la table Contributeur")
    print("3:Voir toute la table Ressource\t4:Voir toute la table Livre")
    print("5:Voir toute la table Film\t6:Voir toute la table Musique")
    print("7:Voir toute la table Compte\t8:Voir toute la table Adherent")
    print("9:Voir toute la table Personnel\t10:Voir toute la table Pret")
    print("11:Modifier mes informations ou celles d'un adherent\t12:ajouter des documents")
    print("13:Ajouter un exemplaire")
    print("14:Donner un conseil pour un adehrant")
    print("15:Retourner un exemplaire")
    reponse = input("Qu'est-ce que vous voulez faire? ")

   if(reponse == '1'):
        cur.execute("select * from Ressource_contributeur")
        ressource_contributeur_liste = cur.fetchall()  # Ressource_Contributeur
        print(ressource_contributeur_liste)

    if(reponse == '2'):
         cur.execute("select * from Contributeur")
         contributeur_liste = cur.fetchall()  # Contributeur
         print(contributeur_liste)

    if(reponse == '3'):
          cur.execute("select * from Ressource")
          ressource_liste = cur.fetchall()  # Ressource
          print(ressource_liste)

    if(reponse == '4'):
          cur.execute("select * from Livre")
          livre_liste = cur.fetchall()  # Livre
          print(livre_liste)

    if(reponse == '5'):
          cur.execute("select * from Film")
          film_liste = cur.fetchall()  # Film
          print(film_liste)
        
    if(reponse == '6'):
        cur.execute("select * from Musique")
        musique_liste = cur.fetchall()  # Musique
        print(musique_liste)

    if(reponse == '7'):
        cur.execute("select * from Compte")
        compte_liste = cur.fetchall()  # Compte
        print(compte_liste)

    if(reponse == '8'):
        cur.execute("select * from Adherent")
        adherent_liste = cur.fetchall()  # Adherent
        print(adherent_liste)

    if(reponse == '9'):
        cur.execute("select * from Personnel")
        personnel_liste = cur.fetchall()  # Personnel
        print(personnel_liste)

    if(reponse == '10'):
        cur.execute("select * from Pret")
        pret_liste = cur.fetchall()  # Prêt
        print(pret_liste)

    if(reponse == '11'):
        gestion_donnee_utilisateur(conn)    # Modification de données

    if (reponse == '12'):
        type=input("livre ou film ou musique?")
        if(type=="musique"):
            ajouter_musique(cur)

        if(type=="film"):
            ajouter_film(cur)

        if (type == "livre"):
            ajouter_livre(cur)

    if (reponse == '13'):
        ajouter_exemplaire(cur)

    if (reponse == '14'):
       conseil_pour_adherent(conn)
    
    if (reponse == '15'):
       retourner(cur)


elif(auth=='a'):
    adherent_login = input("Entrez votre login adherent: ")

    cur.execute("SELECT * FROM Compte WHERE login='%s'" % (adherent_login))
    results = cur.fetchall()
    if (results == []):
        print("Ce login n'existe pas, Veuillez reessayer")
        exit()
    adherent_mdp = input("Entrez votre mot de passe adherent: ")
    cur.execute("SELECT mdp FROM Compte WHERE login='%s'" % (adherent_login))
    mdp = cur.fetchone()
    mdp = mdp[0]
    #print("mdp::", mdp)
    if (mdp != adherent_mdp):
        print("Ce mot de passe n'est pas correct, Veuillez reessayer")
        exit()
    print("Commencer Operation")
    print("Qu'est-ce que vous voulez faire?")
    print("1:Voir toute la table Ressource-Contributeur\t2:Voir toute la table Contributeur")
    print("3:Voir toute la table Ressource\t4:Voir toute la table Livre")
    print("5:Voir toute la table Film\t6:Voir toute la table Musique")
    print("7:Modifier mes informations\t8:Voir mes prêts\t9:Gérer mes prêts ou emprunter")         #le droit de l'adherent est limite
    reponse= input("Qu'est-ce que vous voulez faire?")

    if(reponse == '1'):
         cur.execute("select * from Ressource_contributeur")
         ressource_contributeur_liste = cur.fetchall()  # Ressource_Contributeur
         print(ressource_contributeur_liste)
 
    if(reponse == '2'):
          cur.execute("select * from Contributeur")
          contributeur_liste = cur.fetchall()  # Contributeur
          print(contributeur_liste)
 
    if(reponse == '3'):
           cur.execute("select * from Ressource")
           ressource_liste = cur.fetchall()  # Ressource
           print(ressource_liste)
 
    if(reponse == '4'):
           cur.execute("select * from Livre")
           livre_liste = cur.fetchall()  # Livre
           print(livre_liste)
 
    if(reponse == '5'):
           cur.execute("select * from Film")
           film_liste = cur.fetchall()  # Film
           print(film_liste)
         
    if(reponse == '6'):
         cur.execute("select * from Musique")
         musique_liste = cur.fetchall()  # Musique
         print(musique_liste)

    if(reponse == '7'):
         gestion_donnee_utilisateur(conn)
    
    if (reponse=='8') :
        cur.execute("select * from Pret P join Musique M on P.code_ressource=M.code_unique where compte_adherent='%s' " % (adherent_login))
        pret_liste = cur.fetchall()   #Musique
        print(pret_liste)
        cur.execute("select * from Pret P join Film F on P.code_ressource=F.code_unique where compte_adherent='%s'" % (adherent_login))
        pret_liste = cur.fetchall()   #Film
        print(pret_liste)
        cur.execute("select * from Pret P join Livre L on P.code_ressource=L.code_unique where compte_adherent='%s'" % (adherent_login))
        pret_liste = cur.fetchall()   #Livre
        print(pret_liste)

    if(reponse == '9'):
        gestion_pret_retard_reservation(conn)


#
conn.commit()
cur.close()
conn.close()
