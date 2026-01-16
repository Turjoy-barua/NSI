 
    
    
# Création d'une pile
pile = Pile()
print(pile)  # Pile vide

# Ajout d'éléments
pile.empiler(1)
pile.empiler(5)
pile.empiler(3)
print(pile)  # Pile: 3 <- 5 <- 1
# Consultation du sommet
print(pile.sommet())  # 3

# Retrait d'éléments
print(pile.depiler())  # 3
print(pile.depiler())  # 5
print(pile)  # Pile: 1 <- 

# Vérification
print(pile.taille())  # 1
print(pile.est_vide())  # False