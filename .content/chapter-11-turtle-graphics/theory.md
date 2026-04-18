# Turtle Graphics

Welcome to the next step of your Python journey.

## What is this chapter about?

Turtle draws pictures using simple movement commands.
You tell the turtle to move forward, turn, and change colors — and it draws on the screen.

## What you learn in this chapter

- Import and use the turtle module
- Move and turn the turtle
- Draw shapes with loops
- Change pen color and size

## Key idea

Turtle Graphics help you write stronger and smarter programs.

## Examples

### Example 1

```python
import turtle
t = turtle.Turtle()
for _ in range(4):
    t.forward(100)
    t.right(90)
turtle.done()
```

### Example 2

```python
import turtle
t = turtle.Turtle()
t.pencolor("blue")
t.forward(120)
turtle.done()
```

> **Important:** Turtle graphics open a separate window and do not work inside Jupyter notebooks. Save your code as a .py file and run it with `python filename.py`, or use IDLE.

## Quick tips

- forward(n) moves the turtle n pixels.
- left(d) and right(d) turn by d degrees.
- Use a for loop to draw shapes with equal sides.
- pencolor() and pensize() change the pen style.

Next: Open `exercises.ipynb` and complete each TODO block.
