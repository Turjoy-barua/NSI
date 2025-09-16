class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse
   
    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")] 
        
    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
           réservée, False sinon"""
        reservees = ["192.168.0.0", "192.168.0.255", "127.0.0.1" ]
        return (self.adresse in reservees)
             
    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse 
           IP qui suit l’adresse self
           si elle existe et False sinon"""
        octets = self.liste_octets()
        if self.liste_octet() < 254:
            octet_nouveau = octets[3] + 1
            return AdresseIP('192.168.0.' + octets)
        else:
            return False
