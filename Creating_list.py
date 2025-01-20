
# Declare list object
a1=[]
print(a1)

a=[1,2,3,4,5,6,7,8,9]
print(a)
print(a[4])
print(a[-1])
print(a[2:9:3])
print(a[9:1:-3])

# using split function
b="I love python programing"
c = b.split()
print(c)
print(type(c))

# using list() function
d=list(range(10,21,2))
print(d)

#list of string
e=["python","programming"]
print(e)

#list of mixed datatype
f=[1,'a',2,'b']
print(f)

#list of Nested list
g=[1,2,["z","x"]]
print(g)
print(g[0])
print(g[1])
print(g[2][1])