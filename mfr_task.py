# # Task 1: Square all numbers in a list
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # [1, 4, 9, 16, 25]

# # Task 2: Convert temperatures from Celsius to Fahrenheit
# celsius = [0, 10, 20, 30, 40]
# fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
# print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# # Task 3: Capitalize all strings in a list
# names = ['john', 'jane', 'doe']
# capitalized = list(map(str.capitalize, names))
# print(capitalized)  # ['John', 'Jane', 'Doe']

# # Task 4: Multiple iterables
# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# result = list(map(lambda x, y: x + y, num1, num2))
# print(result)  # [5, 7, 9]

# # Task 5: Filter even numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # [2, 4, 6, 8, 10]

# # Task 6: Filter words longer than 5 characters
# words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# long_words = list(filter(lambda word: len(word) > 5, words))
# print(long_words)  # ['banana', 'cherry', 'elderberry']

# # Task 7: Filter positive numbers
# numbers = [-5, -3, 0, 2, 4, -1, 7]
# positive = list(filter(lambda x: x > 0, numbers))
# print(positive)  # [2, 4, 7]

# # Task 8: Filter None values
# mixed = [0, 1, False, True, None, 'hello', '', 'world']
# truthy = list(filter(None, mixed))
# print(truthy)  # [1, True, 'hello', 'world']

# from functools import reduce

# # Raw data
# data = [10, 25, 30, 45, 50, 65, 70]

# # Step 1: Filter values between 20 and 60
# filtered = list(filter(lambda x: 20 <= x <= 60, data))

# # Step 2: Add 5 to each value
# mapped = list(map(lambda x: x + 5, filtered))

# # Step 3: Calculate average
# average = reduce(lambda x, y: x + y, mapped) / len(mapped)

# print(f"Filtered: {filtered}")      # [25, 30, 45, 50]
# print(f"Mapped: {mapped}")          # [30, 35, 50, 55]
# print(f"Average: {average}")        # 42.5