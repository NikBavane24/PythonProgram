

a="this is a really a long string"
h= "for working"

i=a+" "+h
print(i)
try:
    d=a.index("r")
    print(d)

except Exception as e:
    print(e)

f=a[10:16]
print("f=",f)
g=f[::-1]
print(g)
b=a[::-1]
print(b)

c=list(a.split())
print(c)
c.sort()
print(c)

g=a.split()
print("g=",g)
h=len(g[0]),len(g[1]),len(g[2]),len(g[3]),len(g[4]),len(g[5]),len(g[6])
print("h=",h)