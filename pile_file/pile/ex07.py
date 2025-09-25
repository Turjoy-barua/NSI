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
def evaluer_npi(expression):
    pile = Pile()
    for char in expression:
        if char in "0123456789":
            pile.empiler(int(char))
        elif char in "+-*/":
            a = pile.depiler()
            b = pile.depiler()
            if char == "+":
                pile.empiler(a+b)
            elif char == "-":
                pile.empiler(a-b)
            elif char == "*":
                pile.empiler(a*b)
            elif char == "/":
                pile.empiler(a//b)
    return(pile.sommet())
print(evaluer_npi("3 4 +"))
print(evaluer_npi("3 4 + 2 *"))
