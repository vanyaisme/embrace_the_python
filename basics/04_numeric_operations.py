# =============================================================================
# NUMERIC OPERATIONS AND OPERATORS
# =============================================================================
# This module covers numeric operations, arithmetic operators, type conversions,
# and augmented assignment operators in Python:
# - Integer arithmetic operations
# - Float arithmetic operations
# - Mixed-type arithmetic (int + float)
# - Advanced arithmetic operators (modulus, floor division, exponentiation)
# - Type conversion functions
# - Rounding and absolute value
# - Power and base conversion functions
# - Augmented assignment operators


# -----------------------------------------------------------------------------
# 1. INTEGER ARITHMETIC OPERATIONS
# -----------------------------------------------------------------------------
# Python supports all basic arithmetic operations with integers.
# Integer division (/) always returns a float, even if the result is a whole number.

my_int = 4
my_int_2 = -3

print(type(my_int))    # <class 'int'>
print(type(my_int_2))  # <class 'int'>

# Basic arithmetic operations
print('Addition:', my_int + my_int_2)        # Output: 1
print('Subtraction:', my_int - my_int_2)     # Output: 7
print('Multiplication:', my_int * my_int_2)  # Output: -12
print('Division:', my_int / my_int_2)        # Output: -1.3333... (always returns float)


# -----------------------------------------------------------------------------
# 2. FLOAT ARITHMETIC OPERATIONS
# -----------------------------------------------------------------------------
# Floating-point numbers (floats) represent decimal values.
# All arithmetic operations work the same way as with integers.

my_float = 4.23
my_float_2 = -3.14

print(type(my_float))   # <class 'float'>
print(type(my_float_2)) # <class 'float'>

print('Addition:', my_float + my_float_2)        # Output: 1.09
print('Subtraction:', my_float - my_float_2)     # Output: 7.37
print('Multiplication:', my_float * my_float_2)  # Output: -13.2842
print('Division:', my_float / my_float_2)        # Output: -1.347133757


# -----------------------------------------------------------------------------
# 3. MIXED-TYPE ARITHMETIC (INT + FLOAT)
# -----------------------------------------------------------------------------
# When you perform operations between integers and floats,
# Python automatically converts the result to a float (type coercion).

sum_mixed = my_int + my_float
print(type(sum_mixed))      # <class 'float'> - result is automatically converted to float
print('Mixed Addition:', sum_mixed)  # Output: 8.23


# -----------------------------------------------------------------------------
# 4. ADVANCED ARITHMETIC OPERATORS
# -----------------------------------------------------------------------------
# Python provides additional operators for specialized calculations.

# MODULUS OPERATOR (%)
# Returns the remainder after division
print(my_float % my_float_2)  # Output: 1.09 - remainder of 4.23 / -3.14
print(my_int % my_int_2)      # Output: -2 - remainder of 4 / -3

# FLOOR DIVISION OPERATOR (//)
# Returns the largest integer less than or equal to the division result
print(7 // 3.8)  # Output: 1.0 - removes decimal part, keeps integer portion

# EXPONENTIATION OPERATOR (**)
# Raises a number to a power
print(my_float ** 2)  # Output: 17.8929 - 4.23 squared (4.23 × 4.23)


# -----------------------------------------------------------------------------
# 5. TYPE CONVERSION FUNCTIONS
# -----------------------------------------------------------------------------
# Python provides built-in functions to convert between numeric types.

# Converting strings to numbers
print(float('3.14'))  # Output: 3.14 - string to float
print(int('42'))      # Output: 42 - string to integer

# Converting floats to integers (truncates decimal part, doesn't round)
print(int(3.99))   # Output: 3 - simply removes decimal portion
print(int(-3.99))  # Output: -3 - truncates toward zero


# -----------------------------------------------------------------------------
# 6. ROUNDING AND ABSOLUTE VALUE
# -----------------------------------------------------------------------------

# ROUNDING
print(round(3.141))       # Output: 3 - rounds to nearest integer
print(round(3.147, 2))    # Output: 3.15 - rounds to 2 decimal places
print(round(2.5))         # Output: 2 - rounds to nearest even number (banker's rounding)
print(round(3.5))         # Output: 4

# ABSOLUTE VALUE
print(abs(-7.5))   # Output: 7.5 - distance from zero (always positive)
print(abs(7.5))    # Output: 7.5
print(abs(-10))    # Output: 10


# -----------------------------------------------------------------------------
# 7. POWER AND BASE CONVERSION FUNCTIONS
# -----------------------------------------------------------------------------

# THE pow() FUNCTION
# More versatile than the ** operator
print(pow(2, 3))        # Output: 8 - same as 2 ** 3 (2 to the power of 3)
print(pow(9, 0.5))      # Output: 3.0 - square root of 9 (9 ** 0.5)
print(pow(27, 1, 4))    # Output: 3 - modular exponentiation: (27 ** 1) % 4

# BASE CONVERSION WITH int()
# Converts strings in different bases to decimal integers
print(int('1010', 2))   # Output: 10 - binary (base-2) to decimal
print(int('FF', 16))    # Output: 255 - hexadecimal (base-16) to decimal
print(int('77', 8))     # Output: 63 - octal (base-8) to decimal
print(int('101', 10))   # Output: 101 - decimal (base-10, default)


# -----------------------------------------------------------------------------
# 8. AUGMENTED ASSIGNMENT OPERATORS
# -----------------------------------------------------------------------------
# Shorthand operators that combine an operation with assignment.
# Format: variable operator= value
# These make code more concise and readable.

# Numeric augmented assignments
my_var = 15
my_var += 5  # Equivalent to: my_var = my_var + 5
print('After += 5:', my_var)  # Output: 20

my_var -= 3  # Equivalent to: my_var = my_var - 3
print('After -= 3:', my_var)  # Output: 17

my_var *= 2  # Equivalent to: my_var = my_var * 2
print('After *= 2:', my_var)  # Output: 34

my_var //= 4  # Equivalent to: my_var = my_var // 4
print('After //= 4:', my_var)  # Output: 8

my_var %= 5  # Equivalent to: my_var = my_var % 5
print('After %= 5:', my_var)  # Output: 3

my_var **= 3  # Equivalent to: my_var = my_var ** 3
print('After **= 3:', my_var)  # Output: 27

# String augmented assignments
greet = "Hello"
greet += ", World!"  # Concatenates and assigns back
print(greet)  # Output: Hello, World!

greet *= 2  # Repeats the string twice
print(greet)  # Output: Hello, World!Hello, World!

# Note: Only += and *= work with strings
# Other operators (like -=, /=) will raise TypeError with strings


print("\n" + "="*60)
print("END OF NUMERIC OPERATIONS MODULE")
print("="*60 + "\n")
