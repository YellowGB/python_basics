import random

roulette = random.randint(1,100)

choix = int(input("Choisir un nombre entre 1 et 100 : "))

while choix != roulette:
    if choix < roulette:
        print("T’en en dessous !")
    else:
        print("T’es au-dessus !")
    
    choix = int(input("Essaie encore : "))

print("C’est gagné !")