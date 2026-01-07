# Learning Python using FreeCodeCamp curriculum

A comprehensive repository documenting my journey learning Python through FreeCodeCamp and various programming exercises.

## About This Repository

This repository serves as my personal learning log and practice space for Python programming. It's organized to track progress, practice concepts, and build a portfolio of small projects as I advance through Python fundamentals to more advanced topics.

## Learning Goals

- Master Python fundamentals (variables, data types, control flow)
- Understand object-oriented programming concepts
- Build practical applications and projects
- Develop problem-solving skills through exercises
- Create clean, well-documented code
- Follow Python best practices (PEP 8)

## Topics Covered

### Basics
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
- [x] Functions and scope
  - [x] Function definition and calling
  - [x] Parameters vs arguments
  - [x] Return statements
  - [x] Variable scope (LEGB rule)
  - [x] Built-in functions
- [ ] Loops and sequences
- [ ] Dictionaries and sets
- [ ] Error handling

### Intermediate
- [ ] Object-oriented programming (classes, inheritance)
- [ ] Error handling and exceptions
- [ ] Modules and packages
- [ ] Regular expressions
- [ ] Working with APIs
- [ ] Database operations

### Advanced
- [ ] Decorators and generators
- [ ] Context managers
- [ ] Async/await programming
- [ ] Testing with pytest
- [ ] Virtual environments and package management

## Project Structure

```
embrace_the_python/
│
├── .github/                         # GitHub configuration files
│
├── basics/                          # Fundamental Python concepts
│   ├── 01_basics_io_and_print.py    # Basic I/O and print operations
│   ├── 02_variables_and_data_types.py # Variables and type system
│   ├── 03_strings_and_formatting.py # Complete string operations
│   ├── 04_numeric_operations.py     # Numbers and arithmetic operators
│   ├── 05_conditionals.py           # Booleans and control flow
│   ├── 06_functions.py              # Functions and variable scope
│   ├── learning_python.py           # Comprehensive Python basics (Sessions 1-2)
│   └── learning_python_2.py         # Advanced topics (Sessions 3-5)
│
├── intermediate/                    # Intermediate concepts (coming soon)
│
├── projects/                        # Completed projects (coming soon)
│
├── exercises/                       # Practice exercises
│   └── practice_exercises.py        # Beginner exercises with solutions
│
├── .gitignore                       # Git ignore configuration
├── README.md                        # This file
├── RESOURCES.md                     # Learning resources and links
├── PROJECT_IDEAS.md                 # Project ideas for practice
└── requirements.txt                 # Python package dependencies
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

## Learning Resources

See [RESOURCES.md](RESOURCES.md) for a curated list of learning materials, tutorials, and helpful links.

## Project Ideas

Check out [PROJECT_IDEAS.md](PROJECT_IDEAS.md) for beginner-friendly project ideas to practice your Python skills.

## Current Progress

**Last Updated:** January 2026

- Completed: Python basics (I/O, variables, types, strings, numbers, conditionals, functions)
- Completed: Modular restructuring for focused topic-based learning
- In Progress: Practice exercises and advanced topics
- Next Up: Loops, sequences, dictionaries, and error handling

## Certifications & Courses

- [ ] FreeCodeCamp - Scientific Computing with Python
- [ ] Additional courses (to be added)

## Connect & Contribute

This is a personal learning repository, but feel free to:
- Suggest improvements or corrections
- Share learning resources
- Propose interesting project ideas

## Author

**Ivan Lutso**
- Learning Python through FreeCodeCamp
- Building practical skills for software development
- Documenting the learning journey

## License

This project is open source and available for educational purposes.

---

**Note:** This repository is continuously updated as I progress through my Python learning journey. Check back often for new content!

*Happy Coding!*