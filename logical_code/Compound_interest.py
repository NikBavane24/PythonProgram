


class Bank:
    def Compound_interest (self,principal,rate,time):
        Amount=principal*(pow((1+rate/100),time))

        CI=Amount-principal
        print("Compound interest CI is",CI)
        print("Total amount after interest is",Amount)
b=Bank()
b.Compound_interest(10000,10,5)