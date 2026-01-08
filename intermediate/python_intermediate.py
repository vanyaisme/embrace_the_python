# =============================================================================
# INTERMEDIATE PYTHON - PART 1
# =============================================================================
# This file covers intermediate Python concepts including loops, sequences,
# dictionaries, and sets as part of the FreeCodeCamp curriculum.

# Loops and sequences
# Lists, tuples and ranges

cities = ['Utrecht', 'Den Haag', 'Rotterdam', 'Maastricht', 'Amsterdam']
print('My favourite city is ' + cities[0]) # My favourite city is Utrecht
# 0 indes = first item, -1 index = last item
print('My least favourite city is ' + cities[-1]) # My least favourite city is Amsterdam

len(cities) # 5 # total number of elements in the list

# Lists are mutable, meaning you can change their content
cities[4] = 'Groningen' # changing an element in the list
print(cities) # ['Utrecht', 'Den Haag', 'Rotterdam', 'Maastricht', 'Groningen']

del cities[2] # deleting an element from the list
print(cities) # ['Utrecht', 'Den Haag', 'Maastricht', 'Groningen']

# To check if an element is in a list, use the 'in' keyword
'Amsterdam' in cities # False
'Den Haag' in cities # True

about_me = ['Ivan', 25, ['Neuroscience', 'Artificial Intelligence', 'Technology', 'Rock Climbing'], 'Ukraine']
print('My name is ' + about_me[0] + ' And I like ' + about_me[2][3]) # My name is Ivan And I like Rock Climbing
# Nested lists can be accessed using multiple indices

# Unpacking values from a list
friends = ['Lot', 24, 'Breathing Theraphy']
name, age, activity = friends
print(name) # Lot

fruits = ['Apple', 'Green', 'Sour']
fruit_name, *rest = fruits
print(fruit_name) # Apple
print(rest) # ['Green', 'Sour']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1::2] # [2, 4, 6, 8] # [start:stop:step]

student = 'Ivan'
list(student) # ['I', 'v', 'a', 'n'] # converting a string to a list of characters

# Methods for lists






