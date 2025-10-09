class Animal():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def parler():
        return "..."
class Chien(Animal):
    def parler(self):
        print("wouf !")
class Chat(Animal):
   def parler(self):
        print("Miaou !")

a = Chien("tom", 2)
a.parler()