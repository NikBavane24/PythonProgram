from operator import itemgetter

d1 = {'w': 4, 'x': 3}
d2 = {'y': 3, 'z': 4}

d1.update(d2)

print("d1=",d1)
d3=d1 | d2
print("d3=",d3)

data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]
print(data_list)

# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by name: ")
print(sorted(data_list, key=itemgetter('name')))
