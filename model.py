import mysql.connector
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()   #loading env variables

class EtudiantModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user= os.getenv("USERNAME"),
            password=os.getenv("PASSWORD"),
            database='gestion_etudiants'
        )
        self.cursor = self.conn.cursor()


    def creer_table_etudiants(self):
        query = """
        CREATE TABLE IF NOT EXISTS etudiants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(255) NOT NULL,
            prenom VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def ajouter_etudiant(self, nom, prenom, email):
        query = "INSERT INTO etudiants (nom, prenom, email) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (nom, prenom, email))
        self.conn.commit()

    def obtenir_etudiants(self):
        self.cursor.execute("SELECT * FROM etudiants")
        return self.cursor.fetchall()

    def supprimer_etudiant(self, etudiant_id):
        query = "DELETE FROM etudiants WHERE id = %s"
        self.cursor.execute(query, (etudiant_id,))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()