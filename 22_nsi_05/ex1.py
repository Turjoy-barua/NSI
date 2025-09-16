def rechercheMinMax(tab):
    if not tab:
        return {'min': None, 'max': None}       
    min = tab[0]
    max = tab[0]
    for x in tab:
        if x < min:
            min = x
        if x > max:
            max = x
    return {'min': min, 'max': max}

tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
tableau2 = []

resultat1 = rechercheMinMax(tableau)
resultat2 = rechercheMinMax(tableau2)
print(resultat1)
print(resultat2)