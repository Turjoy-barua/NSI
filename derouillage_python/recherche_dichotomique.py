def dichotomie(tab, x):
    """Applique une recherche dichotomique pour déterminer
    si x est dans le tableau trié tab.
    La fonction renvoie True si tab contient x et False sinon"""
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (fin + debut) // 2
        print(f"m = {m}")
        print(f"fin = {fin}, debut {debut}")
        print(f"tab element {tab[m]}\n")
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False


# Tests avec différents tableaux
tab1 = [1, 3, 5, 7, 9, 11, 13, 15]
""" print(dichotomie(tab1, 7)) # doit afficher True
print(dichotomie(tab1, 4)) # doit afficher False
print(dichotomie(tab1, 1)) # doit afficher True (premier élément) """
print(dichotomie(tab1, 15)) # doit afficher True (dernier élément)
""" print(dichotomie(tab1, 16)) # doit afficher False
tab2 = [10, 20, 30, 40, 50]
print(dichotomie(tab2, 30)) # doit afficher True
print(dichotomie(tab2, 25)) # doit afficher False """