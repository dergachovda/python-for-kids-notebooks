#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / ".content"
MANIFEST = CONTENT / "manifest.json"

CHAPTERS = [
    {
        "slug": "chapter-03-conditionals",
        "title": "Conditionals",
        "emoji": "🚦",
        "about": "Conditionals let your program make decisions.",
        "goals": ["Use if / elif / else", "Compare values", "Use and/or", "Build decision logic"],
        "tips": ["Use == for equality", "Use >, <, >=, <= for number checks", "Use elif for middle cases"],
        "demo_code": [
            ["age = 11", "if age >= 10:", "    print(\"Welcome to coding club!\")", "else:", "    print(\"Try next year.\")"],
            ["weather = \"rain\"", "if weather == \"sun\":", "    print(\"Play outside\")", "elif weather == \"rain\":", "    print(\"Take an umbrella\")", "else:", "    print(\"Check the sky again\")"],
        ],
        "exercises": [
            {"name": "Pass check", "task": "Ask for score. Print Pass if score >= 60 else Retry.", "hint": "Use int(input(...)).", "solution": ["score = int(input(\"Score: \\"))", "if score >= 60:", "    print(\"Pass\")", "else:", "    print(\"Retry\")"]},
            {"name": "Color check", "task": "Ask for color. If color is blue print special text.", "hint": "Compare text with ==.", "solution": ["color = input(\"Color: \").lower()", "if color == \"blue\":", "    print(\"Blue is awesome!\")", "else:", "    print(\"Nice choice!\")"]},
            {"name": "Temperature advice", "task": "Ask for temperature and print clothing advice.", "hint": "Use if/else with number compare.", "solution": ["temp = int(input(\"Temperature: \\"))", "if temp > 25:", "    print(\"Wear a t-shirt\")", "else:", "    print(\"Wear a jacket\")"]},
            {"name": "Secret word", "task": "Print Correct only if user enters python.", "hint": "Use == with string.", "solution": ["word = input(\"Secret word: \")", "if word == \"python\":", "    print(\"Correct\")", "else:", "    print(\"Try again\")"]},
        ],
    },
    {
        "slug": "chapter-04-loops",
        "title": "Loops",
        "emoji": "🔁",
        "about": "Loops repeat code and save time.",
        "goals": ["Use for loops", "Use while loops", "Use range", "Stop loops with break"],
        "tips": ["range(1, 6) gives 1..5", "while runs while condition is true", "break exits loop"],
        "demo_code": [
            ["for n in range(1, 6):", "    print(n)"],
            ["count = 3", "while count > 0:", "    print(count)", "    count -= 1", "print(\"Go!\")"],
        ],
        "exercises": [
            {"name": "Count 1 to 10", "task": "Print numbers from 1 to 10.", "hint": "Use range(1, 11).", "solution": ["for n in range(1, 11):", "    print(n)"]},
            {"name": "Even numbers", "task": "Print even numbers from 2 to 20.", "hint": "Use step 2 in range.", "solution": ["for n in range(2, 21, 2):", "    print(n)"]},
            {"name": "Countdown", "task": "Countdown 5 to 1 then print Go!", "hint": "Use while loop.", "solution": ["n = 5", "while n >= 1:", "    print(n)", "    n -= 1", "print(\"Go!\")"]},
            {"name": "Stop early", "task": "Print 1..10 but stop at 7.", "hint": "Use break.", "solution": ["for n in range(1, 11):", "    if n == 7:", "        break", "    print(n)"]},
        ],
    },
    {
        "slug": "chapter-05-lists",
        "title": "Lists",
        "emoji": "📚",
        "about": "Lists store many values in one variable.",
        "goals": ["Create lists", "Read items by index", "Change items", "Loop through lists"],
        "tips": ["Index starts at 0", "append() adds item", "remove() removes by value"],
        "demo_code": [
            ["fruits = [\"apple\", \"banana\", \"mango\"]", "print(fruits[0])", "fruits.append(\"orange\")", "print(fruits)"],
            ["pets = [\"dog\", \"cat\", \"fish\"]", "for pet in pets:", "    print(\"I like\", pet)"],
        ],
        "exercises": [
            {"name": "Snacks list", "task": "Create list with 3 snacks and print it.", "hint": "Use square brackets.", "solution": ["snacks = [\"chips\", \"nuts\", \"apple\"]", "print(snacks)"]},
            {"name": "Change item", "task": "Replace second item in colors list.", "hint": "Second index is 1.", "solution": ["colors = [\"red\", \"green\", \"blue\"]", "colors[1] = \"yellow\"", "print(colors)"]},
            {"name": "Add and remove", "task": "Add one game then remove one game.", "hint": "Use append and remove.", "solution": ["games = [\"chess\", \"soccer\", \"tennis\"]", "games.append(\"coding\")", "games.remove(\"soccer\")", "print(games)"]},
            {"name": "Loop list", "task": "Print each school item on a new line.", "hint": "Use for item in items.", "solution": ["items = [\"book\", \"pencil\", \"eraser\"]", "for item in items:", "    print(item)"]},
        ],
    },
    {
        "slug": "chapter-06-dictionaries-and-tuples",
        "title": "Dictionaries and Tuples",
        "emoji": "🗂️",
        "about": "Dictionaries use key-value pairs. Tuples store fixed values.",
        "goals": ["Create dictionaries", "Read/update dictionary values", "Create tuples", "Loop dictionary keys"],
        "tips": ["Dictionary keys are unique", "Use dict[key] to access value", "Tuples use parentheses"],
        "demo_code": [
            ["student = {\"name\": \"Mila\", \"age\": 11}", "print(student[\"name\"])", "student[\"age\"] = 12", "print(student)"],
            ["point = (4, 7)", "print(\"x:\", point[0])", "print(\"y:\", point[1])"],
        ],
        "exercises": [
            {"name": "Profile dict", "task": "Create profile with name, age, city.", "hint": "Use curly braces.", "solution": ["profile = {\"name\": \"Alex\", \"age\": 10, \"city\": \"Kyiv\"}", "print(profile)"]},
            {"name": "Update value", "task": "Change age in profile dictionary.", "hint": "profile['age'] = ...", "solution": ["profile = {\"name\": \"Alex\", \"age\": 10}", "profile[\"age\"] = 11", "print(profile)"]},
            {"name": "Tuple read", "task": "Create tuple and print second value.", "hint": "Use index 1.", "solution": ["numbers = (8, 3, 5)", "print(numbers[1])"]},
            {"name": "Dict loop", "task": "Print each key and value from marks dictionary.", "hint": "for key in marks", "solution": ["marks = {\"math\": 95, \"science\": 98}", "for key in marks:", "    print(key, marks[key])"]},
        ],
    },
    {
        "slug": "chapter-07-functions",
        "title": "Functions",
        "emoji": "🛠️",
        "about": "Functions are reusable blocks of code.",
        "goals": ["Define functions", "Use parameters", "Return values", "Break big tasks into small parts"],
        "tips": ["Use clear names", "Use return when needed", "One function = one job"],
        "demo_code": [
            ["def greet(name):", "    print(\"Hello\", name)", "", "greet(\"Mila\")"],
            ["def add(a, b):", "    return a + b", "", "print(add(3, 4))"],
        ],
        "exercises": [
            {"name": "Say hi", "task": "Create say_hi() that prints Hi!", "hint": "No parameters needed.", "solution": ["def say_hi():", "    print(\"Hi!\")", "", "say_hi()"]},
            {"name": "Welcome by name", "task": "Create welcome(name) and print message.", "hint": "Use one parameter.", "solution": ["def welcome(name):", "    print(\"Welcome,\", name)", "", "welcome(\"Alex\")"]},
            {"name": "Square", "task": "Create square(n) that returns n*n.", "hint": "Use return keyword.", "solution": ["def square(n):", "    return n * n", "", "print(square(6))"]},
            {"name": "Pass check function", "task": "Create passed(score) returning True if >= 60.", "hint": "Return boolean expression.", "solution": ["def passed(score):", "    return score >= 60", "", "print(passed(75))"]},
        ],
    },
    {
        "slug": "chapter-08-files-and-errors",
        "title": "Files and Errors",
        "emoji": "📁",
        "about": "Files help save data. Error handling keeps programs safe.",
        "goals": ["Write files", "Read files", "Append data", "Handle input errors"],
        "tips": ["Use with open(...) for files", "Use utf-8 encoding", "Use try/except for risky code"],
        "demo_code": [
            ["with open(\"notes.txt\", \"w\", encoding=\"utf-8\") as f:", "    f.write(\"I love Python\\n\")", "with open(\"notes.txt\", \"r\", encoding=\"utf-8\") as f:", "    print(f.read())"],
            ["try:", "    value = int(input(\"Enter number: \"))", "    print(value)", "except ValueError:", "    print(\"Not a number\")"],
        ],
        "exercises": [
            {"name": "Write story", "task": "Write one sentence to story.txt.", "hint": "Use mode w.", "solution": ["with open(\"story.txt\", \"w\", encoding=\"utf-8\") as f:", "    f.write(\"Today I learned loops!\\n\")", "print(\"Saved\")"]},
            {"name": "Read story", "task": "Read story.txt and print text.", "hint": "Use mode r.", "solution": ["with open(\"story.txt\", \"r\", encoding=\"utf-8\") as f:", "    print(f.read())"]},
            {"name": "Append line", "task": "Add one more line to story.txt.", "hint": "Use mode a.", "solution": ["with open(\"story.txt\", \"a\", encoding=\"utf-8\") as f:", "    f.write(\"Python is fun!\\n\")", "print(\"Line added\")"]},
            {"name": "Safe double", "task": "Ask for a number and print number*2 safely.", "hint": "Use try/except ValueError.", "solution": ["try:", "    n = int(input(\"Number: \"))", "    print(n * 2)", "except ValueError:", "    print(\"Please type digits only\")"]},
        ],
    },
    {
        "slug": "chapter-09-modules-and-project-structure",
        "title": "Modules and Project Structure",
        "emoji": "🧩",
        "about": "Modules help you split code into reusable files.",
        "goals": ["Import modules", "Use random and math", "Understand from ... import", "Organize project files"],
        "tips": ["Keep helper code in modules", "Use short file names", "Import only what you need"],
        "demo_code": [
            ["import random", "print(random.randint(1, 10))"],
            ["import math", "print(math.sqrt(81))"],
        ],
        "exercises": [
            {"name": "Dice roll", "task": "Print a random number from 1 to 6.", "hint": "Use random.randint.", "solution": ["import random", "print(random.randint(1, 6))"]},
            {"name": "Square root", "task": "Print sqrt(49) using math module.", "hint": "Use math.sqrt.", "solution": ["import math", "print(math.sqrt(49))"]},
            {"name": "Import one function", "task": "Import only randint and print random number.", "hint": "from random import randint", "solution": ["from random import randint", "print(randint(1, 100))"]},
            {"name": "Simple helper module", "task": "Create helper.py greet function and call from main file.", "hint": "Two-file example is fine.", "solution": ["# helper.py", "def greet(name):", "    return f\"Hello, {name}!\"", "", "# main.py", "import helper", "print(helper.greet(\"Mila\"))"]},
        ],
    },
    {
        "slug": "chapter-10-classes-and-objects",
        "title": "Classes and Objects",
        "emoji": "🏗️",
        "about": "Classes are blueprints. Objects are created from classes.",
        "goals": ["Create classes", "Use __init__", "Add methods", "Model real things"],
        "tips": ["self means this object", "Methods are functions inside class", "Objects group data and behavior"],
        "demo_code": [
            ["class Robot:", "    def __init__(self, name):", "        self.name = name", "    def say_hi(self):", "        print(\"Hi, I am\", self.name)", "", "r1 = Robot(\"Bolt\")", "r1.say_hi()"],
            ["class Player:", "    def __init__(self, name):", "        self.name = name", "        self.points = 0", "    def add_points(self, value):", "        self.points += value", "", "p = Player(\"Mila\")", "p.add_points(5)", "print(p.points)"]
        ],
        "exercises": [
            {"name": "Pet class", "task": "Create Pet class with name and kind.", "hint": "Use __init__.", "solution": ["class Pet:", "    def __init__(self, name, kind):", "        self.name = name", "        self.kind = kind", "", "p = Pet(\"Luna\", \"cat\")", "print(p.name, p.kind)"]},
            {"name": "Pet speak", "task": "Add speak() method to Pet class.", "hint": "Use self.name in print.", "solution": ["class Pet:", "    def __init__(self, name):", "        self.name = name", "    def speak(self):", "        print(self.name, \"says hello!\")", "", "p = Pet(\"Luna\")", "p.speak()"]},
            {"name": "Counter class", "task": "Create Counter with value=0 and inc().", "hint": "Increase value by 1.", "solution": ["class Counter:", "    def __init__(self):", "        self.value = 0", "    def inc(self):", "        self.value += 1", "", "c = Counter()", "c.inc()", "print(c.value)"]},
            {"name": "Student pass", "task": "Create Student class with passed() method.", "hint": "Return score >= 60.", "solution": ["class Student:", "    def __init__(self, name, score):", "        self.name = name", "        self.score = score", "    def passed(self):", "        return self.score >= 60", "", "s = Student(\"Mila\", 75)", "print(s.passed())"]},
        ],
    },
    {
        "slug": "chapter-11-turtle-graphics",
        "title": "Turtle Graphics",
        "emoji": "🐢",
        "about": "Turtle draws graphics with simple movement commands.",
        "goals": ["Use turtle module", "Move and turn", "Draw shapes", "Use loops for patterns"],
        "tips": ["forward() moves turtle", "left()/right() turns turtle", "Use loops to repeat sides"],
        "demo_code": [
            ["import turtle", "t = turtle.Turtle()", "for _ in range(4):", "    t.forward(100)", "    t.right(90)", "turtle.done()"],
            ["import turtle", "t = turtle.Turtle()", "t.pencolor(\"blue\")", "t.forward(120)", "turtle.done()"],
        ],
        "exercises": [
            {"name": "Triangle", "task": "Draw a triangle using turtle.", "hint": "Use 3 turns of 120 degrees.", "solution": ["import turtle", "t = turtle.Turtle()", "for _ in range(3):", "    t.forward(100)", "    t.left(120)", "turtle.done()"]},
            {"name": "Hexagon", "task": "Draw a hexagon.", "hint": "Use 6 turns of 60 degrees.", "solution": ["import turtle", "t = turtle.Turtle()", "for _ in range(6):", "    t.forward(80)", "    t.right(60)", "turtle.done()"]},
            {"name": "Color line", "task": "Draw thick red line.", "hint": "Use pencolor and pensize.", "solution": ["import turtle", "t = turtle.Turtle()", "t.pencolor(\"red\")", "t.pensize(4)", "t.forward(150)", "turtle.done()"]},
            {"name": "Star", "task": "Draw a star shape.", "hint": "Use 5 turns of 144 degrees.", "solution": ["import turtle", "t = turtle.Turtle()", "for _ in range(5):", "    t.forward(150)", "    t.right(144)", "turtle.done()"]},
        ],
    },
    {
        "slug": "chapter-12-mini-projects",
        "title": "Mini Projects",
        "emoji": "🎮",
        "about": "Mini projects combine your skills into complete little programs.",
        "goals": ["Plan a project", "Build step by step", "Test features", "Improve user experience"],
        "tips": ["Start simple", "Add one feature at a time", "Test after each change"],
        "demo_code": [
            ["import random", "secret = random.randint(1, 10)", "guess = int(input(\"Guess 1-10: \\"))", "if guess == secret:", "    print(\"You win!\")", "else:", "    print(\"Secret was\", secret)"],
            ["score = 0", "if input(\"2 + 2 = \" ) == \"4\":", "    score += 1", "print(\"Score:\", score)"]
        ],
        "exercises": [
            {"name": "3-question quiz", "task": "Ask 3 questions and count correct answers.", "hint": "Use score variable.", "solution": ["score = 0", "if input(\"Sky color on clear day? \" ).lower() == \"blue\":", "    score += 1", "if input(\"5 + 5 = \" ) == \"10\":", "    score += 1", "if input(\"Python is fun? \" ).lower() == \"yes\":", "    score += 1", "print(\"Final score:\", score)"]},
            {"name": "Rock paper scissors", "task": "Make a text rock-paper-scissors game.", "hint": "Use random.choice.", "solution": ["import random", "options = [\"rock\", \"paper\", \"scissors\"]", "computer = random.choice(options)", "player = input(\"rock/paper/scissors: \" ).lower()", "print(\"Computer:\", computer)", "if player == computer:", "    print(\"Draw\")", "elif (player == \"rock\" and computer == \"scissors\") or (player == \"paper\" and computer == \"rock\") or (player == \"scissors\" and computer == \"paper\"):", "    print(\"You win\")", "else:", "    print(\"You lose\")"]},
            {"name": "Best score", "task": "Store scores in list and print highest.", "hint": "Use max(list).", "solution": ["scores = [10, 18, 7, 21]", "print(\"Best score:\", max(scores))"]},
            {"name": "Project steps", "task": "Print 3 steps for your own project.", "hint": "Use list + loop.", "solution": ["steps = [\"Idea\", \"Build first version\", \"Test and improve\"]", "for step in steps:", "    print(step)"]},
        ],
    },
]


def build_notebook(chapter, mode):
    cells = []
    if mode == "exercises":
        cells.append({
            "cell_type": "markdown",
            "metadata": {"language": "markdown"},
            "source": [f"# {chapter['title']} {chapter['emoji']}", "", "Learn by doing. Run the examples, then complete all exercises."],
        })
        for i, block in enumerate(chapter["demo_code"], start=1):
            cells.append({"cell_type": "markdown", "metadata": {"language": "markdown"}, "source": [f"## Example {i}"]})
            cells.append({"cell_type": "code", "execution_count": None, "metadata": {"language": "python"}, "outputs": [], "source": block})

        for i, ex in enumerate(chapter["exercises"], start=1):
            cells.append({
                "cell_type": "markdown",
                "metadata": {"language": "markdown"},
                "source": [f"## Exercise {i} - {ex['name']}", f"TODO: {ex['task']}", "", f"Hint: {ex['hint']}"]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {"language": "python"},
                "outputs": [],
                "source": ["# TODO"] + ex["solution"],
            })

        cells.append({
            "cell_type": "markdown",
            "metadata": {"language": "markdown"},
            "source": ["## Try It Yourself ⭐", "1. Change one example and see what happens.", "2. Add one extra feature.", "3. Share your result with a teacher or friend."],
        })
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {"language": "python"},
            "outputs": [],
            "source": ["# Your playground", "print(\"Experiment here!\")"],
        })

    else:
        cells.append({
            "cell_type": "markdown",
            "metadata": {"language": "markdown"},
            "source": [f"# {chapter['title']} - Solutions ✅", "", "Solved versions of all chapter exercises with short explanations."],
        })

        for i, ex in enumerate(chapter["exercises"], start=1):
            cells.append({
                "cell_type": "markdown",
                "metadata": {"language": "markdown"},
                "source": [f"## Exercise {i} - {ex['name']}", f"Solution idea: {ex['task']}"]
            })
            cells.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {"language": "python"},
                "outputs": [],
                "source": ex["solution"],
            })

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.14"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_chapter(chapter):
    chapter_dir = CONTENT / chapter["slug"]
    chapter_dir.mkdir(parents=True, exist_ok=True)

    theory_lines = [
        f"# {chapter['title']}",
        "",
        "Welcome to the next step of your Python journey.",
        "",
        "## What is this chapter about?",
        "",
        chapter["about"],
        "",
        "## What you learn in this chapter",
        "",
    ]
    theory_lines.extend([f"- {goal}" for goal in chapter["goals"]])
    theory_lines.extend([
        "",
        "## Key idea",
        "",
        f"{chapter['title']} helps you write stronger and smarter programs.",
        "",
        "## Quick tips",
        "",
    ])
    theory_lines.extend([f"- {tip}" for tip in chapter["tips"]])
    theory_lines.extend(["", "Next: Open exercises.ipynb and complete each TODO block."])

    (chapter_dir / "theory.md").write_text("\n".join(theory_lines) + "\n", encoding="utf-8")
    (chapter_dir / "exercises.ipynb").write_text(json.dumps(build_notebook(chapter, "exercises"), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (chapter_dir / "solutions.ipynb").write_text(json.dumps(build_notebook(chapter, "solutions"), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_manifest():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    existing = {entry["slug"] for entry in data["chapters"]}

    new_entries = [
        {
            "slug": chapter["slug"],
            "title": chapter["title"].replace("Chapter ", "").split(" - ", 1)[1],
            "practice_files": ["theory.md", "exercises.ipynb"],
            "solution_files": ["solutions.ipynb"],
        }
        for chapter in CHAPTERS
        if chapter["slug"] not in existing
    ]

    if not new_entries:
        return

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
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


for chapter in CHAPTERS:
    write_chapter(chapter)

update_manifest()
print(f"Created or updated {len(CHAPTERS)} chapters and synced manifest.")
