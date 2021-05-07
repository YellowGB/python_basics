# Ecrire un algorithme qui compare a et b.
# Si a plus petit que b afficher "a est plus petit que b"
# Si b plus petit que a afficher "b est plus petit que a"
# Sinon... ?
# Si on a a=4 et b=5 ?
# Si on a a=8 et b=2?
# Si on a a=4 et b=4?

print("Comparons deux nombres.")
try:
    a = int(input("Entrer nombre 1 : "))
    b = int(input("Entrer nombre 2 : "))

    if a < b:
        print("a est plus petit que b")
    elif a == b:
        print("a est égal à b")
    else:
        print("b est plus petit que a")

except ValueError as ex:
    print("Ceci n'est pas un nombre (",ex,")")

"""
a = input("Entrer nombre 1 : ")
b = input("Entrer nombre 2 : ")

if a.isnumeric() and b.isnumeric():
    if a < b:
        print("a est plus petit que b")
    elif a == b:
        print("a est égal à b")
    else:
        print("b est plus petit que a")
else:
    print("Merci d'entrer des nombres")
"""

# Algorithme pour transférer les valeurs entre deux variables
# Ne fonctionne qu'avec des nombres entiers

print("Transférons les valeurs d'une variable à une autre.")
a = int(input("Entrer une valeur pour a : "))
b = int(input("Entrer une valeur pour b : "))

print("a = ",a)
print("b = ",b)

a = a + b
b = a - b
a = a - b

print("Après transfert :")

print("a = ",a)
print("b = ",b)

# Même exercice qu'au dessus mais qui fonctionne avec n'importe quel type de valeur

print("Transférons les valeurs d'une variable à une autre.")
a = input("Entrer une valeur pour a : ")
b = input("Entrer une valeur pour b : ")
buffer = a

print("a = ",a)
print("b = ",b)

a = b
b = buffer

print("Après transfert :")

print("a = ",a)
print("b = ",b)

# Appeler une fonction depuis un autre fichier (module, bibliothèque)

from custom_functions import addNumbers

print("1 + 5 = ",addNumbers(1,5))