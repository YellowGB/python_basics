# Les fonctions suivantes sont contenues dans le module math
import math

# Power function, retourne le résultat du premier nombre
# augmenté de la puissance du deuxième nombre
# Dans l'exemple ci-dessous, 4 puissance 3 = 64
num = math.pow(4,3)
print(num)

# Arrondi inférieur
num = math.floor(12.64)
print(num)

# Arrondu supérieur
num = math.ceil(12.64)
print(num)

# Valeur absolue (c'est une fonction intégrée qui ne fait pas partie du module math)
num = abs(150)
print(num)
num = abs(-150)
print(num)

# LOGARITHME
# Avec un seul paramètre, retourne le logarithme naturel (népérien) de ce nombre
num = math.log(10)
print(num)
# Avec deux paramètres, retourne le logarithme du premier nombre en base du deuxième
num = math.log(10,2)
print(num)

# Racine carré
num = math.sqrt(9)
print(num)