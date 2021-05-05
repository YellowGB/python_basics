# Fonctionnement de base identique à celui des listes
tuple1 = (2,4,5,6,7,2)
tuple2 = (4,"hi",6,"Me",78)

print(tuple2[1])
print(tuple1[1:4])

# Contrairement aux listes, les tuples sont immuables,
# donc ni updates ni suppressions de valeurs
# On peut, en revanche, supprimer l'entièreté d'un tuple
del tuple1