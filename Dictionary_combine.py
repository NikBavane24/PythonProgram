


a={1:"Python",2:"Java",3:"JavaScript",4:10}
print(a,type(a))

b={5:"C#",6:"Ruby"}

c=a | b
print(c,type(c))

listc=list(c.items())

print(listc,type(listc))

a.update(b)
print(a)