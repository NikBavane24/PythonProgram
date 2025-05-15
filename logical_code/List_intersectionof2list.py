

a = [4, 9, 1, 17, 11, 26, 28, 54, 69]
b = [9, 9, 74, 21, 45, 11, 63, 28, 26]

h=tuple(a)
print(type(h),h)


c=list(sorted(set(a) & set(b)))
print("c=",c)

d=list(sorted(set(a) | set(b)))
print("d=",d)


e=sorted(list(set(a) - set(b)))
print("e=",e)

f=sorted(list(set(b) - set(a)))
print("f=",f)

g=sorted(list(set(a) ^ set(b)))
print("g=",g)