
a={1,2,3}
print(a)
a.add(5)
a.add('b')
#a.add('a',10)  multiple object not allowed

print(a)

a.update([11,22,33])
print(a)

#update with range
a.update(a,range(11))
print(a)

#copy
b=a.copy()
print(b)