import mysql.connector as mysql
connexion = mysql.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "ecole",

)
requete = connexion.cursor()
requete.execute ("select * from étudiant")
result = requete.fetchall()
print(result)
for re in result:
    print(re)