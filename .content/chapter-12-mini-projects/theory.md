# Mini Projects

Welcome to the next step of your Python journey.

## What is this chapter about?

Mini projects combine everything you have learned into complete little programs.
This is where you put your skills together!

## What you learn in this chapter

- Plan a tiny project before coding
- Build step by step
- Test each feature
- Improve the user experience

## Key idea

Mini Projects help you write stronger and smarter programs.

## Examples

### Example 1

```python
import random
secret = random.randint(1, 10)
guess = int(input("Guess 1-10: "))
if guess == secret:
    print("You win!")
else:
    print("Secret was", secret)
```

### Example 2

```python
score = 0
if input("2 + 2 = ") == "4":
    score += 1
print("Score:", score)
```

## Quick tips

- Start with the simplest version first.
- Add one feature at a time.
- Test after every change.
- Ask a friend to try your program!

Next: Open `exercises.ipynb` and complete each TODO block.
