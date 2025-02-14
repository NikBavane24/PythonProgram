

dict = {'a': 100, 'b': 200, 'c': 300}

list1=[]

for i in dict:
    list1.append(dict[i])

final=sum(list1)
print(final)

dict.pop("c")
print(dict)

