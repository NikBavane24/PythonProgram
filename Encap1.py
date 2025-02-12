

class Protected:
    def __init__(self):
        self.__salary=50000
        print("Constructor")

    def display_salary(self):
        print(self.__salary)

o2=Protected()
o2.display_salary()