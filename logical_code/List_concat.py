

a = [1, 2, 3]
b = ['a', 'b', 'c']

for x,y in zip(a,b):
    print(x,y)

c=a+b
print("c=",c)
a.extend(b)
print(a)