


a=[13,45,48,74,53,85,29,19,17,29,86,3,53,59,68,61,-11,-13,-43,-56,-28,-24,-88,-35,-97,-81]
a.sort()
b=[]
c=[]
for i in a:
    if i>0:
        b.append(i)

print("Positive number list=",b)

print("________________________________")

for i in a:
    if i<0:
        c.append(i)

print("Negative number list=",c)