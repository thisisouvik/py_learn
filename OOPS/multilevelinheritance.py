class Animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species
    
    def show_details(self):
        print(f"The name is {self.name} and species is {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        
        self.breed=breed

    def show_details(self):
        Animal.show_details(self)
        print(f"The breed is {self.breed}")

class GoldenRetriver(Dog):
    def __init__(self, name, colour):
        Dog.__init__(self, name, breed="GoldenRetriver")

        self.colour=colour
    
    def show_details(self):
        Dog.show_details(self)
        print(f"The colour is {self.colour}")

o=GoldenRetriver('Jet', "Black")
o.show_details()
print(GoldenRetriver.mro())
