class Employee:
    company="Apple"

    def show(self):
        print(f"Name of Employee {self.name} work in {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):  #if we write self still we will get the same result (without @classmethod argument)
        cls.company=newCompany

e=Employee()
e.name="Souvik"
e.show()
e.changeCompany("Nvidia")
e.show()
print(Employee.company)