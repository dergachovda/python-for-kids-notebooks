# Classes and Objects

Welcome to the next step of your Python journey.

## What is this chapter about?

A class is a blueprint for creating objects.
Objects bundle data (attributes) and actions (methods) together.

## What you learn in this chapter

- Create a class with class
- Use __init__ to set up attributes
- Add methods that use self
- Model real-world things as objects

## Key idea

Classes and Objects help you write stronger and smarter programs.

## Examples

### Example 1

```python
class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am", self.name)

r1 = Robot("Bolt")
r1.say_hi()
```

### Example 2

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, value):
        self.points += value

p = Player("Mila")
p.add_points(5)
print(p.points)
```

## Quick tips

- self refers to the current object.
- Methods are just functions defined inside a class.
- __init__ runs automatically when you create an object.
- Use dot notation: object.attribute or object.method().

Next: Open `exercises.ipynb` and complete each TODO block.
