# STRING FUNCTIONS

# Mettre la première lettre en majuscule et le reste en minuscule
# La valeur de str reste inchangée, la fonction renvoie une autre string
str = "here I Am."
print(str.capitalize())
print(str)

# Compter le nombre d'occurence de la substring spécifiée
print(str.count("e"))
print(str.count("Am."))

# Trouver la localisation de la première occurence de la substring s'il y en a
# L'index (la localisation) commence toujours à 0 (-1 si aucune occurence)
a = str.find("h")
print(a)
a = str.find("I")
print(a)
a = str.find("d")
print(a)

# Concatenation
# Ici, str contient le séparateur utilisé pour la concaténation de la chaîne de caractères
str = ""
iter = ("Je","teste","la","concatenation")
a = str.join(iter)
print(a)

str = " "
iter = ("Je","teste","la","concatenation")
a = str.join(iter)
print(a)

str = "JE "
iter = "teste"
a = str.join(iter)
print(a)