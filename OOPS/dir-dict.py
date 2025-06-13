x=[1,2,3]
print(dir(x))
print(x.__contains__)

class Person:
    def __init__(self, Name, Salary):
        self.name=Name
        self.salary= Salary

e=Person("Souvik", 9999)
print(e.__dict__)

print(help(str))    #HELP FUCNTION