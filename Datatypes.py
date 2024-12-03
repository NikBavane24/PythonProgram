from tkinter.font import names

value=[1,2,3.12,"Nikhil",10,14]
print(value[-1])

print(value[2:5])

value.insert(4,"Bavane")


value.append("End")
print(value)

value[3]="NIKHIL"
del value[-1]
print(value)

age=(2,5,12,18)
print(age[0])

p={1:"Nikhil",2:"Bavane",3:32}

print(p[3])

dict={}
dict["name"]="Rahul"
dict["surname"]="Nigade"

print(dict)
print(dict["name"])
