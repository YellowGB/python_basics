# Ecrire un algorithme qui accepte un mot d'un utilisateur
# et retourne le mot en inversant les lettres
mot = input("Entrer un mot : ")

print("L'inverse de ",mot," est ",''.join(reversed(mot)))

# Solution alternative

print("L'inverse de ",mot," est ",mot[::-1])

# Ecrire une fonction qui trouve le maximum entre 3 nombres

num1 = int(input("Entrer un premier nombre : "))
num2 = int(input("Entrer un deuxième nombre : "))
num3 = int(input("Entrer un troisième nombre : "))

print("Le numéro le plus grand est ",max(num1,num2,num3))

# Solution alternative

num = []

num.append(int(input("Entrer un premier nombre : ")))
num.append(int(input("Entrer un deuxième nombre : ")))
num.append(int(input("Entrer un troisième nombre : ")))

print("Le numéro le plus grand est ",max(num))

# Calcul de la somme des n premiers entiers (1+2+3…+n)

n = int(input("Entrer un nombre entier : "))
somme = 0

for i in range(0,n+1):
    somme = somme + i

print("La somme des entiers de 1 à ",n," est ",somme)

# Solution alternative

n = int(input("Entrer un nombre entier : "))
numbers = range(1,n+1)

resultat = sum(numbers)

print("La somme des entiers de 1 à ",n," est ",resultat)

# Ecrire un programme qui affiche une pyramide
# et qui prend le nombre maximal de colonne en paramètre.
# La pyramide ressemblera à ça:
# *
# * *
# * * *
# * * * *
# * * * * *

col = int(input("Entrer la taille de la pyramide : "))

for i in range(0,col+1):
    print(i*'*')

# Solution alternative

col = int(input("Entrer la taille de la pyramide : "))

for i in range(0,col+1):
    print(''.join('*'*i))