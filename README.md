# Worksheet for Python Lab

## Part A - Project Structure
A short paragraph describing each command used in this part is included here. The commands created directories, created empty Python files, wrote the README content, and displayed the recursive directory tree for verification.

Separating code into src, tests, and docs is good practice because it keeps source files, test assets, and documentation organized. Even for small projects, this structure makes maintenance easier, helps collaborators understand the layout quickly, and reduces confusion when the project grows.

## Part B - Git Initialization and First Commit
The .gitignore file tells Git which files or folders to ignore so they do not show up as untracked changes. The patterns __pycache__/ and *.pyc matter because Python creates compiled bytecode files that should not be committed, while .env files often contain sensitive environment variables that should stay local.

The commit history shows the timeline of a project's development by recording when major changes were added, which helps collaborators review progress and understand the evolution of the codebase over time.

## Part C - Writing and Committing Python Code
```python
# src/utils.py

def square(n):
    return n * n


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def greet(name):
    return f"Hello, {name}!"
```

```python
# src/main.py
from utils import square, is_even, celsius_to_fahrenheit, greet


def main():
    value = input("Enter a number: ")
    try:
        number = float(value)
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"Square: {square(number)}")
    print(f"Even: {is_even(number)}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number):.2f}")
    print(greet("Student"))


if __name__ == "__main__":
    main()
```

Python connects main.py to utils.py through the import statement. When Python runs main.py, it looks for a module named utils in the same directory and loads the functions from that file so they can be used directly.

The program was tested with several sample inputs, including 4, 7, and 0, and produced the expected square, even/odd, Fahrenheit, and greeting output.

## Part D - Publishing to GitHub and Branch Workflow
The GitHub workflow uses branches to keep feature work separate from the main codebase. A new branch allows changes such as the greeting feature to be developed, reviewed, and merged without disturbing the main branch.
