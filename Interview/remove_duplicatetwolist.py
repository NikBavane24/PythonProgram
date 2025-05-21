
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

list3=list(set(list1).symmetric_difference(set(list2)))
print(list3)
