

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]

# Initialize an empty set to store seen elements
s = set()

# List to store duplicates
dup = []

for n in a:
    if n in s:
        dup.append(n)
    else:
        s.add(n)

print(dup)