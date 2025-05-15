from audioop import reverse

a=[10, 2, 3, 6, 5, 4, 7, 8, 9, 1]

#a.reverse()
print(a)

#b=a[::-1]
#print(b)
rev=[]
for i in a:
    rev.insert(0,i)

print(rev)

b=[]
for i in a:
    b=i+b

print(b)