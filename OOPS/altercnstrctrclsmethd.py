# a= "Harry-Kumar-Yadav"
# e=a.split("-")
# print(e)

class Person:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],string.split("-")[1])

e=Person("Dugle", 6000)
print(e.name)
print(e.salary)

string="John-1933"
e2=Person.fromStr(string)
print(e2.name)
print(e2.salary)