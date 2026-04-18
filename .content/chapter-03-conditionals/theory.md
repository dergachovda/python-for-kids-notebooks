# Conditionals

Welcome to the next step of your Python journey.

## What is this chapter about?

Conditionals let your program make decisions.
Instead of running every line, your code can choose what to do based on a condition.

## What you learn in this chapter

- Use if / elif / else
- Compare values with == , != , > , < , >= , <=
- Combine conditions with and / or
- Build decision logic

## Key idea

Conditionals help you write stronger and smarter programs.

## Examples

### Example 1

```python
age = 11
if age >= 10:
    print("Welcome to coding club!")
else:
    print("Try next year.")
```

### Example 2

```python
weather = "rain"
if weather == "sun":
    print("Play outside")
elif weather == "rain":
    print("Take an umbrella")
else:
    print("Check the sky again")
```

## Quick tips

- Use == to check if two values are equal.
- Use > , < , >= , <= for number comparisons.
- elif lets you check another condition if the first was False.
- else runs when nothing above matched.

Next: Open `exercises.ipynb` and complete each TODO block.
