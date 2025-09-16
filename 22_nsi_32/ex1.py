
def recherche(elt, tab):
    index = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            index = i
    return index

print(recherche(1, [2, 3]))
print(recherche(1, [2, 3, 1]))
