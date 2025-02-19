from collections import Counter

# Input string
s = "hello world"

# Count the frequency of characters
frequency = Counter(s)
print(frequency)

# Get the character with the maximum frequency
max_char = max(frequency, key=frequency.get)

print("Maximum time repeated character is",max_char)

min_char=min(frequency,key=frequency.get)
print("Minimum time repeated character is",min_char)