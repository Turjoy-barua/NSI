class AdresseIP:
    def __init__(self, adresse):
        self.adresse = ...
        
    def liste_octets(self):
        """Renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]
    
    def est_reservee(self):
        """Renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        # Adresses réservées : 192.168.0.0, 192.168.0.255, 127.0.0.1
        reservees = ["192.168.0.0", "192.168.0.255", "127.0.0.1" ]
        return ...
    
    def adresse_suivante(self):
        """Renvoie un objet AdresseIP avec l'adresse IP qui suit
        l'adresse self si elle existe et None sinon
        (on se limite au réseau 192.168.0.x)"""
        octets = ...
        if ... == 254: # On s'arrête à .254 (avant .255 qui est réservée)
            return None
        octet_nouveau = ... + ...
        return AdresseIP('192.168.0.' + ...)
    
# Test de création et d'affichage
ip1 = AdresseIP("192.168.0.1")
print(ip1.adresse) # doit afficher "192.168.0.1"
# Test de liste_octets
print(ip1.liste_octets()) # doit afficher [192, 168, 0, 1]
ip2 = AdresseIP("10.0.0.255")
print(ip2.liste_octets()) # doit afficher [10, 0, 0, 255]
# Test d'adresses réservées
ip3 = AdresseIP("127.0.0.1")
print(ip3.est_reservee()) # doit afficher True
ip4 = AdresseIP("192.168.0.0")
print(ip4.est_reservee()) # doit afficher True
ip5 = AdresseIP("192.168.0.50")
print(ip5.est_reservee()) # doit afficher False
# Test d'adresse suivante
ip6 = AdresseIP("192.168.0.10")
ip7 = ip6.adresse_suivante()
print(ip7.adresse) # doit afficher "192.168.0.11"
ip8 = AdresseIP("192.168.0.254")
ip9 = ip8.adresse_suivante()
print(ip9) # doit afficher None