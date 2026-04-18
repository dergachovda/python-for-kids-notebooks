#!/usr/bin/env python3
"""Generate chapter 3-12 content: theory.md, exercises.ipynb, solutions.ipynb."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / ".content"
MANIFEST = CONTENT / "manifest.json"

# ---------------------------------------------------------------------------
# Chapter data
# ---------------------------------------------------------------------------

CHAPTERS = [
    {
        "slug": "chapter-03-conditionals",
        "title": "Conditionals",
        "emoji": "\U0001f6a6",
        "about": "Conditionals let your program make decisions.\nInstead of running every line, your code can choose what to do based on a condition.",
        "goals": [
            "Use if / elif / else",
            "Compare values with == , != , > , < , >= , <=",
            "Combine conditions with and / or",
            "Build decision logic",
        ],
        "tips": [
            "Use == to check if two values are equal.",
            "Use > , < , >= , <= for number comparisons.",
            "elif lets you check another condition if the first was False.",
            "else runs when nothing above matched.",
        ],
        "demo_code": [
            [
                "age = 11",
                "if age >= 10:",
                '    print("Welcome to coding club!")',
                "else:",
                '    print("Try next year.")',
            ],
            [
                'weather = "rain"',
                'if weather == "sun":',
                '    print("Play outside")',
                'elif weather == "rain":',
                '    print("Take an umbrella")',
                "else:",
                '    print("Check the sky again")',
            ],
        ],
        "exercises": [
            {
                "name": "Pass check",
                "task": "Ask for a score. Print Pass if score >= 60, else print Retry.",
                "hint": "Use int(input(...)) to get a number from the user.",
                "starter": [
                    'score = int(input("Score: "))',
                    '# Write if/else: print "Pass" if score >= 60, else print "Retry"',
                ],
                "solution": [
                    'score = int(input("Score: "))',
                    "if score >= 60:",
                    '    print("Pass")',
                    "else:",
                    '    print("Retry")',
                ],
            },
            {
                "name": "Color check",
                "task": "Ask for a color. If the color is blue, print a special message.",
                "hint": "Compare text with ==.  Use .lower() so BLue also works.",
                "starter": [
                    'color = input("Color: ").lower()',
                    '# If color is "blue" print something special, else print "Nice choice!"',
                ],
                "solution": [
                    'color = input("Color: ").lower()',
                    'if color == "blue":',
                    '    print("Blue is awesome!")',
                    "else:",
                    '    print("Nice choice!")',
                ],
            },
            {
                "name": "Temperature advice",
                "task": "Ask for the temperature and suggest what to wear.",
                "hint": "Use if/else with a number comparison.",
                "starter": [
                    'temp = int(input("Temperature: "))',
                    "# If temp > 25 suggest light clothes, else suggest a jacket",
                ],
                "solution": [
                    'temp = int(input("Temperature: "))',
                    "if temp > 25:",
                    '    print("Wear a t-shirt")',
                    "else:",
                    '    print("Wear a jacket")',
                ],
            },
            {
                "name": "Secret word",
                "task": 'Print "Correct" only if the user types python.',
                "hint": "Use == to compare the input with the word.",
                "starter": [
                    'word = input("Secret word: ")',
                    '# Print "Correct" if word equals "python", else "Try again"',
                ],
                "solution": [
                    'word = input("Secret word: ")',
                    'if word == "python":',
                    '    print("Correct")',
                    "else:",
                    '    print("Try again")',
                ],
            },
        ],
    },
    {
        "slug": "chapter-04-loops",
        "title": "Loops",
        "emoji": "\U0001f501",
        "about": "Loops repeat code so you don't have to type the same thing over and over.\nPython has two main loops: for and while.",
        "goals": [
            "Use for loops with range()",
            "Use while loops",
            "Control loops with break",
            "Understand range(start, stop, step)",
        ],
        "tips": [
            "range(1, 6) gives the numbers 1, 2, 3, 4, 5.",
            "A while loop keeps running while the condition is True.",
            "break exits the loop immediately.",
            "Indent the code inside the loop with 4 spaces.",
        ],
        "demo_code": [
            ["for n in range(1, 6):", "    print(n)"],
            [
                "count = 3",
                "while count > 0:",
                "    print(count)",
                "    count -= 1",
                'print("Go!")',
            ],
        ],
        "exercises": [
            {
                "name": "Count 1 to 10",
                "task": "Print the numbers from 1 to 10.",
                "hint": "Use range(1, 11) — the stop value is not included.",
                "starter": ["# Use a for loop with range to print numbers 1 to 10"],
                "solution": ["for n in range(1, 11):", "    print(n)"],
            },
            {
                "name": "Even numbers",
                "task": "Print even numbers from 2 to 20.",
                "hint": "range() accepts a third argument for the step size.",
                "starter": ["# Print even numbers from 2 to 20", "# Hint: range(start, stop, step)"],
                "solution": ["for n in range(2, 21, 2):", "    print(n)"],
            },
            {
                "name": "Countdown",
                "task": "Count down from 5 to 1, then print Go!",
                "hint": "Use a while loop that decreases the number each time.",
                "starter": [
                    "n = 5",
                    '# Count down to 1 using while, then print "Go!"',
                ],
                "solution": [
                    "n = 5",
                    "while n >= 1:",
                    "    print(n)",
                    "    n -= 1",
                    'print("Go!")',
                ],
            },
            {
                "name": "Stop early",
                "task": "Print numbers 1 to 10 but stop at 7.",
                "hint": "Use break inside an if check.",
                "starter": ["# Print 1 to 10 but use break to stop at 7"],
                "solution": [
                    "for n in range(1, 11):",
                    "    if n == 7:",
                    "        break",
                    "    print(n)",
                ],
            },
        ],
    },
    {
        "slug": "chapter-05-lists",
        "title": "Lists",
        "emoji": "\U0001f4da",
        "about": "Lists store many values in one variable.\nYou can add, remove, and loop through the items.",
        "goals": [
            "Create a list with square brackets",
            "Read items by index (starting at 0)",
            "Add and remove items",
            "Loop through a list with for",
        ],
        "tips": [
            "The first item has index 0, not 1.",
            "append() adds an item to the end.",
            "remove() deletes the first matching item.",
            "len(my_list) tells you how many items there are.",
        ],
        "demo_code": [
            [
                'fruits = ["apple", "banana", "mango"]',
                "print(fruits[0])",
                'fruits.append("orange")',
                "print(fruits)",
            ],
            [
                'pets = ["dog", "cat", "fish"]',
                "for pet in pets:",
                '    print("I like", pet)',
            ],
        ],
        "exercises": [
            {
                "name": "Snacks list",
                "task": "Create a list with 3 snacks and print it.",
                "hint": 'Use square brackets: ["a", "b", "c"]',
                "starter": ["# Create a list called snacks with 3 items", "snacks = []", "print(snacks)"],
                "solution": [
                    'snacks = ["chips", "nuts", "apple"]',
                    "print(snacks)",
                ],
            },
            {
                "name": "Change item",
                "task": "Replace the second item in a colors list.",
                "hint": "The second item has index 1.",
                "starter": [
                    'colors = ["red", "green", "blue"]',
                    '# Replace the second item with "yellow"',
                    "print(colors)",
                ],
                "solution": [
                    'colors = ["red", "green", "blue"]',
                    'colors[1] = "yellow"',
                    "print(colors)",
                ],
            },
            {
                "name": "Add and remove",
                "task": "Add one game, then remove another game.",
                "hint": "Use append() and remove().",
                "starter": [
                    'games = ["chess", "soccer", "tennis"]',
                    '# Add "coding" and remove "soccer"',
                    "print(games)",
                ],
                "solution": [
                    'games = ["chess", "soccer", "tennis"]',
                    'games.append("coding")',
                    'games.remove("soccer")',
                    "print(games)",
                ],
            },
            {
                "name": "Loop list",
                "task": "Print each school item on a new line.",
                "hint": "Use: for item in items:",
                "starter": [
                    'items = ["book", "pencil", "eraser"]',
                    "# Print each item using a for loop",
                ],
                "solution": [
                    'items = ["book", "pencil", "eraser"]',
                    "for item in items:",
                    "    print(item)",
                ],
            },
        ],
    },
    {
        "slug": "chapter-06-dictionaries-and-tuples",
        "title": "Dictionaries and Tuples",
        "emoji": "\U0001f5c2\ufe0f",
        "about": "Dictionaries store data as key-value pairs — like a real dictionary where each word has a meaning.\nTuples are like lists that cannot be changed after creation.",
        "goals": [
            "Create a dictionary with curly braces",
            "Read and update values by key",
            "Create tuples with parentheses",
            "Loop through dictionary keys",
        ],
        "tips": [
            "Dictionary keys must be unique.",
            'Use dict["key"] to read or set a value.',
            "Tuples use parentheses: (1, 2, 3).",
            "You cannot change a tuple after creating it.",
        ],
        "demo_code": [
            [
                'student = {"name": "Mila", "age": 11}',
                'print(student["name"])',
                'student["age"] = 12',
                "print(student)",
            ],
            [
                "point = (4, 7)",
                'print("x:", point[0])',
                'print("y:", point[1])',
            ],
        ],
        "exercises": [
            {
                "name": "Profile dict",
                "task": "Create a profile with name, age, and city.",
                "hint": 'Use curly braces: {"key": "value", ...}',
                "starter": [
                    "# Create a dictionary called profile with keys: name, age, city",
                    "profile = {}",
                    "print(profile)",
                ],
                "solution": [
                    'profile = {"name": "Alex", "age": 10, "city": "Kyiv"}',
                    "print(profile)",
                ],
            },
            {
                "name": "Update value",
                "task": "Change the age in a profile dictionary.",
                "hint": 'profile["age"] = new_value',
                "starter": [
                    'profile = {"name": "Alex", "age": 10}',
                    "# Change age to 11",
                    "print(profile)",
                ],
                "solution": [
                    'profile = {"name": "Alex", "age": 10}',
                    'profile["age"] = 11',
                    "print(profile)",
                ],
            },
            {
                "name": "Tuple read",
                "task": "Create a tuple and print the second value.",
                "hint": "The second value has index 1.",
                "starter": [
                    "numbers = (8, 3, 5)",
                    "# Print the second value",
                ],
                "solution": ["numbers = (8, 3, 5)", "print(numbers[1])"],
            },
            {
                "name": "Dict loop",
                "task": "Print each key and value from a marks dictionary.",
                "hint": "Use: for key in marks:",
                "starter": [
                    'marks = {"math": 95, "science": 98}',
                    "# Print each subject and its mark",
                ],
                "solution": [
                    'marks = {"math": 95, "science": 98}',
                    "for key in marks:",
                    "    print(key, marks[key])",
                ],
            },
        ],
    },
    {
        "slug": "chapter-07-functions",
        "title": "Functions",
        "emoji": "\U0001f6e0\ufe0f",
        "about": "Functions are reusable blocks of code that you can call by name.\nThey help you avoid repeating yourself and keep programs organized.",
        "goals": [
            "Define functions with def",
            "Use parameters to pass data in",
            "Return values with return",
            "Break big tasks into small functions",
        ],
        "tips": [
            "Give your function a clear name that describes what it does.",
            "Use return when the function should give back a value.",
            "One function should do one job.",
            "Call the function by writing its name with parentheses.",
        ],
        "demo_code": [
            [
                "def greet(name):",
                '    print("Hello", name)',
                "",
                'greet("Mila")',
            ],
            [
                "def add(a, b):",
                "    return a + b",
                "",
                "print(add(3, 4))",
            ],
        ],
        "exercises": [
            {
                "name": "Say hi",
                "task": 'Create a function say_hi() that prints "Hi!"',
                "hint": "No parameters needed — just def say_hi(): ...",
                "starter": [
                    '# Define a function say_hi() that prints "Hi!"',
                    "",
                    "",
                    "# Call your function below",
                    "say_hi()",
                ],
                "solution": [
                    "def say_hi():",
                    '    print("Hi!")',
                    "",
                    "say_hi()",
                ],
            },
            {
                "name": "Welcome by name",
                "task": "Create welcome(name) that prints a greeting.",
                "hint": "Use one parameter inside the parentheses.",
                "starter": [
                    "# Define welcome(name) that prints a greeting message",
                    "",
                    "",
                    "# Call it",
                    'welcome("Alex")',
                ],
                "solution": [
                    "def welcome(name):",
                    '    print("Welcome,", name)',
                    "",
                    'welcome("Alex")',
                ],
            },
            {
                "name": "Square",
                "task": "Create square(n) that returns n * n.",
                "hint": "Use the return keyword.",
                "starter": [
                    "# Define square(n) that returns n * n",
                    "",
                    "",
                    "# Test it",
                    "print(square(6))",
                ],
                "solution": [
                    "def square(n):",
                    "    return n * n",
                    "",
                    "print(square(6))",
                ],
            },
            {
                "name": "Pass check function",
                "task": "Create passed(score) that returns True if score >= 60.",
                "hint": "Return a boolean expression directly.",
                "starter": [
                    "# Define passed(score) that returns True if score >= 60",
                    "",
                    "",
                    "# Test it",
                    "print(passed(75))",
                ],
                "solution": [
                    "def passed(score):",
                    "    return score >= 60",
                    "",
                    "print(passed(75))",
                ],
            },
        ],
    },
    {
        "slug": "chapter-08-files-and-errors",
        "title": "Files and Errors",
        "emoji": "\U0001f4c1",
        "about": "Files let you save data so it survives after the program stops.\nError handling keeps your program from crashing when something unexpected happens.",
        "goals": [
            "Write text to a file",
            "Read text from a file",
            "Append data to a file",
            "Handle errors with try / except",
        ],
        "tips": [
            'Use with open(...) as f: to work with files safely.',
            'Always set encoding="utf-8" when opening files.',
            "Mode 'w' writes (overwrites), 'r' reads, 'a' appends.",
            "Wrap risky code in try / except to catch errors.",
        ],
        "demo_code": [
            [
                'with open("notes.txt", "w", encoding="utf-8") as f:',
                '    f.write("I love Python\\n")',
                'with open("notes.txt", "r", encoding="utf-8") as f:',
                "    print(f.read())",
            ],
            [
                "try:",
                '    value = int(input("Enter number: "))',
                "    print(value)",
                "except ValueError:",
                '    print("Not a number")',
            ],
        ],
        "exercises": [
            {
                "name": "Write story",
                "task": "Write one sentence to story.txt.",
                "hint": 'Use open("story.txt", "w", encoding="utf-8").',
                "starter": [
                    "# Write one sentence to story.txt",
                    '# with open("story.txt", "w", encoding="utf-8") as f:',
                    "#     f.write(...)",
                ],
                "solution": [
                    'with open("story.txt", "w", encoding="utf-8") as f:',
                    '    f.write("Today I learned loops!\\n")',
                    'print("Saved")',
                ],
            },
            {
                "name": "Read story",
                "task": "Read story.txt and print the text.",
                "hint": 'Use open("story.txt", "r", encoding="utf-8").',
                "starter": [
                    "# Read story.txt and print its content",
                ],
                "solution": [
                    'with open("story.txt", "r", encoding="utf-8") as f:',
                    "    print(f.read())",
                ],
            },
            {
                "name": "Append line",
                "task": "Add one more line to story.txt.",
                "hint": 'Use mode "a" for append.',
                "starter": [
                    '# Add one more line to story.txt using mode "a"',
                ],
                "solution": [
                    'with open("story.txt", "a", encoding="utf-8") as f:',
                    '    f.write("Python is fun!\\n")',
                    'print("Line added")',
                ],
            },
            {
                "name": "Safe double",
                "task": "Ask for a number and print number * 2 — handle bad input.",
                "hint": "Use try / except ValueError.",
                "starter": [
                    "# Ask for a number and print it doubled",
                    "# Use try/except to handle bad input",
                ],
                "solution": [
                    "try:",
                    '    n = int(input("Number: "))',
                    "    print(n * 2)",
                    "except ValueError:",
                    '    print("Please type digits only")',
                ],
            },
        ],
    },
    {
        "slug": "chapter-09-modules-and-project-structure",
        "title": "Modules and Project Structure",
        "emoji": "\U0001f9e9",
        "about": "Modules are files full of useful code that you can import into your programs.\nPython comes with many built-in modules like random and math.",
        "goals": [
            "Import a module with import",
            "Use random and math modules",
            "Import specific items with from ... import",
            "Understand how to organize project files",
        ],
        "tips": [
            "import random gives you the whole random module.",
            "from random import randint imports just one function.",
            "Keep helper code in separate .py files.",
            "Use short, clear file names for your modules.",
        ],
        "demo_code": [
            ["import random", "print(random.randint(1, 10))"],
            ["import math", "print(math.sqrt(81))"],
        ],
        "exercises": [
            {
                "name": "Dice roll",
                "task": "Print a random number from 1 to 6.",
                "hint": "Use random.randint(1, 6).",
                "starter": ["# Import random and print a number from 1 to 6"],
                "solution": ["import random", "print(random.randint(1, 6))"],
            },
            {
                "name": "Square root",
                "task": "Print the square root of 49 using the math module.",
                "hint": "Use math.sqrt(49).",
                "starter": ["# Import math and print the square root of 49"],
                "solution": ["import math", "print(math.sqrt(49))"],
            },
            {
                "name": "Import one function",
                "task": "Import only randint and print a random number.",
                "hint": "from random import randint",
                "starter": [
                    "# Import only randint from random",
                    "# Print a random number from 1 to 100",
                ],
                "solution": [
                    "from random import randint",
                    "print(randint(1, 100))",
                ],
            },
            {
                "name": "Simple helper module",
                "task": "Create a greet function and call it.",
                "hint": 'Define greet(name) that returns a greeting string.',
                "starter": [
                    '# Define a greet(name) function that returns "Hello, {name}!"',
                    "# Then call it and print the result",
                    "",
                    "def greet(name):",
                    "    pass  # Replace pass with your return statement",
                    "",
                    'print(greet("Mila"))',
                ],
                "solution": [
                    "def greet(name):",
                    '    return f"Hello, {name}!"',
                    "",
                    'print(greet("Mila"))',
                ],
            },
        ],
    },
    {
        "slug": "chapter-10-classes-and-objects",
        "title": "Classes and Objects",
        "emoji": "\U0001f3d7\ufe0f",
        "about": "A class is a blueprint for creating objects.\nObjects bundle data (attributes) and actions (methods) together.",
        "goals": [
            "Create a class with class",
            "Use __init__ to set up attributes",
            "Add methods that use self",
            "Model real-world things as objects",
        ],
        "tips": [
            "self refers to the current object.",
            "Methods are just functions defined inside a class.",
            "__init__ runs automatically when you create an object.",
            "Use dot notation: object.attribute or object.method().",
        ],
        "demo_code": [
            [
                "class Robot:",
                "    def __init__(self, name):",
                "        self.name = name",
                "",
                "    def say_hi(self):",
                '        print("Hi, I am", self.name)',
                "",
                'r1 = Robot("Bolt")',
                "r1.say_hi()",
            ],
            [
                "class Player:",
                "    def __init__(self, name):",
                "        self.name = name",
                "        self.points = 0",
                "",
                "    def add_points(self, value):",
                "        self.points += value",
                "",
                'p = Player("Mila")',
                "p.add_points(5)",
                "print(p.points)",
            ],
        ],
        "exercises": [
            {
                "name": "Pet class",
                "task": "Create a Pet class with name and kind.",
                "hint": "Store both values in __init__ using self.",
                "starter": [
                    "class Pet:",
                    "    def __init__(self, name, kind):",
                    "        pass  # Store name and kind as self.name and self.kind",
                    "",
                    'p = Pet("Luna", "cat")',
                    "print(p.name, p.kind)",
                ],
                "solution": [
                    "class Pet:",
                    "    def __init__(self, name, kind):",
                    "        self.name = name",
                    "        self.kind = kind",
                    "",
                    'p = Pet("Luna", "cat")',
                    "print(p.name, p.kind)",
                ],
            },
            {
                "name": "Pet speak",
                "task": "Add a speak() method to the Pet class.",
                "hint": "Use self.name inside the method.",
                "starter": [
                    "class Pet:",
                    "    def __init__(self, name):",
                    "        self.name = name",
                    "",
                    "    def speak(self):",
                    "        pass  # Print a greeting using self.name",
                    "",
                    'p = Pet("Luna")',
                    "p.speak()",
                ],
                "solution": [
                    "class Pet:",
                    "    def __init__(self, name):",
                    "        self.name = name",
                    "",
                    "    def speak(self):",
                    '        print(self.name, "says hello!")',
                    "",
                    'p = Pet("Luna")',
                    "p.speak()",
                ],
            },
            {
                "name": "Counter class",
                "task": "Create a Counter with value=0 and an inc() method.",
                "hint": "inc() should increase self.value by 1.",
                "starter": [
                    "class Counter:",
                    "    def __init__(self):",
                    "        pass  # Set self.value to 0",
                    "",
                    "    def inc(self):",
                    "        pass  # Increase self.value by 1",
                    "",
                    "c = Counter()",
                    "c.inc()",
                    "print(c.value)",
                ],
                "solution": [
                    "class Counter:",
                    "    def __init__(self):",
                    "        self.value = 0",
                    "",
                    "    def inc(self):",
                    "        self.value += 1",
                    "",
                    "c = Counter()",
                    "c.inc()",
                    "print(c.value)",
                ],
            },
            {
                "name": "Student pass",
                "task": "Create a Student class with a passed() method.",
                "hint": "Return score >= 60.",
                "starter": [
                    "class Student:",
                    "    def __init__(self, name, score):",
                    "        pass  # Store name and score",
                    "",
                    "    def passed(self):",
                    "        pass  # Return True if score >= 60",
                    "",
                    's = Student("Mila", 75)',
                    "print(s.passed())",
                ],
                "solution": [
                    "class Student:",
                    "    def __init__(self, name, score):",
                    "        self.name = name",
                    "        self.score = score",
                    "",
                    "    def passed(self):",
                    "        return self.score >= 60",
                    "",
                    's = Student("Mila", 75)',
                    "print(s.passed())",
                ],
            },
        ],
    },
    {
        "slug": "chapter-11-turtle-graphics",
        "title": "Turtle Graphics",
        "emoji": "\U0001f422",
        "about": "Turtle draws pictures using simple movement commands.\nYou tell the turtle to move forward, turn, and change colors — and it draws on the screen.",
        "goals": [
            "Import and use the turtle module",
            "Move and turn the turtle",
            "Draw shapes with loops",
            "Change pen color and size",
        ],
        "tips": [
            "forward(n) moves the turtle n pixels.",
            "left(d) and right(d) turn by d degrees.",
            "Use a for loop to draw shapes with equal sides.",
            "pencolor() and pensize() change the pen style.",
        ],
        "turtle_note": (
            "**Important:** Turtle graphics open a separate window and do not work "
            "inside Jupyter notebooks. Save your code as a .py file and run it with "
            "`python filename.py`, or use IDLE."
        ),
        "demo_code": [
            [
                "import turtle",
                "t = turtle.Turtle()",
                "for _ in range(4):",
                "    t.forward(100)",
                "    t.right(90)",
                "turtle.done()",
            ],
            [
                "import turtle",
                "t = turtle.Turtle()",
                't.pencolor("blue")',
                "t.forward(120)",
                "turtle.done()",
            ],
        ],
        "exercises": [
            {
                "name": "Triangle",
                "task": "Draw a triangle using turtle.",
                "hint": "3 sides, turn 120 degrees each time.",
                "starter": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    "# Draw a triangle: 3 sides, 120-degree turns",
                    "",
                    "turtle.done()",
                ],
                "solution": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    "for _ in range(3):",
                    "    t.forward(100)",
                    "    t.left(120)",
                    "turtle.done()",
                ],
            },
            {
                "name": "Hexagon",
                "task": "Draw a hexagon.",
                "hint": "6 sides, turn 60 degrees each time.",
                "starter": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    "# Draw a hexagon: 6 sides, 60-degree turns",
                    "",
                    "turtle.done()",
                ],
                "solution": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    "for _ in range(6):",
                    "    t.forward(80)",
                    "    t.right(60)",
                    "turtle.done()",
                ],
            },
            {
                "name": "Color line",
                "task": "Draw a thick red line.",
                "hint": "Use pencolor() and pensize().",
                "starter": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    "# Set pen color to red, size to 4, and draw a line",
                    "",
                    "turtle.done()",
                ],
                "solution": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    't.pencolor("red")',
                    "t.pensize(4)",
                    "t.forward(150)",
                    "turtle.done()",
                ],
            },
            {
                "name": "Star",
                "task": "Draw a five-pointed star.",
                "hint": "5 points, turn 144 degrees each time.",
                "starter": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    "# Draw a star: 5 points, 144-degree turns",
                    "",
                    "turtle.done()",
                ],
                "solution": [
                    "import turtle",
                    "t = turtle.Turtle()",
                    "for _ in range(5):",
                    "    t.forward(150)",
                    "    t.right(144)",
                    "turtle.done()",
                ],
            },
        ],
    },
    {
        "slug": "chapter-12-mini-projects",
        "title": "Mini Projects",
        "emoji": "\U0001f3ae",
        "about": "Mini projects combine everything you have learned into complete little programs.\nThis is where you put your skills together!",
        "goals": [
            "Plan a tiny project before coding",
            "Build step by step",
            "Test each feature",
            "Improve the user experience",
        ],
        "tips": [
            "Start with the simplest version first.",
            "Add one feature at a time.",
            "Test after every change.",
            "Ask a friend to try your program!",
        ],
        "demo_code": [
            [
                "import random",
                "secret = random.randint(1, 10)",
                'guess = int(input("Guess 1-10: "))',
                "if guess == secret:",
                '    print("You win!")',
                "else:",
                '    print("Secret was", secret)',
            ],
            [
                "score = 0",
                'if input("2 + 2 = ") == "4":',
                "    score += 1",
                'print("Score:", score)',
            ],
        ],
        "exercises": [
            {
                "name": "3-question quiz",
                "task": "Ask 3 questions and count correct answers.",
                "hint": "Use a score variable. Add 1 for each correct answer.",
                "starter": [
                    "score = 0",
                    "# Ask 3 questions using input()",
                    "# Add 1 to score for each correct answer",
                    "",
                    'print("Final score:", score)',
                ],
                "solution": [
                    "score = 0",
                    'if input("Sky color on clear day? ").lower() == "blue":',
                    "    score += 1",
                    'if input("5 + 5 = ") == "10":',
                    "    score += 1",
                    'if input("Python is fun? ").lower() == "yes":',
                    "    score += 1",
                    'print("Final score:", score)',
                ],
            },
            {
                "name": "Rock paper scissors",
                "task": "Make a text-based rock-paper-scissors game.",
                "hint": "Use random.choice() for the computer pick.",
                "starter": [
                    "import random",
                    'options = ["rock", "paper", "scissors"]',
                    "computer = random.choice(options)",
                    'player = input("rock/paper/scissors: ").lower()',
                    'print("Computer:", computer)',
                    "# Compare player and computer to decide the winner",
                    '# Print "Draw", "You win", or "You lose"',
                ],
                "solution": [
                    "import random",
                    'options = ["rock", "paper", "scissors"]',
                    "computer = random.choice(options)",
                    'player = input("rock/paper/scissors: ").lower()',
                    'print("Computer:", computer)',
                    "if player == computer:",
                    '    print("Draw")',
                    "elif (",
                    '    (player == "rock" and computer == "scissors")',
                    '    or (player == "paper" and computer == "rock")',
                    '    or (player == "scissors" and computer == "paper")',
                    "):",
                    '    print("You win")',
                    "else:",
                    '    print("You lose")',
                ],
            },
            {
                "name": "Best score",
                "task": "Store scores in a list and print the highest.",
                "hint": "Use max(list).",
                "starter": [
                    "scores = [10, 18, 7, 21]",
                    "# Print the highest score from the list",
                ],
                "solution": [
                    "scores = [10, 18, 7, 21]",
                    'print("Best score:", max(scores))',
                ],
            },
            {
                "name": "Project steps",
                "task": "Print 3 steps for your own project idea.",
                "hint": "Use a list and a for loop.",
                "starter": [
                    "# Create a list of 3 project steps",
                    "# Print each step using a for loop",
                ],
                "solution": [
                    'steps = ["Idea", "Build first version", "Test and improve"]',
                    "for step in steps:",
                    "    print(step)",
                ],
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Notebook builder
# ---------------------------------------------------------------------------


def build_notebook(chapter, mode):
    """Build a Jupyter notebook dict for *mode* ('exercises' or 'solutions')."""
    cells = []

    if mode == "exercises":
        # Header
        cells.append(_md_cell([
            f"# {chapter['title']} {chapter['emoji']}",
            "",
            "Learn by doing. Run the examples, then complete all exercises.",
        ]))

        # Turtle compatibility warning
        if "turtle_note" in chapter:
            cells.append(_md_cell([
                "> \u26a0\ufe0f " + chapter["turtle_note"],
                "",
                "The code below **will not draw** inside this notebook.",
                "Copy each exercise into a `.py` file and run it from the terminal.",
            ]))

        # Demo examples
        for i, block in enumerate(chapter["demo_code"], start=1):
            cells.append(_md_cell([f"## Example {i}"]))
            cells.append(_code_cell(block))

        # Exercises with STARTER code (not solutions)
        for i, ex in enumerate(chapter["exercises"], start=1):
            cells.append(_md_cell([
                f"## Exercise {i} \u2014 {ex['name']}",
                f"TODO: {ex['task']}",
                "",
                f"Hint: {ex['hint']}",
            ]))
            cells.append(_code_cell(ex["starter"]))

        # Try-it-yourself
        cells.append(_md_cell([
            "## Try It Yourself \u2b50",
            "1. Change one example and see what happens.",
            "2. Add one extra feature to an exercise.",
            "3. Share your result with a teacher or friend.",
        ]))
        cells.append(_code_cell(["# Your playground", 'print("Experiment here!")']))

    else:
        # Solutions notebook
        cells.append(_md_cell([
            f"# {chapter['title']} \u2014 Solutions \u2705",
            "",
            "Solved versions of all chapter exercises.",
        ]))

        for i, ex in enumerate(chapter["exercises"], start=1):
            cells.append(_md_cell([
                f"## Exercise {i} \u2014 {ex['name']}",
                f"Task: {ex['task']}",
            ]))
            cells.append(_code_cell(ex["solution"]))

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.14"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def _md_cell(source_lines):
    return {
        "cell_type": "markdown",
        "metadata": {"language": "markdown"},
        "source": source_lines,
    }


def _code_cell(source_lines):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"language": "python"},
        "outputs": [],
        "source": source_lines,
    }


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------


def write_chapter(chapter):
    chapter_dir = CONTENT / chapter["slug"]
    chapter_dir.mkdir(parents=True, exist_ok=True)

    # --- theory.md (enriched with demo-code examples) ---
    lines = [
        f"# {chapter['title']}",
        "",
        "Welcome to the next step of your Python journey.",
        "",
        "## What is this chapter about?",
        "",
    ]
    for paragraph in chapter["about"].split("\n"):
        lines.append(paragraph)
    lines.append("")
    lines.append("## What you learn in this chapter")
    lines.append("")
    for goal in chapter["goals"]:
        lines.append(f"- {goal}")

    lines.extend([
        "",
        "## Key idea",
        "",
        f"{chapter['title']} help you write stronger and smarter programs.",
        "",
    ])

    # Include demo code so students see examples BEFORE exercises
    lines.append("## Examples")
    lines.append("")
    for i, block in enumerate(chapter["demo_code"], start=1):
        lines.append(f"### Example {i}")
        lines.append("")
        lines.append("```python")
        lines.extend(block)
        lines.append("```")
        lines.append("")

    # Turtle note in theory
    if "turtle_note" in chapter:
        lines.append(f"> {chapter['turtle_note']}")
        lines.append("")

    lines.append("## Quick tips")
    lines.append("")
    for tip in chapter["tips"]:
        lines.append(f"- {tip}")

    lines.extend(["", "Next: Open `exercises.ipynb` and complete each TODO block."])

    (chapter_dir / "theory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # --- notebooks ---
    _write_notebook(chapter_dir / "exercises.ipynb", build_notebook(chapter, "exercises"))
    _write_notebook(chapter_dir / "solutions.ipynb", build_notebook(chapter, "solutions"))


def _write_notebook(path, nb_dict):
    path.write_text(
        json.dumps(nb_dict, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def update_manifest():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    existing = {entry["slug"] for entry in data["chapters"]}

    new_entries = [
        {
            "slug": ch["slug"],
            "title": ch["title"],
            "practice_files": ["theory.md", "exercises.ipynb"],
            "solution_files": ["solutions.ipynb"],
        }
        for ch in CHAPTERS
        if ch["slug"] not in existing
    ]

    if not new_entries:
        return

    # Keep bonus project at the end
    bonus = None
    kept = []
    for entry in data["chapters"]:
        if entry["slug"] == "bonus-mini-project":
            bonus = entry
        else:
            kept.append(entry)

    kept.extend(new_entries)
    if bonus is not None:
        kept.append(bonus)

    data["chapters"] = kept
    MANIFEST.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    for chapter in CHAPTERS:
        write_chapter(chapter)

    update_manifest()
    print(f"Created or updated {len(CHAPTERS)} chapters and synced manifest.")
