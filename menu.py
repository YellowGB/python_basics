# Importer de cette manière plutôt que de faire
# un import custom_functions permet
# d'appeler les fonctions directement sans avoir
# à les appeler de la forme custom_functions.nomFonction
from custom_functions import *

menu = """
Indiquez votre sélection :
    1 - addition
    2 - soustraction
    3 - hello world
    0 - sortie
"""

print(menu)
choix = int(input())

while choix != 0:
    if choix == 1:
        print("4 + 5 = ",addNumbers(4,5))
    elif choix == 2:
        print("1 - 5 = ",substractNumbers(1,5))
    elif choix == 3:
        helloWorld()
    else:
        print("choix inconnu")
    print(menu)
    choix = int(input())

print("Merci, à la prochaine !")