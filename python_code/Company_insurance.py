
a = str(input("Enter your marital status (Married/Unmarried): "))
b = str(input("Enter your sex (Male/Female): "))
c = int(input("Enter your age: "))
if a == 'Married':
    print("Driver is insured")
elif a == 'Unmarried' and b == 'Male' and c > 30:
    print("Driver is insured")
elif a == 'Unmarried' and b == 'Female' and c > 25:
    print("Driver is insured")
else:
    print("Driver is not insured")