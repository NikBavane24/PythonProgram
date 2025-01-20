

a=dict({1:"Python",2:"Java",3:"JavaScript",4:"Ruby",10:"C#"})
print(a,type(a))

for i,j in a.items():
    print(i," ",j)

print("                                  ")
for i in a:
    print(i," ",a[i])