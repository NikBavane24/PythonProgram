

#P-Principle amount,T-Time,R-rate of interest

def Simple_interest(p,t,r):
    print("Principle amount is=",p)
    print("Time is=", t)
    print("rate of interest is=", r)

    s=(p*t*r)/100

    total_amount=p+s

    print("Simple interest s is",s)
    print("Total amount is",total_amount)

Simple_interest(10000,5,10)