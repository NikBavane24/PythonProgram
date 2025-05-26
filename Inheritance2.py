
from Inheritance import Cl1


class Cl2(Cl1):
    def __init__(self):
        super().__init__()
        print("Constructor of CL2")
    def M2(self):
        super().M1()
        print("Method M2")




#o1=Cl1()
o2=Cl2()

o2.M2()
#o2.M1()