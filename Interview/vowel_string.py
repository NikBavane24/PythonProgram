def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(count_vowels("Python program with Selenium Pytest"))  # 3