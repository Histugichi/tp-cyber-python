import mysql.connector as mysql

class ListePersonnes:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connect(
            user= "root", 
            host= "localhost",
            password= "",
            database="miniprojet"

        )
        requete = self.cursor()
        requete.execute ("select * from liste_personne")
        result = requete.fetchall()

    def ajouter_personne(self, nom, age):
        query = "INSERT INTO Personnes (nom, age) VALUES (%s, %s)"
        values = (nom, age)
        self.cursor.execute(query, values)
        self.conn.commit()

    def afficher_personnes(self):
        query = "SELECT * FROM Personnes"
        self.cursor.execute(query)
        personnes = self.cursor.fetchall()
        for personne in personnes:
            print(f"Nom: {personne[1]}, Age: {personne[2]}")

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    liste_personnes = ListePersonnes(user="root", host="localhost", password="", database="miniprojet")

    # Ajouter une personne
    liste_personnes.ajouter_personne()

    # Afficher toutes les personnes
    liste_personnes.afficher_personnes()