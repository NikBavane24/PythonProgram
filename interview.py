import inflect

# Create an engine
p = inflect.engine()

# Loop from 1 to 100 and convert each number to words
for i in range(1, 101):
    word = p.number_to_words(i)
    print(f"{i} -> {word}")
