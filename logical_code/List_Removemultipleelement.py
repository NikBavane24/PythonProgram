


a = [10, 20, 30, 40, 50, 60, 70]

b=[40,50,60]
c=[]
for i in a:
    if i not in b:
        c.append(i)

print(c)
