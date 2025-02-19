

a = [4, 9, 1, 17, 11, 26, 28, 54, 69]
b = [9, 9, 74, 21, 45, 11, 63, 28, 26]

h=tuple(a)
print(type(h),h)


c=list(sorted(set(a) & set(b)))
print(c)

d=list(sorted(set(a) | set(b)))
print(d)


e=list(set(a) - set(b))
print(e)

f=list(set(b) - set(a))
print(f)

g=list(set(a) ^ set(b))
print(g)