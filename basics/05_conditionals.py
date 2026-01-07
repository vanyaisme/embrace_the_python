# =============================================================================
# CONDITIONALS: BOOLEANS AND CONTROL FLOW
# =============================================================================
# This module covers comparison operators, conditional statements (if/elif/else),
# logical operators, and truthy/falsy values in Python:
# - Comparison operators (==, !=, >, <, >=, <=)
# - The if statement
# - The if-else statement
# - The elif statement (multiple conditions)
# - Nested conditional statements
# - Logical operators (and, or, not)
# - Truthy and falsy values


# -----------------------------------------------------------------------------
# 1. COMPARISON OPERATORS
# -----------------------------------------------------------------------------
# Comparison operators compare two values and return a Boolean (True or False).
# They are essential for making conditional statements.

# List of comparison operators:
# ==  : Equal to (checks if two values are the same)
# !=  : Not equal to (checks if two values are different)
# >   : Greater than (left value is larger than right)
# <   : Less than (left value is smaller than right)
# >=  : Greater than or equal to
# <=  : Less than or equal to

# Examples of comparison operators
print(3 == 2)    # Output: False - 3 is not equal to 2
print(3 != 2)    # Output: True - 3 is different from 2
print(5 > 3)     # Output: True - 5 is greater than 3
print(2 < 10)    # Output: True - 2 is less than 10
print(5 >= 5)    # Output: True - 5 is equal to 5
print(3 <= 2)    # Output: False - 3 is not less than or equal to 2


# -----------------------------------------------------------------------------
# 2. THE if STATEMENT
# -----------------------------------------------------------------------------
# The if statement executes code only when a condition is True.
# Indentation (spaces/tabs) defines which code belongs to the if block.
# Python uses indentation instead of curly braces like other languages.

# Basic if statement structure:
# if condition:
#     code to execute if condition is True

age = 18
if age >= 18:
    print("You are an adult!")  # This prints because age >= 18 is True

# Using pass as a placeholder
# pass is a null operation - it does nothing but prevents syntax errors
if True:
    pass  # Placeholder for future code


# -----------------------------------------------------------------------------
# 3. THE if-else STATEMENT
# -----------------------------------------------------------------------------
# else provides an alternative block of code when the if condition is False.
# else never takes a condition - it's the "catch-all" for everything else.

age = 12
if age >= 18:
    print("You are an adult!")
else:
    print("You are not old enough yet!")  # Output: You are not old enough yet!

# Another example
temperature = 15
if temperature > 20:
    print("It's warm outside.")
else:
    print("It's cool outside.")  # This executes because 15 <= 20


# -----------------------------------------------------------------------------
# 4. THE elif STATEMENT (MULTIPLE CONDITIONS)
# -----------------------------------------------------------------------------
# elif (else if) allows you to check multiple conditions in sequence.
# Python evaluates conditions from top to bottom and executes the first True one.
# Once a condition is True, remaining elif/else blocks are skipped.

age = 16
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")  # This executes because 13 <= 16 < 18
elif age <= 25:
    print("You are a young adult.")
else:
    print("You are an adult.")

# Example with user input
# input() always returns a string, so we convert it to int
age = int(input("How old are you? "))
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age <= 25:
    print("You are a young adult.")
else:
    print("You are getting old, my friend.")


# -----------------------------------------------------------------------------
# 5. NESTED CONDITIONAL STATEMENTS
# -----------------------------------------------------------------------------
# You can place if statements inside other if statements (nesting).
# Each level of nesting adds another layer of indentation.
# Be careful with indentation - it determines which code belongs where!

is_student = input("Are you a student? (yes/no): ")
age = int(input("How old are you? "))

if is_student == "yes":
    print("You are eligible for a student discount!")
    if age < 18:
        print("You get an additional youth discount!")
    else:
        print("Standard student discount applies.")
else:
    print("No student discount available.")
    if age < 18:
        print("But you qualify for a youth discount!")
    else:
        print("Regular pricing applies.")


# -----------------------------------------------------------------------------
# 6. LOGICAL OPERATORS (and, or, not)
# -----------------------------------------------------------------------------
# Logical operators combine multiple conditions to create more complex logic.

# AND operator - ALL conditions must be True
age = 20
has_license = True
if age >= 18 and has_license:
    print("You can drive!")  # Both conditions are True, so this executes

# OR operator - AT LEAST ONE condition must be True
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("No work today!")  # One condition is True, so this executes

# NOT operator - reverses the boolean value
is_raining = False
if not is_raining:
    print("You don't need an umbrella!")  # not False = True

# Another example with NOT
is_admin = True
if not is_admin:
    print("Access denied. Contact admin.")
else:
    print("Welcome, master!")  # This executes because is_admin is True

# Combining multiple logical operators
# Python evaluates: not first, then and, then or (can use parentheses for clarity)
age = 25
income = 50000
has_debt = False
if age >= 18 and income > 30000 and not has_debt:
    print("Loan approved!")  # All three conditions are True


# -----------------------------------------------------------------------------
# 7. TRUTHY AND FALSY VALUES
# -----------------------------------------------------------------------------
# In Python, every value has an inherent Boolean value (truthy or falsy).
# This means you can use any value in an if statement, not just True/False.

# TRUTHY VALUES (evaluate to True):
# - Non-zero numbers: 1, -5, 3.14, etc.
# - Non-empty strings: "hello", "a", etc.
# - Non-empty collections: [1, 2], {"key": "value"}, etc.

# FALSY VALUES (evaluate to False):
# - None
# - False (the boolean itself)
# - Integer 0
# - Float 0.0
# - Empty string ""
# - Empty list []
# - Empty tuple ()
# - Empty dictionary {}
# - Empty set set()

# Using bool() to check the Boolean value of any object
print(bool(0))           # Output: False - zero is falsy
print(bool(42))          # Output: True - non-zero number is truthy
print(bool(""))          # Output: False - empty string is falsy
print(bool("Hello"))     # Output: True - non-empty string is truthy
print(bool([]))          # Output: False - empty list is falsy
print(bool([1, 2, 3]))   # Output: True - non-empty list is truthy

# Practical examples using truthy/falsy values
user_input = input("Enter your name (or press Enter to skip): ")
if user_input:  # Non-empty string is truthy
    print(f"Hello, {user_input}!")
else:  # Empty string is falsy
    print("Hello, anonymous!")

# Checking if a list has items
shopping_cart = []
if shopping_cart:
    print(f"You have {len(shopping_cart)} items in your cart.")
else:
    print("Your shopping cart is empty.")


print("\n" + "="*60)
print("END OF CONDITIONALS MODULE")
print("="*60 + "\n")
