# Ecrire un algorithme qui compare a et b.
# Si a plus petit que b afficher "a est plus petit que b"
# Si b plus petit que a afficher "b est plus petit que a"
# Sinon... ?
# Si on a a=4 et b=5 ?
# Si on a a=8 et b=2?
# Si on a a=4 et b=4?

try:
    a = int(input("Entrer nombre 1 : "))
    b = int(input("Entrer nombre 2 : "))

    if a < b:
        print("a est plus petit que b")
    elif a == b:
        print("a est égal à b")
    else:
        print("b est plus petit que a")

except:
    print("Ceci n'est pas un nombre")

"""
a = input("Entrer nombre 1 : ")
b = input("Entrer nombre 2 : ")

if a.isnumeric() and b.isnumeric():
    if int(a) < int(b):
        print("a est plus petit que b")
    elif int(a) == int(b):
        print("a est égal à b")
    else:
        print("b est plus petit que a")
else:
    print("Merci d'entrer des nombres")
"""