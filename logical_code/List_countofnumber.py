

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

b=0
for i in a:
    if i==2:
        b+=1
print("Count of value 2=",b)

c=a.count(2)
print(c)