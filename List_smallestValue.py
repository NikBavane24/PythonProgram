list1=[13,45,48,74,53,85,29,19,17,29,86,48,4,6,53,59,68,61,93,92,87]
a=[]
for i in list1:
    if i<list1[0]:
        a.insert(0,i)
        a.sort()
print(a[0])
b=list1.sort()
c=list1[0]
print(c)
Min=min(list1)
print(Min)
z=[]
for i in list1:
    if i>list1[0]:
        z.insert(0,i)
print(z[0])
list1.reverse()
print(list1[0])
y=max(list1)
print(y)