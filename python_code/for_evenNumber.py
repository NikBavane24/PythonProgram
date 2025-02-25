

given_range=101
a=[]

for i in range(given_range):

    if i%2==0:
        a.append(i)
        print(i)
print(a)
b=tuple(a)
print(b)
print("*******************************")
for i in range(0,101,2):
    print(i)