

class Cl1:
    def M1(self):
        print("It is the class of CL1")


class Cl2(Cl1):
    def M2(self):
        print("It is the class of CL2")

o2=Cl2

o2.M1(self="")
o2.M2(self="")