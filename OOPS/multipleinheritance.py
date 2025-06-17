#ak se jaida class adjoint

class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")


class Dance:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"Dance {self.dance}")

class PersonDancer(Person, Dance):
    def __init__(self, name,dance):
        self.dance=dance
        self.name=name

o=PersonDancer("Shivam", "Kathak")
print(o.name)
print(o.dance)
o.show()
print(PersonDancer.mro())