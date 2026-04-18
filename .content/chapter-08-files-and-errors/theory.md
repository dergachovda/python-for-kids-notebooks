# Files and Errors

Welcome to the next step of your Python journey.

## What is this chapter about?

Files let you save data so it survives after the program stops.
Error handling keeps your program from crashing when something unexpected happens.

## What you learn in this chapter

- Write text to a file
- Read text from a file
- Append data to a file
- Handle errors with try / except

## Key idea

Files and Errors help you write stronger and smarter programs.

## Examples

### Example 1

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("I love Python\n")
with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

### Example 2

```python
try:
    value = int(input("Enter number: "))
    print(value)
except ValueError:
    print("Not a number")
```

## Quick tips

- Use with open(...) as f: to work with files safely.
- Always set encoding="utf-8" when opening files.
- Mode 'w' writes (overwrites), 'r' reads, 'a' appends.
- Wrap risky code in try / except to catch errors.

Next: Open `exercises.ipynb` and complete each TODO block.
