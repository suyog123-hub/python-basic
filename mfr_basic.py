# higher order inbuilt order function 

# map
    #used for the transforming the elements of an iterable
    # syntax for the map fucntion 
       # map(fucntion,iterable)
'''
# Without map (traditional way)
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # [1, 4, 9, 16, 25]

# WITH map (Pythonic way)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

'''

#filter
# used for filtering the elements of an iterable based on a condition 
    # SYNTAX FOR THE FILTER FUCNTION
      # filter(predicate,iterable)
'''

# Without filter (traditional way)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # [2, 4, 6, 8, 10]

# WITH filter (Pythonic way)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

'''


# REDUCE 
    #to reduce sequence to a single value 
   # WE HAVE TO IMPORT THE REDUCE FUNCTION 
   # reduce(function,iterable)
     #from functools import reduce  # Must import!
     #reduce(function, iterable, initial)

'''
   from functools import reduce

# Without reduce (traditional way)
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # 15

# WITH reduce (Pythonic way)
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15'''