a=[1,2,3]
b=[4,5,6]

result = tuple([item for pair in zip(a, b) for item in pair])

print(result)

c=[11,12,13]
d=[14,15,16]

tuple_list=tuple([item for pair in zip(c,d) for item in pair])
print(tuple_list)