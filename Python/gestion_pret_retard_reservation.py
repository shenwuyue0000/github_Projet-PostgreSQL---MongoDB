# gestion de prets, des retards et des reservation.

# fonction preter un livre marche
# fonction reserver un livre disponible marche

import datetime

def gestion_pret_retard_reservation(conn):
	cur = conn.cursor()
	
	choix = input("\nQu'est-ce que vous voulez faire ?\
			\n1) Emprunter ou réserver un exemplaire\
			\n2) Retourner un exemplaire\
			\nvotre choix : ")
	if choix == '1' :
		choix_type = input("\nQuel type d'exemplaire voulez-vous emprunter ou reserver ?\
			\n1) livre\
			\n2) film\
			\n3) musique\
			\nvotre choix : ")
		while choix_type != '1' and choix_type != '2' and choix_type != '3' :
			ifcontinuer = input("\nmal choix. \n1)ressayer 2)terminer\n")
			if ifcontinuer == '1' :
				choix_type = input("\nQuel type d'exemplaire voulez-vous emprunter ou reserver ?\
					\n1) livre\
					\n2) film\
					\n3) musique\
					\nvotre choix : ")
			elif ifcontinuer == '2' :
				return
			else :
				return

		# emprunter un exemplaire (livre)
		if choix_type == '1' :
			preter_ou_reserver = input("\n1) emprunter\n2) reserver\nvotre choix : ")
			while preter_ou_reserver != '1' and preter_ou_reserver != '2' :
				ifcontinuer = input("\nmal choix. \n1)ressayer 2)terminer\n")
				if ifcontinuer == '1' :
					preter_ou_reserver = input("\n1) emprunter\n2) reserver\nvotre choix : ")
				elif ifcontinuer == '2' :
					return
				else :
					return
			# preter quand disponible
			if preter_ou_reserver == '1' :
				# affiche tous les livres "disponibles"
				sql = "SELECT L.res_code,R.titre,E.id,E.disponible FROM Livre L,Ressource R,Exemplaire E \
					WHERE L.res_code=R.code_unique AND R.code_unique=E.ressource_code\
					AND E.disponible=1\
					ORDER BY E.id;"
				cur.execute(sql)
				res = cur.fetchall()
				print("\nres_code | titre | exemplaire_id ")
				for raw in res :
					print("%d | %s | %d | %d" %(raw[0],raw[1],raw[2]))
				# choisir un exemplaire a emprunter
				exemplaire_a_preter = int(input("L'id d'exemplaire vous voulez preter : "))
				exist = int(0)
				for raw in res :
					if exemplaire_a_preter == raw[2]:
						exist = int(1)
				while exist != 1 :
					ifcontinuer = input("\nmal id. \n1)ressayer 2)terminer\n")
					if ifcontinuer == '1' :
						exemplaire_a_preter = int(input("L'id de l'exemplaire que vous voulez emprunter : "))
						for raw in res :
							if exemplaire_a_preter == raw[2]:
								exist = int(1)
					elif ifcontinuer == '2' :
						return
					else :
						return
				# entrer secu d'adherent
				secu_adherent = input("secu d'adherent : ")
				sql = "SELECT nom,prenom FROM Adherent WHERE secu='%s';" %secu_adherent
				cur.execute(sql)
				res = cur.fetchall()	
				while not res :
					ifcontinuer = input("\nmal secu. \n1)ressayer 2)terminer\n")
					if ifcontinuer == '1' :
						secu_adherent = input("secu d'adherent : ")
						sql = "SELECT nom,prenom FROM Adherent WHERE secu='%s';" %secu_adherent
						cur.execute(sql)
						res = cur.fetchall()
					elif ifcontinuer == '2' :
						return
					else :
						return
				# entrer durée de prêt
				duree_preter = input("Combien de jours ? (0 < duree <= 180)\n")
				while int(duree_preter) > 180 or int(duree_preter) <= 0 :
					ifcontinuer = input("\nmal duree. \n1)ressayer 2)terminer\n")
					if ifcontinuer == '1' :
						duree_preter = input("Combien de jour ? (<=180)\n")
					elif ifcontinuer == '2' :
						return
					else :
						return
				duree_preter = duree_preter + ' days'
				# INSERT et UPDATE
				sql = "INSERT INTO Pret values('%s',%d,'%s','%s');" %(secu_adherent,exemplaire_a_preter,str(datetime.date.today()),duree_preter)
				cur.execute(sql)
				sql = "UPDATE Exemplaire SET disponible=0 WHERE id=%d;" %exemplaire_a_preter
				cur.execute(sql)
				# affiche resultat
				sql = "SELECT * FROM Pret WHERE compte_adherent='%s' AND id_exemplaire=%d AND date_pret='%s';" %(secu_adherent,exemplaire_a_preter,str(datetime.date.today()))
				cur.execute(sql)
				res = cur.fetchall()
				print(res)
				print("Enregistré avec succès")

			# reserver
			elif preter_ou_reserver == '2' :
				# verifier depuis quelle date on peut l'emprunter
				# affiche tous les livres (disponibles et non-disponibles)
				sql = "SELECT L.res_code,R.titre,E.id,E.disponible FROM Livre L,Ressource R,Exemplaire E \
					WHERE L.res_code=R.code_unique AND R.code_unique=E.ressource_code\
					ORDER BY E.id;"
				cur.execute(sql)
				res = cur.fetchall()
				print("\nres_code | titre | exemplaire_id | disponible")
				for raw in res :
					print("%d | %s | %d | %d" %(raw[0],raw[1],raw[2],raw[3]))
				# choisir un exemplaire a reserver
				exemplaire_a_reserver = int(input("L'id d'exemplaire vous voulez reserver : "))
				exist = int(0)
				for raw in res :
					if exemplaire_a_reserver == raw[2]:
						exist = int(1)
				while exist != 1 :
					ifcontinuer = input("\nmal id. \n1)ressayer 2)terminer\n")
					if ifcontinuer == '1' :
						exemplaire_a_reserver = int(input("L'id de l'exemplaire que vous voulez réserver : "))
						for raw in res :
							if exemplaire_a_reserver == raw[2]:
								exist = int(1)
					elif ifcontinuer == '2' :
						return
					else :
						return
				# entrer secu d'adherent
				secu_adherent = input("secu d'adherent : ")
				sql = "SELECT nom,prenom FROM Adherent WHERE secu='%s';" %secu_adherent
				cur.execute(sql)
				res = cur.fetchall()	
				while not res :
					ifcontinuer = input("\nmal secu. \n1)ressayer 2)terminer\n")
					if ifcontinuer == '1' :
						secu_adherent = input("secu d'adherent : ")
						sql = "SELECT nom,prenom FROM Adherent WHERE secu='%s';" %secu_adherent
						cur.execute(sql)
						res = cur.fetchall()
					elif ifcontinuer == '2' :
						return
					else :
						return
				# verifier il est disponible ou pas
				sql = "SELECT E.disponible FROM Livre L,Ressource R,Exemplaire E \
					WHERE L.res_code=R.code_unique AND R.code_unique=E.ressource_code\
					AND R.code_unique='%s';" %exemplaire_a_reserver
				cur.execute(sql)
				res = cur.fetchall()
				# peut toujours emprunter (pas encore considerer le cas ou il y a des autres reservations)
				if res[0][0] == 1 :
					# entrer date de pret, doit etre correct maintenant
					date_pret = input("date de pret comme : yyyy-mm-dd : ")
					# verifier la date > today
					date_pret_FormatDate = datetime.datetime.strptime(date_pret, '%Y-%m-%d')
					today = datetime.datetime.now()
					diff_date = int((date_pret_FormatDate - today).days)
					while diff_date <= 0 :
						ifcontinuer = input("\nmal date. \n1)ressayer 2)terminer\n")
						if ifcontinuer == '1' :
							date_pret = input("date de pret comme : yyyy-mm-dd : ")
							date_pret_FormatDate = datetime.datetime.strptime(date_pret, '%Y-%m-%d')
							diff_date = int((date_pret_FormatDate - today).days)
						elif ifcontinuer == '2' :
							return
						else :
							return
					date_pret = str(date_pret)
					# entrer duree de pret
					duree_preter = input("Combien de jour ? (0 < duree <= 180)\n")
					while int(duree_preter) > 180 or int(duree_preter) <= 0 :
						ifcontinuer = input("\nmal duree. \n1)ressayer 2)terminer\n")
						if ifcontinuer == '1' :
							duree_preter = input("Combien de jour ? (<=180)\n")
						elif ifcontinuer == '2' :
							return
						else :
							return
					duree_preter = duree_preter + ' days'
					# INSERT et UPDATE
					sql = "INSERT INTO Pret values('%s',%d,'%s','%s');" %(secu_adherent,exemplaire_a_reserver,date_pret,duree_preter)
					cur.execute(sql)
					# Pas de besoin de le mettre comme indisponible, on le traiter quand il vient ????
					#sql = "UPDATE Exemplaire SET disponible=0 WHERE id=%d;" %exemplaire_a_reserver
					#cur.execute(sql)
					# affiche resultat
					sql = "SELECT * FROM Pret WHERE compte_adherent='%s' AND id_exemplaire=%d AND date_pret='%s';" %(secu_adherent,exemplaire_a_reserver,date_pret)
					cur.execute(sql)
					res = cur.fetchall()
					print(res)
					print("l'enregistrer avec succes")
				# indisponible -> reserver depuis une date (c'est indisponible maintenant)(pas encore considerer le cas ou il y a des autres reservations)
				else :
					# verifier la date_pret+duree
					sql = "SELECT date_pret,duree FROM Pret WHERE id_exemplaire='%s';" %exemplaire_a_reserver
					cur.execute(sql)
					res = cur.fetchall()
					old_date_pret = res[0][0]
					old_duree = res[0][1]
					print(old_date_pret)
					print(old_duree)
					
					# peut pas avancer
					
					return
					'''
					# entrer date de pret, doit etre correct maintenant
					date_pret = input("date de pret comme : yyyy-mm-dd : ")
					# verifier la date > today
					date_pret_FormatDate = datetime.datetime.strptime(date_pret, '%Y-%m-%d')
					today = datetime.datetime.now()
					diff_date = int((date_pret_FormatDate - today).days)
					while diff_date <= 0 :
						ifcontinuer = input("\nmal date. \n1)ressayer 2)terminer\n")
						if ifcontinuer == '1' :
							date_pret = input("date de pret comme : yyyy-mm-dd : ")
							date_pret_FormatDate = datetime.datetime.strptime(date_pret, '%Y-%m-%d')
							diff_date = int((date_pret_FormatDate - today).days)
						elif ifcontinuer == '2' :
							return
						else :
							return
					date_pret = str(date_pret)
					# entrer duree de pret
					duree_preter = input("Combien de jour ? (0 < duree <= 180)\n")
					while int(duree_preter) > 180 or int(duree_preter) <= 0 :
						ifcontinuer = input("\nmal duree. \n1)ressayer 2)terminer\n")
						if ifcontinuer == '1' :
							duree_preter = input("Combien de jour ? (<=180)\n")
						elif ifcontinuer == '2' :
							return
						else :
							return
					duree_preter = duree_preter + ' days'
					# INSERT et UPDATE
					sql = "INSERT INTO Pret values('%s',%d,'%s','%s');" %(secu_adherent,exemplaire_a_reserver,date_pret,duree_preter)
					cur.execute(sql)
					# Pas de besoin de le mettre comme indisponible, on le traiter quand il vient ????
					#sql = "UPDATE Exemplaire SET disponible=0 WHERE id=%d;" %exemplaire_a_reserver
					#cur.execute(sql)
					# affiche resultat
					sql = "SELECT * FROM Pret WHERE compte_adherent='%s' AND id_exemplaire=%d AND date_pret='%s';" %(secu_adherent,exemplaire_a_reserver,date_pret)
					cur.execute(sql)
					res = cur.fetchall()
					print(res)
					print("l'enregistrer avec succes")
					'''
			else : 
				return
		# emprunter un exemplaire (film)
		elif choix_type == '2' :
			return

		# emprunter un exemplaire (musique)
		elif choix_type == '3' :
			return

		else :
			print("requete termine\n")
			return
		
	elif choix == '2' :
		return
	else :
		print("Vous n'avez pas donne un bon choix, requete termine\n")
	
	# voir tous les descriptions(livre.resume ou film.synopsis)
	# sql = "SELECT * FROM Livre;"
	# cur.execute(sql)
	# res = cur.fetchall()
	# print("\nToutes les infos des livres:")
	# for raw in res:



