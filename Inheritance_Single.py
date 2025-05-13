

class Person:
    def __init__(self, name):
        self.name = name
        #print(name)

class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        print("Name=",name,"Salary=",salary)

c1=Employee("Shubham",10000)