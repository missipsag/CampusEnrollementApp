from model import EtudiantModel
from view import EtudiantView
from tkinter import messagebox

class EtudiantController:
    def __init__(self):
        self.model = EtudiantModel()
        self.view = EtudiantView(self)
        self.model.creer_table_etudiants()
        self.afficher_etudiants()

    def ajouter_etudiant(self, nom, prenom, email):
        try:
            self.model.ajouter_etudiant(nom, prenom, email)
            self.afficher_etudiants()
            self.view.nom_var.set("")
            self.view.prenom_var.set("")
            self.view.email_var.set("")
            messagebox.showinfo("Succès", "Étudiant ajouté avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    def supprimer_etudiant(self, etudiant_id):
        try:
            self.model.supprimer_etudiant(etudiant_id)
            self.afficher_etudiants()
            messagebox.showinfo("Succès", "Étudiant supprimé avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

    def afficher_etudiants(self):
        etudiants = self.model.obtenir_etudiants()
        self.view.afficher_etudiants(etudiants)

    def run(self):
        self.view.start()
