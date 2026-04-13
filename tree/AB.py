# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:39:52 2020
Classe ArbreBinaire avec une fonction d'affichage récursive.
@author: Trebaul-NSI
"""

class ArbreBinaire:
    def __init__(self, racine, agauche, adroit):
        self.racine = racine
        self.gauche = agauche
        self.droit = adroit
        
    def Affiche(self, space = 0):
        spaces = "  "*space
        print(spaces, self.racine)
        if self.gauche:
            self.gauche.Affiche(space+1)
        if self.droit:
            self.droit.Affiche(space+1)
            
            

