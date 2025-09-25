class Pile:
    def __init__(self):
        self ._elements = []
    def empiler(self, element):
        self._elements.append(element)
    def depiler(self):
        if self.est_vide():
            raise IndexError("Impossible de dépiler une pile vide")
        return self._elements.pop()
    def sommet (self):
        if self. est_vide():
            raise IndexError ("Pile vide")
        return self ._elements[-1]
    def est_vide(self) :
        return len(self._elements) == 0
    def taille(self):
        return len(self._elements)
    def __str__(self) :
        if self.est_vide():
            return "Pile vide"
        return f"Pile: {' <- '.join(map(str, reversed(self._elements) ))}"
    
def decimal_ver_binaire(nombre):
    if nombre == 0:
        return("0")
    pile = Pile()
    while nombre > 0:
        pile.empiler(str(nombre%2))
        nombre //= 2
    decimal = ""
    while not pile.est_vide():
        decimal += pile.depiler()
    return(decimal)


print(decimal_ver_binaire(10))
print(decimal_ver_binaire(25))
print(decimal_ver_binaire(0))
