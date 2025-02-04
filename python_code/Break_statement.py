from operator import index

numbers=[8,386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527,10]

for i in numbers:
    if i==237:
        break
    print(i)
print("************************************")
max_value=max(numbers)
print(max_value)

maxvalue_index=numbers.index(max(numbers))
print(maxvalue_index)

min_value=min(numbers)
print(min_value)
print(numbers.index(min_value))


matrix = [[i for i in range(5)] for i in range(5)]
print(matrix)