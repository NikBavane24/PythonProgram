
from Inheritance import Cl1


class Cl2(Cl1):
    def M2(self):
        print("Method2")



o1=Cl1
o2=Cl2

o2.M2(self='')
o2.M1(self='')