print("Hello World!") # This is a simple Python program that prints "Hello World!" to the console.

def greet(name):
    """This function greets the person whose name is passed as a parameter."""
    print(f"Hello, {name}!")
greet("Alice")  # Calling the function with the name "Alice"

print('My favorite drinks are', 'red bull', 'Fritz Cola', 'and', 'coffee.', sep=' > ') # Demonstrating the use of the sep parameter in the print function to customize the separator between printed items.

name = 'Ivan' # Assigning a string value to a variable
age = 30      # Assigning an integer value to a variable
height = 1.75 # Assigning a float value to a variable
is_student = True # Assigning a boolean value to a variable
print(f'{name} is {age} years old, {height} meters tall, and student status is {is_student}.') # Using an f-string to format and print multiple variables in a single line.
