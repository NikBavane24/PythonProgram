

a = [1, 4, 5, 6, 7]
b = ['a', 'b', 'c', 'd', 'e']

for index,value in zip(range(len(a)),zip(a,b)):
    print(index,value)