#Constructor

class Person:
    def __init__(self, n, addr):
        print("Hello I am in Constructor")
        self.name = n
        self.address = addr

    def info(self):
        print(f"Hi I am {self.name} and from {self.address}")
a=Person("Souvik", "Kolkata")
a.info()