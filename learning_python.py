print("Hello World!") # This is a simple Python program that prints "Hello World!" to the console.

def greet(name):
    print(f'Hello, {name}!') # Function to greet a person by their name.

greet("Alice")  # Calling the function with the name "Alice"

print('My favorite drinks are', 'red bull', 'Fritz Cola', 'and', 'coffee.', sep=' > ') # Demonstrating the use of the sep parameter in the print function to customize the separator between printed items.

name = 'Ivan' # Assigning a string value to a variable
surname = 'Lutso' 
age = 25      # Assigning an integer value to a variable
height = 1.83 # Assigning a float value to a variable
is_student = True # Assigning a boolean value to a variable
print(f'{name} {surname} is {age} years old, {height} meters tall, and student status is {is_student}.') # Using an f-string to format and print multiple variables in a single line.

my_integer_var = 10
print(type(my_integer_var)) # <class 'int'>

my_float_var = 10.5
print(type(my_float_var)) # <class 'float'>

my_string_var = "Hello"
print(type(my_string_var)) # <class 'str'>

my_boolean_var = False
print(type(my_boolean_var)) # <class 'bool'>

my_dictionary_var = {"key": "value"}
print(type(my_dictionary_var)) # <class 'dict'>

my_tuple_var = (8, 4, 5)
print(type(my_tuple_var)) # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var)) # <class 'range'>

my_list_var = [2.3, 'Bye', 7, True]
print(type(my_list_var)) # <class 'list'>

my_set_var = {1, 2, 3}
print(type(my_set_var)) # <class 'set'>

my_bytes_var = b'example'
print(type(my_bytes_var)) # <class 'bytes'>

my_frozenset_var = frozenset([4, 5, 6]) 
print(type(my_frozenset_var)) # <class 'frozenset'>

my_bytearray_var = bytearray(b'example')
print(type(my_bytearray_var)) # <class 'bytearray'>

my_complex_var = 3 + 4j
print(type(my_complex_var)) # <class 'complex'>

my_none_var = None
print(type(my_none_var)) # <class 'NoneType'>

print("End of the program.")

isinstance(age, int) # True
isinstance('Cute', int) # False
isinstance(height, float) # True

# isinstance() let's you check if a variable is of a specific type

