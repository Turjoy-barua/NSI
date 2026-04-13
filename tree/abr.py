# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:21:05 2021
Représentation d'un arbre binaire de recherche avec deux classes.
@author: Trebaul-NSI
"""

class ABR:
    def __init__(self, racine = None):
        self.racine = racine
    
    def affiche_abr(self):
        if self is None:
            representation = "L'arbre est vide !"
        else:
            representation = self.racine.affiche()
        return representation
        

class Noeud:
    def __init__(self, valeur, fils_gauche = None, fils_droit = None):
        self.valeur = valeur
        self.fils_gauche = fils_gauche
        self.fils_droit = fils_droit
        
    def affiche(self, space = 0):
        spaces = "  "*space
        print(spaces, self.valeur)
        if self.fils_gauche:
            self.fils_gauche.affiche(space+1)
        if self.fils_droit:
            self.fils_droit.affiche(space+1)
        