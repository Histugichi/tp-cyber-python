# Nombre 
nombre_etudiants = int(input("nombre d'etudiants : "))

#liste des etudiants
etudiants = []

# Saisie des noms et notes 
for i in range(nombre_etudiants):
    nom = input("nom de l'etudiant {} : ".format(i+1))
    note = int(input("la note de l'etudiant {} : ".format(i+1)))
    etudiants.append({"nom": nom, "note": note})
# note supérieure ou égale à 10
print("note supérieure ou égale à 10 :")
for etudiant in etudiants:
    if etudiant["note"] >= 10:
        print(etudiant["nom"])
