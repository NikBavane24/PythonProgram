

unit=int(input("Unit use for month= "))

if unit<=100:
    print("Bill amount=0")

elif unit>100 and unit<=200:
    amount=(unit-100)*5
    print("Bill amount=",amount)

else:
    amount = 500+(unit - 200) * 10
    print("Bill amount=",amount)