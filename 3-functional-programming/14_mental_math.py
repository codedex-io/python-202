# Define the range of integers
start = 1
end = 11
numbers_range = range(start, end)

# Create a list of even numbers using list comprehension
even_numbers = [num for num in numbers_range if num % 2 == 0]

# Display the original range and the list of even numbers
print("Original Range:", list(numbers_range))
print("Even Numbers:", even_numbers)
