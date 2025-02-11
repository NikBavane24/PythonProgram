

a=[13,45,48,74,53,85,29,19,17,29,86,3,62,58,76,53,59,68,61]
a.sort()
b=[]
c=[]
for i in a:
    if i%2==0:
        b.append(i)

    else:
        c.append(i)



print("Even number list=",b)
print("Odd number list=",c)