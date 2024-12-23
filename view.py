import tkinter as tk
from tkinter import messagebox, ttk

class EtudiantView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Gestion des Étudiants")

        # Variables pour les champs
        self.nom_var = tk.StringVar()
        self.prenom_var = tk.StringVar()
        self.email_var = tk.StringVar()

        # UI
        self.setup_ui()

    def setup_ui(self):
        # Formulaire d'ajout
        tk.Label(self.root, text="Nom:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.nom_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Prénom:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.prenom_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Ajouter Étudiant", command=self.ajouter_etudiant).grid(row=3, column=0, columnspan=2, pady=10)

        # Tableau des étudiants
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nom", "Prénom", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prénom", text="Prénom")
        self.tree.heading("Email", text="Email")
        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.root, text="Supprimer Étudiant", command=self.supprimer_etudiant).grid(row=5, column=0, columnspan=2, pady=10)

    def ajouter_etudiant(self):
        nom = self.nom_var.get()
        prenom = self.prenom_var.get()
        email = self.email_var.get()

        if not nom or not prenom or not email:
            messagebox.showwarning("Erreur", "Tous les champs sont obligatoires.")
            return

        self.controller.ajouter_etudiant(nom, prenom, email)

    def supprimer_etudiant(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant à supprimer.")
            return

        etudiant_id = self.tree.item(selected_item, "values")[0]
        self.controller.supprimer_etudiant(etudiant_id)

    def afficher_etudiants(self, etudiants):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for etudiant in etudiants:
            self.tree.insert("", "end", values=etudiant)

    def start(self):
        self.root.mainloop()
