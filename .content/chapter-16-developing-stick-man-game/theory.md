# Chapter 16 - Developing the Mr. Stick Man Game

Now you build level mechanics for a platform game.

## What you learn in this chapter

- `Platform` class design
- Collision checks with platforms
- Canvas coordinate system basics
- Level layout with object lists

## Platform class

A platform can be represented by a canvas rectangle or sprite with bounds.

```python
class Platform:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill="green")
```

## Collision with platforms

Use bounds (`x1, y1, x2, y2`) to decide if the character lands on top.

Common rule:
- character is moving down
- character bottom crosses platform top
- x ranges overlap

## Coordinate system

`tkinter` canvas starts at top-left:

- x increases to the right
- y increases downward

## Key idea

Solid platform logic makes movement feel fair and predictable.

## Quick tips

- Separate horizontal and vertical collision handling.
- Use small velocity steps to reduce overlap bugs.
- Test character near platform edges.

Next: Open `exercises.ipynb` and create a simple level with platforms.
