import operations

#saisir deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Utiliser les fonctions du module pour effectuer des opérations
resultat_addition = operations.addition(nombre1, nombre2)
print("Résultat de l'addition :", resultat_addition)

resultat_multiplication = operations.multiplication(nombre1, nombre2)
print("Résultat de la multiplication :", resultat_multiplication)