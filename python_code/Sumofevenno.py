

a=range(1,11)
b=0
for i in a:
    if i%2==0:
        b+=i
print("Sum of Even numbers",b)
c=0
for i in a:
    if i%2!=0:
        c+=i
print("Sum of odd numbers",c)
