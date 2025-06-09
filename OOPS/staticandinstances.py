class Employee:
    company="Apple" 
    no_of_Employee=0              #static
    def __init__(self,name,sal): 
        self.name=name            #instances
        self.salary=sal
        self.no_of_Employee += 1
    def show(self):
        print(f"Name of Employee {self.name} and salary is {self.salary} is {self.company} is {self.no_of_Employee} no. employee ")

e1=Employee("Souvik", 10000)
e1.name ="Rakesh"
e1.salary= 6000
e1.company="APple INdia"
e1.show()