# modifier leur description(livre.resume ou film.synopsis)

def modifier_description(conn):
	cur = conn.cursor()
	
	# voir tous les descriptions(livre.resume ou film.synopsis)
	sql = "SELECT * FROM Livre;"
	cur.execute(sql)
	res = cur.fetchall()
	print("\nToutes les infos des livres:")
	for raw in res:
		print(raw)

	sql = "SELECT * FROM Film;"
	cur.execute(sql)
	res = cur.fetchall()
	print("\nToutes les infos des films:")
	for raw in res:
		print(raw)

	choice = input("\n1) Modifier un des resumes des livres.\
			\n2) Modifier une des synopsis des films.\n")
	
	if choice == '1':
		livre_a_modifier = input("Code unique du livre?\n")
		if not livre_a_modifier.isdigit() :
			print("Vous n'avez pas bien donne le code unique, requete termine.\n")
		else:
			sql = "SELECT res_code FROM Livre WHERE res_code=%d;" % int(livre_a_modifier)
			cur.execute(sql)
			res = cur.fetchall()
			# s'il existe
			if res :
				nouveau_resume = input("Pour livre %d, le nouveau resume est :\n" % int(livre_a_modifier))
				sql = "UPDATE Livre SET resume='%s' WHERE res_code=%d;" % (nouveau_resume,int(livre_a_modifier))
				cur.execute(sql)
				print("Fin de modifier le resume")
			# s'il n'existe pas
			else:
				print("Cette ressource n'existe pas, requete termine.\n")

	elif choice == '2':
		film_a_modifier = input("Code unique du film?\n")
		if not film_a_modifier.isdigit() :
			print("Vous n'avez pas bien donne le code unique, requete termine.\n")
		else:
			sql = "SELECT res_code FROM Film WHERE res_code=%d;" % int(film_a_modifier)
			cur.execute(sql)
			res = cur.fetchall()
			# s'il existe
			if res :
				nouveau_synopsis = input("Pour film %d, la nouvelle synopsis est :\n" % int(film_a_modifier))
				sql = "UPDATE Film SET synopsis='%s' WHERE res_code=%d;" % (nouveau_synopsis,int(film_a_modifier))
				cur.execute(sql)
				print("Fin de modifier la synopsis")
			# s'il n'existe pas
			else:
				print("Cette ressource n'existe pas, requete termine.\n")
	else:
		print("Vous n'avez pas donne un bon choix, requete termine\n")

