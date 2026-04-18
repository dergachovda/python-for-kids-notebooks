# Chapter 15 - Creating Graphics for the Mr. Stick Man Game

In this chapter, you prepare visual assets for the platform game.

## What you learn in this chapter

- What sprites are
- How to organize image assets
- How to load GIF images with `PhotoImage`
- How to place images on a `Canvas`

## Sprites

A sprite is a small image used for a game object.
Examples: player, platform, door, background.

## Asset organization

Use a clean folder such as `assets/images/`.
Name files clearly, for example:

- `stickman_idle.gif`
- `platform.gif`
- `door.gif`

## Loading images in tkinter

```python
player_img = tkinter.PhotoImage(file="assets/images/stickman_idle.gif")
canvas.create_image(100, 200, image=player_img, anchor="nw")
```

Keep a reference to each image object so it is not removed by Python.

## Key idea

Good asset naming and loading rules make game code easier to maintain.

## Quick tips

- Start with tiny images.
- Use consistent transparent backgrounds.
- Keep image sizes aligned to your game scale.

Next: Open `exercises.ipynb` and load your first sprite set into a canvas.
