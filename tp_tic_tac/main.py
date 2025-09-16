import random
import os

class Personnage:
    def __init__(self, nb_pv):
         self.pv = nb_pv
    def perdVie(self, pointsPerdus):
        self.pv = self.pv - pointsPerdus
    def donneEtat(self):
        return self.pv
    def attaque(self, ennimie, force):
        if random.random() > 0.5:
            degats = 1 * force 
        else:
            degats = 2 * force
        ennimie.perdVie(degats)

tic = Personnage(40)         
tac = Personnage(40)
tic_win = 0
tac_win = 0
name = ""
fight = False

def start():
    global fight
    starting = input("do you want to start the game? y/n ")
    if starting.lower() == "y":
            os.system('cls' if os.name == 'nt' else 'clear') # to clear the screen so that its looks cool
            print(f"tic = {tic.donneEtat()}pv \ntac = {tac.donneEtat()}pv")
            fight = True
    elif starting.lower() == "n":
            fight =  False

def finish():
    user = input("you want to end the game? y/n ")
    if user.lower() == "y":
        os.system('cls' if os.name == 'nt' else 'clear') # to clear the screen so that its looks cool
        print(f"tic won {tic_win} times and tac won {tac_win} times")
        return True
    elif user.lower() == "n":
        tic.pv = 40
        tac.pv = 40
        return False

    
# initializing game
start()
while fight:
    force = int(input("force for tac: ")) # force that can multiply with degats
    tac.attaque(tic, force)
    tic.attaque(tac, random.randrange(1,2)) # playing with computer 
    os.system('cls' if os.name == 'nt' else 'clear') # to clear the screen so that its looks cool
    print(f"tic = {tic.donneEtat()}pv \ntac = {tac.donneEtat()}pv")
    if tac.donneEtat() <= 0:
        print(f"the winner is tic with {tic.donneEtat()} points")
        tic_win+=1
        if finish():
            fight= False
    elif tic.donneEtat() <= 0:
        print(f"the winner is tac with {tac.donneEtat()} points")
        tac_win+=1
        if finish():
            fight= False
    
    