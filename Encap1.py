

class Protected:
    def __init__(self):
        self.__salary=50000
        print("Constructor")

    def display_salary(self):
        print(self.__salary)

    def salary(self):
        self.__salary=60000
    def get_salary(self):
        print(self.__salary)


o2=Protected()
o2.display_salary()
o2.salary()
o2.get_salary()