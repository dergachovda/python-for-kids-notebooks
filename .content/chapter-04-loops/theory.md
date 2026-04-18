# Loops

Welcome to the next step of your Python journey.

## What is this chapter about?

Loops repeat code so you don't have to type the same thing over and over.
Python has two main loops: for and while.

## What you learn in this chapter

- Use for loops with range()
- Use while loops
- Control loops with break
- Understand range(start, stop, step)

## Key idea

Loops help you write stronger and smarter programs.

## Examples

### Example 1

```python
for n in range(1, 6):
    print(n)
```

### Example 2

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
```

## Quick tips

- range(1, 6) gives the numbers 1, 2, 3, 4, 5.
- A while loop keeps running while the condition is True.
- break exits the loop immediately.
- Indent the code inside the loop with 4 spaces.

Next: Open `exercises.ipynb` and complete each TODO block.
