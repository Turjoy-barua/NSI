class CompteBancaire():
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde
    def deposer(self, montant):
        self.solde += montant
    def retirer(self, montant):
        if not (self.solde - montant) < 0:
            self.solde -= montant
    def virement(self, autre_compte, montant):
        autre_compte.solde += montant
        self.solde -= montant
    def afficher_solde(self):
        print(f"in the bank account of {self.titulaire} theres left {self.solde}")
        


user1 = CompteBancaire("turjoy", 1000)
user1.deposer(2000)
user1.retirer(100)
user1.afficher_solde()


user2 = CompteBancaire("newton", 1000)
user2.deposer(5000)
user2.retirer(2500)
user2.virement(user1, 1000)
user2.afficher_solde()