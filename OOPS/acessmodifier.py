# private public acess in OOPS
class Employee:
    def __init__(self):
        self.__name="Harry"
    def _funname(self):
        return "Codewithme"

class Project(Employee):
    pass

e = Project()

# print(e.__name) cant be acessed like that

print(e._Employee__name)  # can be acessed inderctly  NAME MANGLING
print(e._funname()) # private acess through child

