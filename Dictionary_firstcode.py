# Key and value pair
# duplicate keys are not allowed but values are allowed
#dictionary are mutable


a={}
print(a,type(a))

a={1:"Python",2:"Java",3:"JavaScript",4:10}
print(a,type(a))

#Using dict()
a=dict()
print(a,type(a))

a=dict({1:"Python",2:"Java",3:"JavaScript",4:"Ruby",10:"C#"})
print(a,type(a))

#Accessing element using[key]
print(a[1])
print(a[2])
print(a[10])
#print(a[20])

#accessing using get()
print(a.get(1))
print(a.get(100))