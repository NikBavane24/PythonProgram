


a = [1, None, 3, 0, None, 5]

i = 0

# Use a `while` loop to iterate over the list.
while i < len(a):
    if a[i] is None:
        del a[i]
    else:
        i += 1
print(a)