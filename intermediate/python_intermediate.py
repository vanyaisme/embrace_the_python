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

# =============================================================================
# SECTION 12: TUPLES - BASICS
# =============================================================================
# Tuples are immutable sequences, similar to lists but cannot be modified after creation
# Used to create ordered sequences of values that shouldn't change
# Defined using parentheses () instead of square brackets []
# Key difference from lists: attempting to modify a tuple raises a TypeError

# Creating and accessing tuples
human = ('Ivan', 25, 'Ukraine') # Creating a tuple with mixed data types
print(human[0]) # Accessing elements works the same as lists (returns 'Ivan')

# Tuples are immutable - these operations would fail:
# human[1] = 26 # TypeError: 'tuple' object does not support item assignment
# human[9] # IndexError: tuple index out of range

# =============================================================================
# SECTION 13: CONVERTING TO TUPLES
# =============================================================================

# tuple() constructor - converts iterables to tuples
developer = 'John Doe'
tuple(developer) # Returns ('J', 'o', 'h', 'n', ' ', 'D', 'o', 'e') - each character becomes an element
# The tuple() constructor accepts strings, lists, and other iterables

# =============================================================================
# SECTION 14: TUPLE OPERATIONS
# =============================================================================

# Membership testing with tuples (using 'in' keyword)
programming_languages = ('Python', 'Java', 'C++', 'Python', 'R', 'Brainfuck')
'Rust' in programming_languages # Returns False
'Brainfuck' in programming_languages # Returns True

# Tuple unpacking - works the same as with lists
human_being = ('Miron', 40, 'January 31, 1985', 'Rap artist', 'One album per 4 years')
name, age, date_of_birth, *features = human_being # *features captures remaining elements as a list

# Tuple slicing - extract a portion of the tuple
food = ('Burger', 'Pizza', 'Pasta', 'Sweet Potatoes', 'Salad')
print(food[1:3]) # Returns ('Pizza', 'Pasta') - ending index is not included

# =============================================================================
# SECTION 15: TUPLES VS LISTS
# =============================================================================

# Important: Tuples are immutable - you cannot add, remove, or modify elements
# No methods like append(), remove(), or pop() for tuples

# When to use tuples vs lists?
# - Dynamic collection (will change)? Use a LIST
# - Fixed collection (won't change)? Use a TUPLE
# - Tuples are faster and use less memory than lists
# - Tuples can be used as dictionary keys (lists cannot)

# =============================================================================
# SECTION 16: TUPLE METHODS
# =============================================================================
# Note: Tuples have only 2 methods (count and index) because they're immutable

# count() - counts how many times an item appears in a tuple
debtors = ('Andrew', 'John', 'Margo', 'John', 'Newton', 'John')
debtors.count('John') # Returns 3 - 'John' appears three times
# If no argument is passed to count(), raises TypeError

# index() - finds the first index where an item appears in a tuple
debtors.index('John') # Returns 1 - first occurrence of 'John' is at index 1

# index() with start parameter: index(value, start)
debtors.index('John', 3) # Returns 3 - finds 'John' starting from index 3 onwards

# index() with start and stop parameters: index(value, start, stop)
# debtors.index('Newton', 1, 3) # ValueError: 'Newton' is not in range [1:3)

# =============================================================================
# SECTION 17: SORTING TUPLES
# =============================================================================

# sorted() - built-in function that creates a NEW sorted list from a tuple
# Syntax: sorted(iterable, key=function, reverse=bool)
sorted(debtors) # Returns ['Andrew', 'John', 'John', 'John', 'Margo', 'Newton']
# Important: sorted() returns a LIST, not a tuple. Original tuple remains unchanged

# key parameter - allows custom sorting logic
words = ('go', 'melancholy', 'joy', 'Python', 'I')
sorted(words, key=len) # Returns ['I', 'go', 'joy', 'Python', 'melancholy'] - sorted by string length

# reverse parameter - sorts in descending order when True
sorted(words, reverse=True) # Returns ['melancholy', 'joy', 'go', 'Python', 'I'] - reverse alphabetical order

# =============================================================================
# SECTION 18: LOOPS TYPES
# =============================================================================

# Two main types of loops in Python: for loops and while loops
# for loops - iterate over a sequence (like a list, tuple or string)
fruits = ['Apple', 'Banana', 'Cherry']
for fruit in fruits:
    print(fruit) # Prints each fruit in the list

for char in 'Melancholy':
    print(char) # Prints each character in the string

# nested for loops - loops inside loops
categories = ['Hip Hop', 'Rock', 'Jazz']
artists = ['2Pac', 'Nirvana', 'Miles Davis']
for category in categories:
    for artist in artists:
        print(category + ': ' + artist)
# Prints all combinations of categories and artists

# while loops - repeat block of code as long as a condition is True
secret_code = 10
guess = 0
while guess != secret_code:
    guess = int(input('Make your guss (1-10): '))
    if guess < secret_code:
        print('Too low! Try again.') # As long as guess lower than secret_code # Too low! Try again.
    elif guess > secret_code:
        print('Too high! Try again.') # As long as guess higher than secret_code # Too high! Try again.

print('Congratulations! You guessed the secret code.') # When guess equals secret_code # Congratulations! You guessed the secret code.

# break statement - exits the loop immediately
print('--- Using break statement ---')
developer_names = ['James', 'John', 'Naomi', 'Hanna']
for name in developer_names:
    if name == 'Naomi':
        print('Found Naomi! Let\'s wrap it up, lads.')
        break # Exits the loop when 'Naomi' is found
    print('Current developer: ' + name) # Prints names until 'Naomi' is found

# continue statement - skips the current iteration and moves to the next
print('--- Using continue statement ---')
for name in developer_names:
    if name == 'Naomi':
        print('Skipping Naomi for now.')
        continue # Skips the rest of the loop body for 'Naomi'
    print('Current developer: ' + name) # Prints names except 'Naomi'

# break vs continue:
# - break: exits the entire loop when condition met
# - continue: skips current iteration and continues with next one
# =============================================================================

# both for and while loops can be combined with else clause, which executes when the loop is not terminated by a break statement
print('--- Using else with loops ---')
words = ['sky', 'appple', 'rhytm', 'fly', 'orange']             # creating a list of 5 words
for word in words:                                          # iterating through each word in the list, one by one
    for letter in word:                                     # iterating through each letter in the current word 'sky' = 's', 'k', 'y'
        if letter.lower() in 'aeiou':                         # checking if the current letter is a vowel (a, e, i, o, u)
            print(f"'{word}' contains a vowel: '{letter}'") # if a vowel is found, print the word and the vowel
            break                                        # exit the inner loop (stop checking letters for this word) and move to the next word
    else:                                                 # if we checked ALL letters in the word and found NO vowels
        print(f"'{word}' has no vowels.")                  # print that the word has no vowels

# =============================================================================
# SECTION 19: RANGE() FUNCTION
# =============================================================================
# range() - generates a sequence of integers, commonly used in for loops
# Syntax: range(start, stop, step)
# - start: starting integer (inclusive, default is 0)
# - stop: ending integer (exclusive)
# - step: increment between each integer (default is 1)

for num in range(5): # Generates numbers 0 to 4
    print(num) # Prints 0, 1, 2, 3, 4

for num in range(1, 5): # Generates numbers 1 to 4
    print(num) # Prints 1, 2, 3, 4

for num in range(2, 11, 2): # Generates even numbers from 2 to 10
    print(num) # Prints 2, 4, 6, 8, 10

# range() has only one required argument (stop); start and step are optional
# if you don't provide any arguments, it raises a TypeError
# if you try to pass float values, it raises a TypeError as well

# if you want decrementing sequence, use a negative step
for num in range(40, -5, -5): # Generates numbers from 40 down to 0, decrementing by 5
    print(num) # Prints 40, 35, 30, 25, 20, 15, 10, 5, 0

# you can convert range objects to lists or tuples using list() or tuple() constructors
even_numbers = list(range(0, 21, 2)) # Creates a list of even numbers from 0 to 20
print(even_numbers) # Prints [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odd_numbers = tuple(range(1, 20, 2)) # Creates a tuple of odd numbers from 1 to 19
print(odd_numbers) # Prints (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)

# =============================================================================
# SECTION 20: ENUMERATE AND ZIP FUNCTIONS
# =============================================================================

languages = ['Spanish', 'Dutch', 'English', 'Portugese', 'Chinese']
index = 0

for language in languages: 
    print(f'#{index} and language {language}')
    index += 1

# Easier way to do this using enumerate() function
# enumerate() keeps track of the index for an iterable and return an enumerate object

developers = ['Asia', 'Gronzo', 'Kitana', 'John', 'Niko']
print(list(enumerate(developers))) #[(0), 'Asia', (1, 'Gronzo'), (2, 'Kitana'), ... )]

# Each entry in the enumerate object (now a list) is a tuple containing a count.

languages = ['Spanish', 'Dutch', 'English', 'Portuguese', 'Chinese']

for index, language in enumerate(languages): 
    print(f'#{index} and language {language}') # #0 Spanish \n #1 Dutch \n #2 English \n #3 Portuguese
# this approach removes the need for manually creating and updating an index variable

# enumerate() function also accepts an optional start argument
# if this argument is ommitted, the count will begin at 0 by default

fruits = ['Kiwi', 'Orange', 'Apple', 'Banana']

for index, fruit in enumerate(fruits, 1):
    print(f'#{index} {fruit}') # #1 Kiwi \n #2 Orange \n #3 Apple \n #4 Banana

# zip() function combines lists into pairs of elements and returns an iterator of tuples 

friends = ['Lot', 'Sara', 'Hanka', 'Alex', 'Gaia']
ids = [1, 2, 3, 4, 5]

list(zip(developers, ids)) # [('Lot', 1), ('Sara', 2), ('Hanka', 3), ('Alex', 4), ...]

# zip() combines the two list into pairs of elements and returns and iterator of tuples
# for loop then unpacks each tuple into name and id
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}') # Name: Naomi...
    print(f'ID: {id}') # ID: 1...

# =============================================================================
# SESSION 21: LIST COMPREHENSIONS AND FUNCTIONS TO WORK WITH LISTS
# =============================================================================

even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

# More concise way to write this using comprehensions
# Comprehensions allows to create list in a single line by combining loop and condition directly withing square brackets

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
# this approach is more concise and eliminates the need for separate loop and conditional block 

# another example of comprehension 
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else(num, 'Odd') for num in numbers]
print(result) # [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

words = ['tree', 'dog', 'anarchy', 'life', 'cow', 'house']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['anarchy', 'house']

# filter () is used to select elements from an iterable that meet a specific condition
# filter () accepts a function and an iterable for its arguments 

# map () function take an iterable and applies a functin to each of its elements
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# sum() function is used to get the sum form an iterable like a list or tuple
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # 50

# we can also pass start argument which sets the initial values for the summation
numbers = [5, 10, 15, 20]
total = sum(numbers, 10)
print(total) # 60

# =============================================================================
# SESSION 22: LAMBDA FUNCTIONS
# =============================================================================

# lambda is an anonymous inline function 
lambda num: num ** 2


numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # [2, 4]

# Do Not use Lambda which:
# Difficult to read, or which are overcomplicated
# Variable are obvious, and defeats the purpose of anonymous function
gi