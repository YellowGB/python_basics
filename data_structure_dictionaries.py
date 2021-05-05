# Structuration d'un dictionary
dict1 = {
    'name' : 'xyz',
    'age' : 25,
    'hobby' : 'Dancing'
}

# On accède aux valeurs par leurs clés
print(dict1['age'])

# Afficher tous les items
# Les données ne seront pas forcément affichées dans l'ordre car un dictionaire,
# contrairement à une liste par exemple, n'ont pas d'ordre défini
print(dict1)

# Update
dict1['name'] = 'abc'
print(dict1)

# Pour ajouter une valeur, il suffit d'utiliser une clé qui n'est pas encore utilisée
# et lui assigner une valeur
dict1['profession'] = 'pilot'
print(dict1)

# Supprimer un item individuellement
del dict1['name']
print(dict1)

# Vider le dictionnaire sans pour autant le supprimer
dict1.clear()
print(dict1)

# Supprimer le dictionnaire entier, qu'il soit vide ou non
del dict1