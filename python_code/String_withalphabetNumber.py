


a="Nikhil @249 1# @"
b=0
c=0
d=0
e=0
for i in a:
    if i.isalpha():
        b=b+1
print("Number of alphabets=",b)

for i in a:
    if i.isnumeric():
        c=c+1
print("Number of Numeric values=",c)



for i in a:
    if i.isspace():
        e=e+1
print("Number of spaces =",e)


f=d-b-c
print("Number of Special character=",e)

for i in a:
    d=d+1
print("Total number of characters",d)



