# Dictionaries and Tuples

Welcome to the next step of your Python journey.

## What is this chapter about?

Dictionaries store data as key-value pairs — like a real dictionary where each word has a meaning.
Tuples are like lists that cannot be changed after creation.

## What you learn in this chapter

- Create a dictionary with curly braces
- Read and update values by key
- Create tuples with parentheses
- Loop through dictionary keys

## Key idea

Dictionaries and Tuples help you write stronger and smarter programs.

## Examples

### Example 1

```python
student = {"name": "Mila", "age": 11}
print(student["name"])
student["age"] = 12
print(student)
```

### Example 2

```python
point = (4, 7)
print("x:", point[0])
print("y:", point[1])
```

## Quick tips

- Dictionary keys must be unique.
- Use dict["key"] to read or set a value.
- Tuples use parentheses: (1, 2, 3).
- You cannot change a tuple after creating it.

Next: Open `exercises.ipynb` and complete each TODO block.
