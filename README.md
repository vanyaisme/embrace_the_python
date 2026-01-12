# Learning Python using FreeCodeCamp curriculum

[![Python](https://img.shields.io/badge/Python-3.14.2-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)
[![FreeCodeCamp](https://img.shields.io/badge/Course-FreeCodeCamp-purple.svg)](https://www.freecodecamp.org/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)](https://github.com/vanyaisme/embrace_the_python)

A repository where I'm documenting my journey learning Python through FreeCodeCamp curriculum.

---

## Table of Contents

- [Learning Python using FreeCodeCamp curriculum](#learning-python-using-freecodecamp-curriculum)
  - [Table of Contents](#table-of-contents)
  - [About This Repository](#about-this-repository)
  - [Learning Goals](#learning-goals)
  - [Topics Covered](#topics-covered)
    - [Basics](#basics)
    - [Intermediate](#intermediate)
    - [Advanced](#advanced)
  - [Repository Structure](#repository-structure)
    - [About the Module Structure](#about-the-module-structure)
  - [How to Run the Code](#how-to-run-the-code)
    - [Prerequisites](#prerequisites)
    - [Running Individual Files](#running-individual-files)
    - [Setting Up Virtual Environment (Optional but Recommended)](#setting-up-virtual-environment-optional-but-recommended)
  - [Learning Resources](#learning-resources)
  - [Project Ideas](#project-ideas)
  - [Current Progress](#current-progress)
  - [Certifications \& Courses](#certifications--courses)
  - [Connect](#connect)
  - [License](#license)

---

## About This Repository

This repository serves as my personal learning log and practice space for Python programming. It's organized to track progress, practice concepts, and build a portfolio of small projects as I advance through Python fundamentals to more advanced topics.

## Learning Goals

- Master Python fundamentals (variables, data types, control flow)
- Understand object-oriented programming concepts
- Build practical applications and projects
- Develop problem-solving skills through exercises
- Create clean, well-documented code
- Follow Python best practices (PEP 8)

---

## Topics Covered


### Basics
<details>
<summary><strong>Core Concepts</strong></summary>

- [x] Basic I/O and print operations
  - [x] Basic output with print()
  - [x] Advanced print features (sep parameter)
- [x] Variables and data types
  - [x] Declaring variables
  - [x] Print function
  - [x] Common data types
  - [x] How to get type of a variable
  - [x] Type checking with isinstance()
  - [x] Membership testing with 'in' operator
- [x] String operations and formatting
  - [x] Strings and string immutability
  - [x] String slicing and indexing
  - [x] Common string methods
  - [x] F-strings and formatting
  - [x] Case transformation methods
  - [x] String searching and validation
- [x] Numbers and Mathematical Operations
  - [x] Integers and floating point numbers
  - [x] Augmented assignments
  - [x] Type conversion functions
  - [x] Rounding and absolute value
  - [x] Power and base conversion
- [x] Boolean and conditionals
  - [x] Conditional statements and logical operators
  - [x] True and False values
  - [x] Boolean operators (and, or, not)
  - [x] Truthy and falsy values
  - [x] Nested conditionals
- [x] Functions and scopes
  - [x] Function definition and calling
  - [x] Parameters vs arguments
  - [x] Return statements
  - [x] Variable scope (LEGB rule)
  - [x] Built-in functions
  
</details>

<details>
<summary><strong>Projects/Labs</strong></summary>

- [x] [Caesar cipher](https://github.com/vanyaisme/embrace_the_python/blob/main/projects/caesar_cypher.py)
- [x] [RPG character](https://github.com/vanyaisme/embrace_the_python/blob/main/projects/RPG_character.py)
  
</details>

### Intermediate
<details>
<summary><strong>Core Concepts</strong></summary>

- [x] Loops and sequences
  - [x] Lists and operations
  - [x] Common list methods
  - [x] Tuples and operations
  - [x] Common tuple methods
  - [x] Loop fundamentals
  - [x] Ranges in loops
  - [x] Enumerate and zip functions
  - [x] List comprehensions and functions
  - [x] Lambda functions
- [ ] Dictionaries and sets
  - [ ] Dictionaries and sets 
    - [ ] Loop over a dictionary 
    - [ ] Sets 
  - [ ] Python standard library and importing module
- [ ] Error handling
  - [ ] Error messages 
  - [ ] Debugging techniques 
  - [ ] Exception handling
  - [ ] Raise statement 
- [ ] Classes and objects
  - [ ] How classes differ from objects
  - [ ] Methods and attributes
  - [ ] Special methods 
  - [ ] Object attributes dynamically 
- [ ] Object-Oriented Programming (OOP) 
  

</details>

<details>
<summary><strong>Projects/Labs</strong></summary>

- [x] PIN extractor
- [ ] Number pattern generator
- [ ] Medical data validator
- [ ] Debug an ISBN validator
- [ ] Musical instrument delivery 
- [ ] Planet class
- [ ] Email simulator

**Certification projects**
- [ ] User configuration manager
- [ ] Budget app

</details>

### Advanced
<details>
<summary><strong>Core Concepts</strong></summary>

- [ ] Decorators and generators
- [ ] Context managers
- [ ] Async/await programming
- [ ] Testing with pytest
- [ ] Virtual environments and package management

</details>

<details>
<summary><strong>Projects/Labs</strong></summary>

- [ ] Coming soon...

</details>

---

## Repository Structure

```
[embrace_the_python]
├── PROJECT_IDEAS.md                     # Project ideas for practice
├── README.md                            # This file
├── RESOURCES.md                         # Learning resources and links
├── basics                               # Fundamental Python concepts (Complete)
│   ├── 0_learning_python.py             # Python basics p.1 (Sessions 1-2)
│   ├── 0_learning_python_2.py           # Basics in-depth p.2 (Sessions 3-5)
│   ├── 01_basics_io_and_print.py        # Basic I/O and print operations
│   ├── 02_variables_and_data_types.py   # Variables and type system
│   ├── 03_strings_and_formatting.py     # Complete string operations
│   ├── 04_numeric_operations.py         # Numbers and arithmetic operators
│   ├── 05_conditionals.py               # Booleans and control flow
│   ├── 06_functions.py                  # Functions and variable scope
│   └── BASICS_REVIEW.md                 # Overview of all concepts from Python Basics
├── exercises                            # Practice exercises
│   └── practice_exercises.py            # Beginner exercises with solutions
├── intermediate                         # Intermediate concepts 
│   ├── python_intermediate.py           # Loops and Sequences
│   └── python_intermediate_2.py         # Dictionaries and Sets (Coming Soon)
├── projects                             # Completed labs/workshops
│   ├── RPG_character.py                 #
│   ├── caesar_cypher.py                 #
│   └── pin_extractor.py                 #
└── requirements.txt                     # Python package dependencies
```

### About the Module Structure

The `basics/` directory contains two types of learning files:

**Topic-Specific Modules (01-06):**
- Focused, single-topic modules for targeted learning
- Numbered for sequential progression
- Each module is self-contained and independently executable
- Ideal for studying specific concepts

**Comprehensive Learning Files:**
- `learning_python.py` - Sessions 1-2: Python fundamentals and strings
- `learning_python_2.py` - Sessions 3-5: Numbers, conditionals, and functions
- Complete learning sessions with multiple topics
- Useful for comprehensive reviews

---

## How to Run the Code

### Prerequisites
- Python 3.x installed on your system
- A code editor (VS Code, PyCharm, etc.)

### Running Individual Files

1. Clone this repository:
```bash
git clone https://github.com/vanyaisme/embrace_the_python.git
cd embrace_the_python
```

2. Run any Python file:
```bash
# Run topic-specific modules (recommended for focused learning)
python basics/01_basics_io_and_print.py
python basics/02_variables_and_data_types.py
python basics/03_strings_and_formatting.py
python basics/04_numeric_operations.py
python basics/05_conditionals.py
python basics/06_functions.py

# Run comprehensive learning sessions
python basics/learning_python.py      # Sessions 1-2
python basics/learning_python_2.py    # Sessions 3-5

# Practice exercises
python exercises/practice_exercises.py
```

**Note:** Files with `input()` calls (like `05_conditionals.py` and `06_functions.py`) are interactive and will prompt you for input during execution.

### Setting Up Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Learning Resources

See [RESOURCES.md](RESOURCES.md) for a curated list of learning materials, tutorials, and helpful links.

## Project Ideas

Check out [PROJECT_IDEAS.md](PROJECT_IDEAS.md) for beginner-friendly project ideas to practice your Python skills.

---

## Current Progress

**Last Updated:** January 2026

- Completed: Python basics (I/O, variables, types, strings, numbers, conditionals, functions)
- Completed: Modular restructuring for focused topic-based learning
- In Progress: Practice exercises and advanced topics
- Next Up: Loops, sequences, dictionaries, and error handling

---

## Certifications & Courses

- [ ] FreeCodeCamp - Python Certification
- [ ] Additional courses (to be added)

---

## Connect

This is a personal learning repository, but feel free to:
- Suggest improvements or corrections
- Share learning resources
- Propose interesting project ideas

---

## License

This project is open source and available for educational purposes.

---

*Happy Coding!*
