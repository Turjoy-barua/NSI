def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat
def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return (inverse == chaine)
def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre
    est un palindrome'''
    chaine = str(nbre)
    return est_palindrome(chaine)


# Tests pour inverse_chaine
print(inverse_chaine("bonsoir")) # doit afficher "riosob"
print(inverse_chaine("python")) # doit afficher "nohtyp"
# Tests pour est_palindrome
print(est_palindrome("radar")) # doit afficher True
print(est_palindrome("python")) # doit afficher False
print(est_palindrome("kayak")) # doit afficher True
# Tests pour est_nbre_palindrome
print(est_nbre_palindrome(121)) # doit afficher True
print(est_nbre_palindrome(123)) # doit afficher False
print(est_nbre_palindrome(1331)) # doit afficher True