# Lists

Welcome to the next step of your Python journey.

## What is this chapter about?

Lists store many values in one variable.
You can add, remove, and loop through the items.

## What you learn in this chapter

- Create a list with square brackets
- Read items by index (starting at 0)
- Add and remove items
- Loop through a list with for

## Key idea

Lists help you write stronger and smarter programs.

## Examples

### Example 1

```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])
fruits.append("orange")
print(fruits)
```

### Example 2

```python
pets = ["dog", "cat", "fish"]
for pet in pets:
    print("I like", pet)
```

## Quick tips

- The first item has index 0, not 1.
- append() adds an item to the end.
- remove() deletes the first matching item.
- len(my_list) tells you how many items there are.

Next: Open `exercises.ipynb` and complete each TODO block.
