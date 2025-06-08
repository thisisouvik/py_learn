class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def show(self):
        print(f" Name {self.name} and id is {self.id}")
class Language(Employee): #inheritence
    def showlan(self):
        print("Default language is Python")

e=Employee("Rohan Das", 43)
e.show()
e2=Language("Sarvesh", 69)
e2.showlan()
e2.show()