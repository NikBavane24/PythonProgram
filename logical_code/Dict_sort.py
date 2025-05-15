

a={1:"a",2:"b",3:"c",6:"f",5:"e",4:"d"}

b=sorted(a.keys())
print(b)

c=sorted(a.values())
print(c)

print(sorted(a,key=a.get))