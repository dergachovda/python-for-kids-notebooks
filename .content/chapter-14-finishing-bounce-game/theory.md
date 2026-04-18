# Chapter 14 - Finishing Your First Game: Bounce!

Now you improve the game so it feels complete.

## What you learn in this chapter

- Collision detection with paddle
- Keeping score
- Defining game over rules
- Displaying messages on the screen

## Collision detection

A common approach is checking object bounds.
In `tkinter`, `canvas.coords(item)` gives box coordinates.

If ball and paddle boxes overlap, bounce the ball upward.

## Score system

Start with score `0` and add points when the paddle hits the ball.

```python
score += 1
```

Then update score text on the canvas.

## Game over

When the ball reaches the bottom edge, stop movement and show a message.

```python
if ball_y2 >= canvas_height:
    game_over = True
```

## Key idea

A complete game needs rules: win, lose, and feedback.

## Quick tips

- Update score text only when score changes.
- Keep game states clear with flags like `game_over`.
- Test edge cases near corners.

Next: Open `exercises.ipynb` and finish Bounce with score and game over.
