# Chapter 17 - Creating Mr. Stick Man

In this chapter, you build the player character and controls.

## What you learn in this chapter

- `StickFigure` class structure
- Keyboard control bindings
- Jump mechanics
- Simple animation frame switching

## Character class

The character stores position, velocity, and animation state.

```python
self.vx = 0
self.vy = 0
self.on_ground = False
```

## Keyboard controls

Bind keys to movement methods:

- Left arrow: move left
- Right arrow: move right
- Space: jump

## Jump behavior

A jump usually sets an upward velocity once.
Gravity then pulls the character down each frame.

```python
if self.on_ground:
    self.vy = -12
```

## Animation

Switch sprite frames based on state:

- idle
- running
- jumping

## Key idea

Player control should feel responsive and consistent.

## Quick tips

- Prevent double-jump unless intended.
- Tune gravity and jump speed together.
- Keep animation code separate from physics logic.

Next: Open `exercises.ipynb` and implement movement, jump, and basic animation.
