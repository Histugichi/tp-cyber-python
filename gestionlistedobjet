class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_details(self):
        print(f"Nom: {self.nom}, Age: {self.age}")


class ListePersonnes:
    def __init__(self):
        self.liste_personnes = []

    def ajouter_personne(self, nom, age):
        personne = Personne(nom, age)
        self.liste_personnes.append(personne)

    def afficher_personnes(self):
        print("Liste des personnes:")
        for personne in self.liste_personnes:
            personne.afficher_details()

    def rechercher_personne(self, nom):
        for personne in self.liste_personnes:
            if personne.nom == nom:
                personne.afficher_details()
                return
        print("Personne non trouvée.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        print(f"Personnes âgées entre {min_age} et {max_age} :")
        for personne in self.liste_personnes:
            if min_age <= personne.age <= max_age:
                personne.afficher_details()


class FileAttente:
    def __init__(self):
        self.file_attente = []

    def ajouter_personne_en_attente(self, nom):
        self.file_attente.append(nom)

    def supprimer_personne_de_attente(self):
        if self.file_attente:
            personne_supprimee = self.file_attente.pop(0)
            print(f"{personne_supprimee} a été supprimé ")
        else:
            print("File d'attente vide.")


class SalleCinema:
    def __init__(self, capacite):
        self.capacite = capacite
        self.places_reservees = {}

    def reserver_place(self, nom, place):
        if len(self.places_reservees) < self.capacite:
            self.places_reservees[nom] = place
            print(f"{nom} a réservé la place {place}.")
        else:
            print("no disponible")

    def afficher_places_reservees(self):
        print("reserve:")
        for nom, place in self.places_reservees.items():
            print(f"{nom}: Place {place}")

    def nombre_places_disponibles(self):
        return self.capacite - len(self.places_reservees)

    def filtrer_reservations_par_personne(self, nom):
        print(f" {nom}:")
        for personne, place in self.places_reservees.items():
            if personne == nom:
                print(f"Place {place}")

    def annuler_reservation(self, nom):
        if nom in self.places_reservees:
            del self.places_reservees[nom]
            print(f"Réservations de {nom} annulées.")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

    def reserver_place_speciale(self, nom):
        if len(self.places_reservees) < self.capacite:
            place_speciale = f"Spéciale-{len(self.places_reservees) + 1}"
            self.places_reservees[nom] = place_speciale
            print(f"{nom} a réservé la place spéciale {place_speciale}.")
        else:
            print("Plus de places spéciales disponibles.")