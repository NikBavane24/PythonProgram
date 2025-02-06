

a="this is a really a long string"

b=a.split()
print("b=",b,type(b))

c=b[3].isnumeric()
print("c=",c)

d=" ".join(b)
print("d=",d,type(d))