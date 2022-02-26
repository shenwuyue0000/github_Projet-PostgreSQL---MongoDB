# gerer des utilisateur et leur donnee(personnel ou adherent)
# personnel peut rajouter un adherent, modifier l'info d'adherent,
# l'adherent peut seulement modifier son info

def gestion_donnee_utilisateur(conn):
	cur = conn.cursor()
	
	# personnel ou adherent?
	identite = input("personnel=1, adherent=2, vous etes ?\n")
	if identite == '1' :
		login_personnel = input("Votre compte de personnel :\n")
		mdp_personnel = input("Votre mot de passe :\n")
		sql = "SELECT * FROM Compte_Personnel,Personnel WHERE Personnel.login_personnel=Compte_Personnel.login AND login='%s' AND mdp='%s';" %(login_personnel,mdp_personnel)
		cur.execute(sql)
		res = cur.fetchall()
		# login,mdp correct
		if res :
			chose_a_faire=input("\nQu'est-ce que vous voulez faire ?\
				\n1) modifier vos informations (adresse,email,mdp) \
				\n2) ajouter un compte d'adherent et un adherent\
				\n3) modifier l'information d'un adherent\
				\nvotre choix : ")
			if chose_a_faire == '1':
				sql = "SELECT adresse,email FROM Personnel WHERE login_personnel='%s';" %login_personnel
				cur.execute(sql)
				res = cur.fetchall()
				while chose_a_faire != '0':
					print("Votre adresse : ", res[0][0])
					print("Votre email : ", res[0][1])
					chose_a_faire=input("\nQu'est-ce que vous voulez modifier ?\
						\n1) modifier adresse \
						\n2) modifier email\
						\n3) modifier mot de passe\
						\n0) quitter\
						\nvotre choix : ")
					if chose_a_faire == '1':
						nouveau_adresse = input("Votre nouvelle adresse :\n")
						sql = "UPDATE Personnel SET adresse='%s' WHERE login_personnel='%s';" %(nouveau_adresse,login_personnel)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email FROM Personnel WHERE login_personnel='%s';" %login_personnel
						cur.execute(sql)
						res = cur.fetchall()
					elif chose_a_faire == '2':
						nouveau_email = input("Votre nouvel email :\n")
						sql = "UPDATE Personnel SET email='%s' WHERE login_personnel='%s';" %(nouveau_email,login_personnel)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email FROM Personnel WHERE login_personnel='%s';" %login_personnel
						cur.execute(sql)
						res = cur.fetchall()
					elif chose_a_faire == '3':
						nouveau_mdp = input("Votre nouveau mdp :\n")
						sql = "UPDATE Compte_Personnel SET mdp='%s' WHERE login='%s';" %(nouveau_mdp,login_personnel)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email FROM Personnel WHERE login_personnel='%s';" %login_personnel
						cur.execute(sql)
						res = cur.fetchall()
			elif chose_a_faire == '2':
				# create nouveau login d'adherent
				nouveau_compte_adherent_login = input("\nlogin de nouveau compte d'adherent :\n")
				sql = "SELECT login FROM Compte WHERE login='%s';" %nouveau_compte_adherent_login
				cur.execute(sql)
				res = cur.fetchall()
				# deje existe, ressayer
				while res :
					ressayer = input("\nlogin deja existe\
							\n1) ressayer\
							\n2) exit\n")
					if ressayer == '1':
						nouveau_compte_adherent_login = input("\n[entrer 0 pour quitter]\
							\nlogin de nouveau compte d'adherent :\n")
						sql = "SELECT login FROM Compte WHERE login='%s';" %nouveau_compte_adherent_login
						cur.execute(sql)
						res = cur.fetchall()
					else:
						break
				# entrer le mdp
				nouveau_compte_adherent_mdp = input("mot de passe :\n")
				# creer le compte d'adherent
				sql = "INSERT INTO Compte_Adherent values('%s','%s');" %(nouveau_compte_adherent_login,nouveau_compte_adherent_mdp)
				cur.execute(sql)
				# verifier OK ou pas
				sql = "SELECT * FROM Compte_Adherent WHERE login='%s';" %nouveau_compte_adherent_login
				cur.execute(sql)
				res = cur.fetchall()
				if res :
					print("creer avec succes\n")
				else :
					print("erreur\n")
			elif chose_a_faire == '3':
				# info
				print("\nLes adherents :\
					\nnom | prenoms | login\
					\n---------------------")
				sql = "SELECT nom,prenom,login_adherent FROM Adherent;"
				cur.execute(sql)
				res = cur.fetchall()
				for raw in res :
					print("%s | %s | %s" %(raw[0],raw[1],raw[2]))
				login_adherent = input("Quel adherent vous voulez modifier ? Son login :\n")
				# verifier s'il existe				
				sql = "SELECT * FROM Adherent WHERE login_adherent='%s';" %login_adherent
				cur.execute(sql)
				res = cur.fetchall()
				# n'existe pas, ressayer
				while not res :
					ressayer = input("\nlogin n'existe pas\
							\n1) ressayer\
							\n2) exit\n")
					if ressayer == '1':
						login_adherent = input("Quel adherent vous voulez modifier ? Son login :\n")
						sql = "SELECT * FROM Adherent WHERE login_adherent='%s';" %login_adherent
						cur.execute(sql)
						res = cur.fetchall()
					else:
						print("requete termine.\n")
						return
				# existe 
				chose_a_modifier = '1'
				sql = "SELECT adresse,email,telephone,etat FROM Adherent WHERE login_adherent='%s';" %login_adherent
				cur.execute(sql)
				res = cur.fetchall()
				while chose_a_modifier != '0' :
					print("")
					print("Son adresse : ", res[0][0])
					print("Son email : ", res[0][1])
					print("Son telephone : ", res[0][2])
					print("Son etat : ", res[0][3])

					chose_a_modifier = input("\n[entrez 0 pour quitter]\
						\nQu'est-ce que vous voulez modifier?\
						\n1) modifier adresse \
						\n2) modifier email\
						\n3) modifier telephone\
						\n4) modifier etat\
						\n5) modifier mot de passe\
						\n0) quitter\
						\nvotre choix : ")
					if chose_a_modifier == '1':
						nouveau_adresse = input("Sa nouvelle adresse :\n")
						sql = "UPDATE Adherent SET adresse='%s' WHERE login_adherent='%s';" %(nouveau_adresse,login_adherent)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email,telephone,etat FROM Adherent WHERE login_adherent='%s';" %login_adherent
						cur.execute(sql)
						res = cur.fetchall()
					elif chose_a_modifier == '2':
						nouveau_email = input("Son nouvel email :\n")
						sql = "UPDATE Adherent SET email='%s' WHERE login_adherent='%s';" %(nouveau_email,login_adherent)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email,telephone,etat FROM Adherent WHERE login_adherent='%s';" %login_adherent
						cur.execute(sql)
						res = cur.fetchall()
					elif chose_a_modifier == '3':
						nouveau_telephone = input("Son nouveau numero de telephone :\n")
						sql = "UPDATE Adherent SET telephone='%s' WHERE login_adherent='%s';" %(nouveau_telephone,login_adherent)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email,telephone,etat FROM Adherent WHERE login_adherent='%s';" %login_adherent
						cur.execute(sql)
						res = cur.fetchall()
					elif chose_a_modifier == '4':
						nouveau_etat = input("0:desactive, 1:active\n")
						sql = "UPDATE Adherent SET etat='%s' WHERE login_adherent='%s';" %(nouveau_etat,login_adherent)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email,telephone,etat FROM Adherent WHERE login_adherent='%s';" %login_adherent
						cur.execute(sql)
						res = cur.fetchall()
					elif chose_a_modifier == '5':
						nouveau_mdp = input("Son nouveau mdp :\n")
						sql = "UPDATE Compte_Adherent SET mdp='%s' WHERE login='%s';" %(nouveau_mdp,login_adherent)
						cur.execute(sql)
						# renouveler
						sql = "SELECT adresse,email,telephone,etat FROM Adherent WHERE login_adherent='%s';" %login_adherent
						cur.execute(sql)
						res = cur.fetchall()
				return
			else :
				print("Vous n'avez pas donne le bon choix, requete termine.\n")
				return
		# login,mdp erreur
		else :
			print("Login ou mdp erreur, requete termine.\n")

	elif identite == '2' :
		login_adherent = input("Votre login :")
		# verifier s'il existe				
		sql = "SELECT * FROM Compte_Adherent WHERE login='%s';" %login_adherent
		cur.execute(sql)
		res = cur.fetchall()
		# n'existe pas, ressayer
		while not res :
			ressayer = input("\nlogin n'existe pas\
					\n1) ressayer\
					\n2) exit\n")
			if ressayer == '1':
				login_adherent = input("Votre login :")
				sql = "SELECT * FROM Compte_Adherent WHERE login='%s';" %login_adherent
				cur.execute(sql)
				res = cur.fetchall()
			else:
				print("requete termine.\n")
				return
		# existe 
		mdp_adherent = input("Votre mdp :")
		sql = "SELECT adresse,email,telephone FROM Adherent,Compte_Adherent WHERE Adherent.login_adherent=Compte_Adherent.login AND login='%s' AND mdp='%s';" %(login_adherent,mdp_adherent)
		cur.execute(sql)
		res = cur.fetchall()
		
		# login,mdp correct
		if res :
			chose_a_modifier = '1'
			while chose_a_modifier != '0' :
				print("")
				print("Votre adresse : ", res[0][0])
				print("Votre email : ", res[0][1])
				print("Votre telephone : ", res[0][2])

				chose_a_modifier = input("\n[entrez 0 pour quitter]\
					\nQu'est-ce que vous voulez modifier?\
					\n1) modifier adresse \
					\n2) modifier email\
					\n3) modifier telephone\
					\n4) modifier mot de passe\
					\n0) quitter\
					\nvotre choix : ")
				if chose_a_modifier == '1':
					nouveau_adresse = input("Votre nouvelle adresse :\n")
					sql = "UPDATE Adherent SET adresse='%s' WHERE login_adherent='%s';" %(nouveau_adresse,login_adherent)
					cur.execute(sql)
					# renouveler
					sql = "SELECT adresse,email,telephone FROM Adherent WHERE login_adherent='%s';" %login_adherent
					cur.execute(sql)
					res = cur.fetchall()
				elif chose_a_modifier == '2':
					nouveau_email = input("Votre nouvel email :\n")
					sql = "UPDATE Adherent SET email='%s' WHERE login_adherent='%s';" %(nouveau_email,login_adherent)
					cur.execute(sql)
					# renouveler
					sql = "SELECT adresse,email,telephone FROM Adherent WHERE login_adherent='%s';" %login_adherent
					cur.execute(sql)
					res = cur.fetchall()
				elif chose_a_modifier == '3':
					nouveau_telephone = input("Votre nouveau numero de telephone :\n")
					sql = "UPDATE Adherent SET telephone='%s' WHERE login_adherent='%s';" %(nouveau_telephone,login_adherent)
					cur.execute(sql)
					# renouveler
					sql = "SELECT adresse,email,telephone FROM Adherent WHERE login_adherent='%s';" %login_adherent
					cur.execute(sql)
					res = cur.fetchall()
				elif chose_a_modifier == '4':
					nouveau_mdp = input("Votre nouveau mdp :\n")
					sql = "UPDATE Compte_Adherent SET mdp='%s' WHERE login='%s';" %(nouveau_mdp,login_adherent)
					cur.execute(sql)
					# renouveler
					sql = "SELECT adresse,email,telephone FROM Adherent WHERE login_adherent='%s';" %login_adherent
					cur.execute(sql)
					res = cur.fetchall()
			return
		# login,mdp erreur		
		else :
			print("Login ou mdp erreur, requete termine.\n")
	else :
		print("Vous n'avez pas donne le bon choix, requete termine.\n")

