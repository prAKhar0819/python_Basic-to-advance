
# Day 5 - Comments, Escape Sequence & Print in Python

Welcome to **Day 5 of 100DaysOfCode**. Today we will learn about:

- Single-line and multi-line comments
- Escape sequences in strings
- More customization options for the `print()` statement

---

## 📝 Comments in Python

A **comment** is used to describe code and is ignored during execution.

### ➤ Single-Line Comments

Use `#` at the beginning of a line.

```python
# This is a single-line comment
print("This is a print statement.")  # Printing message
```

**Output:**
```
This is a print statement.
```

You can also comment out code:
```python
print("Python Program")
# print("This won't run")
```

**Output:**
```
Python Program
```

---

### ➤ Multi-Line Comments

Use multiple `#` symbols or triple quotes `''' '''` or `""" """`.

```python
# This is line 1 of a multi-line comment
# This is line 2

"""
This is another way to write
a multi-line comment using triple quotes
"""
```

---

## 🔠 Escape Sequence Characters

Escape sequences begin with a backslash `\` to allow special characters in strings.

### Examples:

```python
print("This doesn't \"break\" the string")
print("Line1\nLine2")     # New line
print("Tab\tSpace")       # Tab space
```

**Output:**
```
This doesn't "break" the string
Line1
Line2
Tab     Space
```

---

## 🖨️ More on `print()` in Python

The syntax for `print()` is:
```python
print(object(s), sep='separator', end='end', file=file, flush=flush)
```

### ➤ Parameters:

- `object(s)`: One or more objects to be printed.
- `sep`: Separator between objects (default `' '`).
- `end`: What to print at the end (default `\n`).
- `file`: Output stream (default `sys.stdout`).
- `flush`: Whether to forcibly flush the stream.

### ➤ Examples:

```python
print("Hello", "World", sep="-")
print("Hello", end="!!!")
```

**Output:**
```
Hello-World
Hello!!!
```

---

## ✅ Summary

- Use `#` or `""" """` for comments.
- Escape sequences allow special characters in strings.
- The `print()` function is powerful and customizable.

---

🧠 **Try It Yourself!**
Practice by adding your own comments, escape sequences, and using different `print()` parameters.

---

🚀 [Next → Day 6: Variables and Data Types](#)