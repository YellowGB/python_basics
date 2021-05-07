# Lire un nombre saisi par l’utilisateur et afficher son carré
"""
nombre = int(input("Veuillez saisir un nombre : "))

nombre = nombre * nombre

print(nombre)
"""
# Jeu du nombre mystère
nombre_mystere = 90

saisie = int(input("Saisissez une valeur entre 1 et 100: "))

while saisie != nombre_mystere:
    if saisie < nombre_mystere:
        print("Le nombre à trouver est supérieur.")
    else:
        print("Le nombre à trouver est inférieur.")
    saisie = int(input("Saisissez une valeur entre 1 et 100: "))
if saisie == nombre_mystere:
    print("C'est gagné !")