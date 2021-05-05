# Comme pour le reste en Python, l'index d'une liste commence à 0
list1 = [2,4,5,6,7,2] # 2 = index 0, 4 = index 1, 5 = index2, etc.
# Une liste peut contenir plusieurs types de données
list2 = [4,"hi",6,"Me",78]

# L'accès à une liste se fait par le nom de la liste
# suivi de l'index de la valeur entre crochets
print(list2[1])

# Accès à de multiple index
# Comme pour for, le premier index est inclusif et le dernier est exclusif
print(list1[1:4]) # Donc ici afficher l'index 1, 2 et 3

# Toute la liste
print(list2)
# ou
print(list2[:])

# De 0 à x
print(list1[:5]) # Ici, index 0 à 4

# De x à la fin
print(list2[2:])

# Update l'item d'une liste
list2[4] = 88
print(list2)

# Ajouter un item à la fin d'une liste
list2.append(150)
print(list2)

# Supprimer un item d'une liste
# Depuis l'index
del list2[3]
print(list2)
# Depuis la valeur
list2.remove("hi")
print(list2)