# =============================================================================
# INTERMEDIATE PYTHON - PART 2
# =============================================================================
# This file covers intermediate Python concepts including loops, sequences,
# dictionaries, and sets as part of the FreeCodeCamp curriculum.

# =============================================================================
# SESSION 23: DICTIONARIES
# =============================================================================

# General Syntax of Python Dictionary

dictionary = {
    # key1: value1,
    # key2: values2
}

# Keys must be unique in the dictionary, and they must be an immutable data type.
# Values can be of any data type and can be repeated

pizza = {
    'name': 'Margherita',
    'price': 8.9,
    'calories_per_slice': 110,
    'toppings': ['mozzarella', 'basil']
}

# Another alternative is using dict() constructor
# Tuples contain the key as the first element and the value as second

pasta = dict([('name', 'orecchiette'), ('price', 9.99), ('calories', 280)])
