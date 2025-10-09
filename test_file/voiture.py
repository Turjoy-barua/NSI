class Voiture():
    def __init__(self, marque, vitesse):
        self.marque = marque
        self.vitesse = vitesse
    def accelerer(self):
        self.vitesse+= 10
    def ralentir(self):
        self.vitesse-=10
    def afficheEtat(self):
        print(f"{self.marque} spped is {self.vitesse}")
        
renault = Voiture("renault", 90)
renault.accelerer()
renault.accelerer()
renault.ralentir()
renault.afficheEtat()