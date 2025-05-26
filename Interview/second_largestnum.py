def second_largest(numbers):
 unique_numbers = list(set(numbers)) # Remove duplicates
 unique_numbers.sort(reverse=True) # Sort in descending order
 return unique_numbers[1] # Second largest number
numbers = [12, 35, 1, 10, 34, 1,40]
print(second_largest(numbers)) # Output: 34