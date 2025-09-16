from random import randint, random
import time

# Code sans commentaires, fait à l'arrache - à ne pas reproduire comme tel !
# (C'est important, les commentaires)
class Personnage:
    def __init__(self, name, pv, dgts, armure, speed, special=None, crit=0.2):
        self.name = name
        self.pv = pv
        self.dgts = dgts
        self.armure = armure
        self.speed = speed
        self.crit = crit
        if special:
            self.spc = special
        else:
            r = randint(0,10)
            if r == 0:
                self.spc = "classique"
            elif r < 5 :
                self.spc = "de feu"
            else:
                self.spc = "de métal"
    def perdVie(self, pv):
        self.pv -= pv

    def estMort(self):
        return self.pv <= 0

    def getName(self):
        return self.name + " " + self.spc

    def getCrit(self):
        return self.crit

    def getDgts(self):
        return self.dgts

    def donneEtat(self):
        return self.pv

    def afficheEtat(self):
        return str(self.donneEtat())

    def getSpc(self):
        return self.spc

    def attaque(self, ennemi):
        if ennemi.getSpc() == "de métal":
            block = max(ennemi.bloque(), ennemi.bloque()) + 1
        else:
            block = ennemi.bloque()
        if random() <= self.getCrit():
            if self.getSpc() == "de feu":
                degats = self.getDgts() * 4 - block
            else:
                degats = self.getDgts() * 2 - block
            print("CRITICAL !")
        else:
            degats = self.getDgts() - block
        print("--- " + self.getName() + " hits " + ennemi.getName() + " for " + str(degats) + " (" + ennemi.getName() + " blocks " + str(block) + ").")

        ennemi.perdVie(degats)

    def bloque(self):
        return randint(0, self.armure)

    def speedCheck(self):
        return randint(0, self.speed)

    def victory(self):
        print(self.getName() + " WON WITH " + self.afficheEtat() + " HP LEFT !")

    def fight(self, ennemi):
        roundNb = 1
        while not (self.estMort() or ennemi.estMort()):
            if self.speedCheck() > ennemi.speedCheck():
                player1 = self
                player2 = ennemi
            else:
                player1 = ennemi
                player2 = self

            print("Round # " + str(roundNb) + " - " + self.getName() + " (" + self.afficheEtat() + " hp) vs " + ennemi.getName() + " (" + ennemi.afficheEtat() + " hp).")

            player1.attaque(player2)
            if not player2.estMort():
                player2.attaque(player1)
                if player1.estMort():
                    player2.victory()
            else:
                player1.victory()
            roundNb += 1
            time.sleep(2)



morio = Personnage("Morio", 200, 6, 4, 10)
lonk = Personnage("Lonk", 100, 12, 1, 8)

morio.fight(lonk)
