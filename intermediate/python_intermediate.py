# =============================================================================
# INTERMEDIATE PYTHON - PART 1
# =============================================================================
# This file covers intermediate Python concepts including loops, sequences,
# dictionaries, and sets as part of the FreeCodeCamp curriculum.

# =============================================================================
# SECTION 1: LIST BASICS
# =============================================================================

# Creating lists and accessing elements
cities = ['Utrecht', 'Den Haag', 'Rotterdam', 'Maastricht', 'Amsterdam']
print('My favourite city is ' + cities[0]) # My favourite city is Utrecht

# Python uses zero-based indexing: 0 = first item, -1 = last item (negative indices count from the end)
print('My least favourite city is ' + cities[-1]) # My least favourite city is Amsterdam

len(cities) # Returns 5 - len() function counts the total number of elements in the list

# =============================================================================
# SECTION 2: LIST MUTABILITY
# =============================================================================

# Lists are mutable, meaning you can modify their content after creation
cities[4] = 'Groningen' # Replacing the element at index 4 (Amsterdam → Groningen)
print(cities) # ['Utrecht', 'Den Haag', 'Rotterdam', 'Maastricht', 'Groningen']

del cities[2] # The 'del' keyword removes an element at a specific index (Rotterdam removed)
print(cities) # ['Utrecht', 'Den Haag', 'Maastricht', 'Groningen']

# =============================================================================
# SECTION 3: MEMBERSHIP TESTING
# =============================================================================

# Membership testing: use the 'in' keyword to check if an element exists in a list
'Amsterdam' in cities # Returns False (Amsterdam was replaced earlier)
'Den Haag' in cities # Returns True (Den Haag is still in the list)

# =============================================================================
# SECTION 4: NESTED LISTS
# =============================================================================

# Lists can contain other lists (nested/2D lists)
about_me = ['Ivan', 25, ['Neuroscience', 'Artificial Intelligence', 'Technology', 'Rock Climbing'], 'Ukraine']
print('My name is ' + about_me[0] + ' And I like ' + about_me[2][3]) # My name is Ivan And I like Rock Climbing
# Nested lists: access inner elements using multiple indices [outer_index][inner_index]

# =============================================================================
# SECTION 5: LIST UNPACKING
# =============================================================================

# List unpacking: assign list elements to multiple variables in one line
friends = ['Lot', 24, 'Breathing Theraphy']
name, age, activity = friends # Number of variables must match number of elements
print(name) # Lot

# Unpacking with * (star operator): captures remaining elements into a list
fruits = ['Apple', 'Green', 'Sour']
fruit_name, *rest = fruits # *rest collects all remaining elements
print(fruit_name) # Apple
print(rest) # ['Green', 'Sour'] - rest is a list of remaining elements

# =============================================================================
# SECTION 6: LIST SLICING
# =============================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1::2] # Returns [2, 4, 6, 8] - Slicing syntax: [start:stop:step] (start at index 1, skip every 2nd element)

# =============================================================================
# SECTION 7: CONVERTING TO LISTS
# =============================================================================

student = 'Ivan'
list(student) # Returns ['I', 'v', 'a', 'n'] - list() function converts any iterable (like strings) into a list

# =============================================================================
# SECTION 8: LIST METHODS - ADDING ELEMENTS
# =============================================================================

colors = ['Red', 'Violet', 'Green', 'Brown']

# append() - adds a single element to the end
colors.append('Blue')
# Result: ['Red', 'Violet', 'Green', 'Brown', 'Blue']

pastel_colors = ['Light Blue', 'Light Green', 'Light Pink', 'Light Yellow']

# extend() vs append(): extend adds each element individually instead of nesting the list
# colors.append(pastel_colors) # Would nest the entire list as a single element (creating a 2D list)
# Result: ['Red', 'Violet', 'Green', 'Brown', 'Blue', ['Light Blue', 'Light Green', 'Light Pink', 'Light Yellow']]

colors.extend(pastel_colors) # Adds all elements from pastel_colors to colors list
# Result: ['Red', 'Violet', 'Green', 'Brown', 'Blue', 'Light Blue', 'Light Green', 'Light Pink', 'Light Yellow']

# insert() - adds an element at a specific position
colors.insert(2, 'Yellow') # insert(index, element)

# =============================================================================
# SECTION 9: LIST METHODS - REMOVING ELEMENTS
# =============================================================================

# remove() - removes the first occurrence of a specific value
# Note: remove() only accepts ONE argument at a time
colors.remove('Brown') # Removes the first occurrence of 'Brown' from the list
# colors.remove('Blue') # To remove multiple, call remove() multiple times
# colors.remove('Violet')

# pop() - removes and returns an element by index
colors.pop(1) # pop(index) - removes and returns the element at the specified index
# If no index is given, pop() removes and returns the last element

# clear() - removes all elements from the list
# colors.clear() # Makes the list empty []

# =============================================================================
# SECTION 10: LIST METHODS - SORTING AND ORDERING
# =============================================================================

# sort() - sorts the list in-place (modifies the original list)
# colors.sort() # Sorts in ascending order (alphabetically for strings, numerically for numbers)

# sorted() - returns a new sorted list without modifying the original
sorted_colors = sorted(colors)
print(colors) # Original list remains unchanged
print(sorted_colors) # New sorted list

# =============================================================================
# SECTION 11: LIST METHODS - SEARCHING AND COUNTING
# =============================================================================

# index() - finds the position of an element
colors.index('Yellow') # Returns the index of the first occurrence of 'Yellow'
# If element is not found, raises a ValueError

# count() - counts occurrences of an element
colors.count('Blue') # Returns the number of times 'Blue' appears in the list

numbers = [6, 5, 4, 3, 2, 1]
# reverse() - reverses the order of elements in the list
numbers.reverse() # Now numbers is [1, 2, 3, 4, 5, 6]

# =============================================================================


