

a=dict({1:"Python",2:"Java",3:"JavaScript",4:"Ruby",10:"C#"})
print(a,type(a))
#len()
print(len(a))

#get
print(a.get(10))

#keys()
print(a.keys())
print(type(a.keys()))
b=list(a.keys())
print(b)
print(type(b))


#values()
print(a.values())
print(type(a.values()))
b=list(a.values())
print(b)
print(type(b))


#Items()
print(a.items())
print(type(a.items()))
b=list(a.items())
print(b)
print(type(b))