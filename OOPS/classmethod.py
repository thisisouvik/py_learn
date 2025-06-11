class Employee:
    company="Apple"

    def show(self):
        print(f"Name of Employee {self.name} work in {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company=newCompany

e=Employee()
e.name="Souvik"
e.show()
e.changeCompany("Nvidia")
e.show()
print(Employee.company)