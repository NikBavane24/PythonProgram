

a=int(input("Enter the number a="))
b=int(input("Enter the number b="))
c=int(input("Enter the number c="))

if (a>b) and (b>c):
    print("Largest number is a =",a)

elif (b>a) and (b>c):
    print("Largest number is b =", b)

else:
    print("Largest number is c =", c)