
a={1,2,3,4,5,6,7,8}
b={6,7,8,9,10,11,12}


#union
print(a.union(b))
print(b | a)


#Intersection
print(a.intersection(b))
print(a & b)

#Diffrence
print(a.difference(b))
print(a - b)
print(b.difference(a))
print(b - a)

#Symettric_difference
print(a.symmetric_difference(b))
print(a ^ b)
