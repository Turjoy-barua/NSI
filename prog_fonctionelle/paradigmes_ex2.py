# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:59:03 2021

Exercice de transformation de code en utilisant des fonctions
Ici : garder les boucles (ce ne sera pas de la programmation fonctionnelle "pure" mais s'en rapprochera)
Le programme doit retourner les tableaux t3, t4, t5 et t6.

@author: Trebaul-NSI
"""

t = [2,5,7,3,1,6,10]

def cutting(tab):
    middle = (len(tab)//2)
    return tab[:middle], tab[middle:]

def cutting2(tab):
    tab1 = []
    tab2 = []
    middle = len(tab) // 2
    for i in range(middle):
        tab1.append(tab[i])
    for i in range(middle, len(tab)):
        tab2.append(tab[i])
    return tab1, tab2
        

t1, t2 = cutting2(t)
t3, t4 = cutting2(t1)
t5, t6 = cutting2(t2) 

""" t1 = []
for i in range(len(t)//2):
    t1.append(t[i])

t2 = []
for i in range(len(t)//2, len(t)):
    t2.append(t[i])

t3 = []
for i in range(len(t1)//2):
    t3.append(t1[i])
    
t4 = []
for i in range(len(t1)//2, len(t1)):
    t4.append(t1[i])

t5 = []
for i in range(len(t2)//2):
    t5.append(t2[i])
    
t6 = []
for i in range(len(t2)//2, len(t2)):
    t6.append(t2[i]) """
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)