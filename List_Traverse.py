

a=[1,2,3,4,5,6,7,8,9,10]

i=0
while i<len(a):
    print(a[i])
    i=i+1
    if i==8:
        break

for i in a:

    if i==5:
        continue
    print(i)

n=len(a)
for i in range(n):
    print(i,":",a[i])
