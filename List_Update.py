a=[1,2,3,4,5,6,7,8,9,10]
print(a)

a[1]=20
print(a)

a[1:4]=[22,33,44]
print(a)

a.append(200)
a.append(300)
print(a)

a.extend([2,3,4])
print(a)

a.insert(1,2)
print(a)

#delete Element
del a[1]
print(a)

del a[1:4]
print(a)

a.remove(1)
print(a)

a.pop()
print(a)

a.pop(0)
print(a)

a.clear()
print(a)