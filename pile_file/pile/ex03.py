
class Pile:
    def __init__(self):
        self ._elements = []
    def empiler(self, element):
        self._elements. append (element)
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
    
def separe_assiettes(pile_assiettes, assiette_recherchee):
    pile_retirees = Pile()
    
    while not pile_assiettes.est_vide():
        assiette = pile_assiettes.depiler()
        if assiette == assiette_recherchee:
            pile_assiettes.empiler(assiette)
            return pile_assiettes, pile_retirees
        else:
            pile_retirees.empiler(assiette)
    return pile_assiettes
