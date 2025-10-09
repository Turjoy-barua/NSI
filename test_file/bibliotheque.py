class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True  # par défaut, le livre est disponible

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible.")

    def rendre(self):
        if not self.disponible:
            self.disponible = True
            print(f"Le livre '{self.titre}' a été rendu.")
        else:
            print(f"Le livre '{self.titre}' est déjà disponible.")

    def __str__(self):
        # cette méthode permet d'afficher joliment un livre avec print()
        etat = "disponible" if self.disponible else "emprunté"
        return f"'{self.titre}' de {self.auteur} ({etat})"


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté à la bibliothèque.")

    def afficher_livres(self):
        print("\nListe des livres :")
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
        else:
            for livre in self.livres:
                print(" -", livre)

    def rechercher(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None

    def emprunter(self, titre):
        livre = self.rechercher(titre)
        if livre:
            livre.emprunter()
        else:
            print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

    def rendre(self, titre):
        livre = self.rechercher(titre)
        if livre:
            livre.rendre()
        else:
            print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")
