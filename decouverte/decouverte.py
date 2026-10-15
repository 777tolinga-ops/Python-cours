#operateurs arithmetiques
print("7 + 2 = ", 7 + 2)
print("7 -2 = ", 7 - 2)
print("7 * 2 = ", 7 * 2)
print("7 / 2 = ", 7 / 2)
print("7 % 2 = ", 7 % 2)

# priorite des operateurs
print("7 + 2 * 3 = ", 7 + 2 * 3)
print("(7 + 2) * 3 = ", (7 + 2) * 3)

# comparaison : resultat boolean
print("7 > 2 = ", 7 > 2)
print("7 < 2 = ", 7 < 2)
print("7 == 2 = ", 7 == 2)
print("7 != 2 = ", 7 != 2)

# arrondi et conversion de type
print("Arrondi de 34.6785 : ", round(34.6785, 2))
print("Conversion de type : ", float(34))

# aberration de type : flottant
print("0.1 + 0.2 = ", 0.1 + 0.2)
input("coucou")
age_saisi = input("Quel est ton age ?")
print("Dans deux ans tu auras : ", int(age_saisi) + 2)

prix = round(float(input("Quel est le prix du produit ? ")), 2)
prix_formate = str(prix).replace(".", ",")
print("Prix TTC : ", prix_formate, "$")

#formater avec f-strings
print(f"Prix TTC : {prix_formate} $")

nom = "Melvin"
moyenne = 12.5
nombres_de_notes = 3
print(f"Nom : {nom}, Moyenne : {moyenne}, Nombre de notes : {nombres_de_notes}")
print(f"Nom : {nom}, Moyenne : {moyenne:.2f}, Nombre de notes : {nombres_de_notes}")

print(f"Nom : {nom:>10}, Moyenne : {moyenne:.2f}, Nombres de notes : {nombres_de_notes}")

#les caracteres d'echappement
print("Ceci est une ligne\nceci est une autre ligne")

#tabulation
print("nom\tMoyenne\tNombres de notes")

# guillements : \" et \'
print("Il a dit : \" Bonjour !\"")
