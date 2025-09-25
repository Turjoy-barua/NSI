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

def expression(expression):
    pile = Pile()
    for x in expression:
        if x in "[(":
            pile.empiler(x)
        elif x == ")":
            if pile.est_vide() or pile.sommet() != "(":
                return False
            pile.depiler()
        elif x == "]":
            if pile.est_vide() or pile.sommet() != "[":
                return False
            pile.depiler()
    return(pile.est_vide())      