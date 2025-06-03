a = "Hello World"

# Optional: Replace spaces with underscores if needed
b = a.replace(" ", "_")
print("Modified string:", b)

# Step 1: Create an empty dictionary to count characters
freq = {}

# Step 2: Iterate through characters
for char in b:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Step 3: Print frequency dictionary
print("Character frequency:", freq)