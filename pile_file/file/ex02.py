class File:
    def __init__(self) :
        self._elements = []
    def enfiler(self, element) :
        """Ajoute un élément à la queue de la file"""
        self._elements. append (element)
    def defiler(self):
        """Retire et retourne l'élément en tête"""
        if self. est_vide():
            raise IndexError("Impossible de défiler une file vide")
        return self._elements.pop(0)
    def tete(self):
        """Retourne l'élément en tête sans le retirer"""
        if self.est_vide():
            raise IndexError ("File vide")
        return self._elements[0]
    def est_vide(self) :
        """Vérifie si la file est vide"""
        return len(self._elements) == 0
    def taille(self):
        """Retourne le nombre d'éléments"""
        return len(self._elements)
    def __str__(self) :
        """Représentation textuelle de la file"""
        if self.est_vide():
            return "File vide"
        return f"File: {' <- '.join(map(str, self._elements))} (tête à droite)"
    # Retire le premier élément

def gerer_caisse(file_clients, nouveaux_clients, nb_services):
    # À compléter
    for clients in nouveaux_clients:
        File.enfiler(clients)
    for x in range(nb_services):
        File.defiler()
    return file_clients
    pass

# Test
file = File()
file.enfiler("Alice")
file.enfiler("Bob")

file_mise_a_jour = gerer_caisse(file, ["Charlie", "David"], 1)
# Alice a été servie, la file contient : Bob, Charlie, Davi