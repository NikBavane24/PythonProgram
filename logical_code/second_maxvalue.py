a = [1, 2, 3, 1, 2, 4, 5, 6, 5,8,10]

# Step 1: Find the maximum value
max_val = a[0]
for num in a:
    if num > max_val:
        max_val = num

# Step 2: Find the second maximum
second_max = None
for num in a:
    if num != max_val:
        if second_max is None or num > second_max:
            second_max = num

# Output the second largest value
print("Second largest value:", second_max)
