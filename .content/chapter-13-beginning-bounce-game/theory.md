# Chapter 13 - Beginning Your First Game: Bounce!

In this chapter, you start a simple paddle-and-ball game using `tkinter`.

## What you learn in this chapter

- How a game loop works
- How to create a `Ball` class
- How to create a `Paddle` class
- How keyboard controls connect to game objects

## Game loop idea

A game updates many times per second.
Each update step usually does three things:

1. Read input
2. Update positions
3. Draw the new frame

In `tkinter`, this can be done with a repeated `after()` call.

## Ball class

A `Ball` object stores position and speed.
It moves every frame.

```python
self.x += self.dx
self.y += self.dy
```

The ball should bounce on top and side walls by reversing direction.

## Paddle class

A `Paddle` object moves left and right.
Keyboard events can change its speed.

```python
def move_left(self, event=None):
    self.dx = -6
```

## Key idea

Classes help organize game behavior.
Each object controls its own state and movement.

## Quick tips

- Keep movement values small at first.
- Test one feature at a time.
- Print debug info if something moves incorrectly.

Next: Open `exercises.ipynb` and build your first playable Bounce prototype.
