print("Hello World!")  # Basic hello


def greet(name):
    print(f'Hello, {name}!')  # Function to greet a person by their name.


greet("Alice")  # Calling the function with "Alice" as the argument - prints "Hello, Alice!"


# Print with custom separator - the sep parameter changes what appears between printed items (default is a space)
print('My favorite drinks are', 'red bull', 'Fritz Cola', 'and', 'coffee.', sep=' > ')


# Personal info variables and formatted output
name = 'Ivan'
surname = 'Lutso'
age = 25
height = 1.83
is_student = True
print(f'{name} {surname} is {age} years old, {height} meters tall, and student status is {is_student}.')


# Core Python data types
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 10.5
print(type(my_float_var))  # <class 'float'>

my_string_var = "Hello"
print(type(my_string_var))  # <class 'str'>

my_boolean_var = False
print(type(my_boolean_var))  # <class 'bool'>

my_dictionary_var = {"key": "value"}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (8, 4, 5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list_var = [2.3, 'Bye', 7, True]
print(type(my_list_var))  # <class 'list'>

my_set_var = {1, 2, 3}
print(type(my_set_var))  # <class 'set'>

my_bytes_var = b'example'
print(type(my_bytes_var))  # <class 'bytes'>

my_frozenset_var = frozenset([4, 5, 6])
print(type(my_frozenset_var))  # <class 'frozenset'>

my_bytearray_var = bytearray(b'example')
print(type(my_bytearray_var))  # <class 'bytearray'>

my_complex_var = 3 + 4j
print(type(my_complex_var))  # <class 'complex'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>


# Type checking with isinstance
print(isinstance(age, int))  # True
print(isinstance('Cute', int))  # False
print(isinstance(height, float))  # True


# Substring checks
test_str = 'Hi there!'
print('Hi' in test_str)  # True
print('hello' in test_str)  # False


# String operations
my_str = "If Python was an AI, bubble would never have existed."
print(len(my_str))  # Length of the string
my_str = my_str.upper()
print(my_str[3:9])  # Slice from index 3 up to (but not including) index 9 - gets characters at positions 3-8
print(my_str.replace('PYTHON', 'JavaScript'))
print(my_str.split(','))


# Concatenation and repetition
my_str_draft = "No matter where you live"
my_str_final = ", matter what inside your code."
concat = my_str_draft + my_str_final
print(concat)
print((concat + " ") * 3)  # Repeat the concatenated string 3 times


print("End of the program.")

# Session 2 06/01/2026
# Introduction to Strings
# All elements should be in string format to concatenate

name_str = "Alex"
age_integer = 30 # integer
print(name_str + str (age_integer)) # Alex30
# Type conversion from integer to string using str() function

name_and_age = name_str
name_and_age += str(age_integer)
print(name_and_age)  # Alex30
# Using += operator to concatenate strings
# The process of inserting variables and expressions inside a string is called string interpolation

# f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}
# f-strings are prefixed with 'f' or 'F' before the opening quotation mark

greeting = f'Hello, my name is {name_str} and I am {age_integer} years old.'
print(greeting)  # Hello, my name is Alex and I am 30 years old
# Using f-string for string interpolation



