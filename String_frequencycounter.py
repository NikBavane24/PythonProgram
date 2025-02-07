


from collections import Counter

# Input string
s = "hello world"

# Count the frequency of characters
frequency = Counter(s)
print(frequency)

# Get the character with the maximum frequency
max_char = max(frequency, key=frequency.get)

print(max_char)