

def milk(a):
    b=3.25*a
    print(f"Total amount of milk for {a} liter=",b)

    c=a
    for i in range(1,a+1):
        if i % 4==0:
            c=c+1
    print("Total milk after adding water=",c)

    d=c*4.15
    print("Total amount milk after adding water",d)

    gain=d-b
    print("Total gain of vendor=",gain)

milk(100)