# Chapter 18 - Completing the Mr. Stick Man Game

This chapter adds the final goal and game polish.

## What you learn in this chapter

- Creating an exit or door target
- Detecting win conditions
- Showing victory messages
- Small polish improvements

## Exit object

Create a door sprite and place it at the end of the level.

When player bounds overlap door bounds, trigger win.

## Win condition

```python
if intersects(player_box, door_box):
    has_won = True
```

Stop movement updates or switch to a victory state.

## Polish ideas

- Add background color or image
- Display timer or score
- Add a restart key

## Key idea

Finishing touches make your game feel complete and rewarding.

## Quick tips

- Keep win detection simple and clear.
- Make end-state messages easy to read.
- Test from level start to finish without editing variables manually.

Next: Open `exercises.ipynb` and complete the game loop from start to win.
