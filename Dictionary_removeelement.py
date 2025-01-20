

a=dict({1:"Python",2:"Java",3:"JavaScript",4:"Ruby",10:"C#"})
print(a,type(a))

#pop(<key>)
print(a.pop(1))
print(a)

#popItem()
print(a.popitem())
print(a)


#del
del a[2]
print(a)

#del a
#print(a)



#clear
a.clear()
print(a)