class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def make_sound(self):
        print("Sound made by Dog")

class Dog(Animal):
    def __init__(self, name,breed):
        Animal.__init__(self,name,species=Dog)
        self.breed=breed

    def make_sound(self):
        print("Bark")

d=Dog("Dog", "Persian")
d.make_sound()

c=Animal("Dog", "Doggerman")
c.make_sound()