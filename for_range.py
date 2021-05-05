for num in range(1,101): # Nombre de répétitions +1 car la dernière valeur est exclue (mais la première est inclue)
    print(num)
    
# Si une seule valeur est indiquée dans range(), il partira de 0 jusqu'à la valeur indiquée
# range(100) = range(0,100)
#
# Un troisième paramètre est possible, le nombre de step, par défaut il est de 1
# range(0,10,2) retournera [0, 2, 4, 6, 8]

# Afficher les nombres impairs entre 1 et 10
for num in range(1,10,2):
    print(num)