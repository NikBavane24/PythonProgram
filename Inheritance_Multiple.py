from Inheritance_Single import Employee


# 2. Multiple Inheritance

class Job:
    def __init__(self, role):
        self.role = role
        print("role=", role)

class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
    def __init__(self, name, salary,role):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, role)            # Initialize Job role
        print("Name",name,"Salary",salary,"Role",role)

c2=EmployeePersonJob("Vishal",20000,"QA")