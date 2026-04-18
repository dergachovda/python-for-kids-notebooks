# Chapter 2 - Variables and Input

Great job finishing Chapter 1.
Now you will store information and ask the user for data.

## What is a variable?

A variable is a labeled box for data.
You can put text or numbers in it and use it later.

```python
name = "Mila"
age = 10
print(name)
print(age)
```

## What you learn in this chapter

- Creating variables
- Naming rules for variables
- Basic data types: `str` and `int`
- Using `input()` to ask questions
- Combining values in simple programs

## Naming rules

- Use letters, numbers, and underscores
- Do not start with a number
- Use clear names like `user_name` instead of `x`

## Basic types

- `str` — text: `"hello"`, `'world'`
- `int` — whole numbers: `10`, `42`

You can check the type with `type()`:

```python
print(type("hello"))  # <class 'str'>
print(type(42))       # <class 'int'>
```

## input()

`input()` asks the user to type something. It always gives back text (`str`):

```python
user_name = input("What is your name? ")
print("Nice to meet you,", user_name)
```

To get a number from the user, convert the text with `int()`:

```python
age = int(input("How old are you? "))
```

> **Note:** If the user types letters instead of digits, `int()` will cause
> an error. For now, just type numbers when asked. You will learn how to
> handle errors in Chapter 8.

## String concatenation

You can join strings together with `+`:

```python
first = "Alex"
last = "Brown"
full_name = first + " " + last
print(full_name)   # Alex Brown
```

## Key idea

Variables help your programs remember things.

## Quick tips

- Give variables clear names so your code is easy to read.
- `input()` always returns text — use `int()` if you need a number.
- Use `+` to join strings together.

Next: Open `exercises.ipynb` and complete all TODO sections.
