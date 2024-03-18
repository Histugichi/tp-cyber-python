from Librairie import Librairie
from Livre import Livre

# Creating a library object
librairie = Librairie()

#menu controle de saisi
def menu():
    while True:
        print("Menu:")
        print("1. Créer un livre")
        print("2. Ajouter un livre dans la librairie")
        print("3. Chercher un livre")
        print("4. Supprimer un livre")
        print("5. Afficher tous les livres")
        print("6. Quitter")
        
        choice = input("choix (1-6): ")

        if choice == '1':
            titre = input("Entrez le titre du livre: ")
            auteur = input("Entrez l'auteur du livre: ")
            categorie = input("Entrez la catégorie du livre: ")
            pages = int(input("Entrez le nombre de pages du livre: "))
            livre = Livre(titre, auteur, categorie, pages)
            print("Livre créé avec succès!")
        
        elif choice == '2':
            librairie.ajouter_livre(livre)
            print("Livre ajouté à la librairie avec succès!")

        elif choice == '3':
            titre = input("Entrez le titre du livre à chercher: ")
            librairie.chercher_livre(titre)
        
        elif choice == '4':
            titre = input("Entrez le titre du livre à supprimer: ")
            librairie.supprimer_livre(titre)
            print("Livre supprimé avec succès!")

        elif choice == '5':
            librairie.afficher_librairie()
        
        elif choice == '6':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")
menu()
