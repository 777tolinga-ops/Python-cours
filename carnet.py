nom_etudiant = "Timothee"
note_1 = 11.5
note_2 = 8
note_3 = 13

print("etudiant : ", nom_etudiant)
print("Notes : ", note_1, note_2, note_3)
#calculs
nombre_de_notes = 3
somme_des_notes = note_1 + note_2 + note_3
moyenne = somme_des_notes / nombre_de_notes

#compariason : le resultat serq un booleean
est_admis = moyenne >= 10

#affichage des resultats : 
print("Etudiant : ", nom_etudiant)
print("Sommes des notes : ", somme_des_notes)
print("Moyenne : ", moyenne)
print("Admis : ", est_admis)

# verification du typage
print("Type de 'nom_etudiant' : ", type(nom_etudiant))
print("Type de 'somme_des_notes' : ", type(somme_des_notes))
print("Type de 'moyenne' : ", type(moyenne))
print