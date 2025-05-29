# What are Strings?

In Python, anything that you enclose between single or double quotation marks is considered a **string**. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

## Example

```python
name = "Harry"
print("Hello, " + name)
```

**Output:**
```
Hello, Harry
```

> **Note:** It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks within the string.  
For example, consider the sentence:  
**He said, “I want to eat an apple”.**

To print this statement in Python:

```python
print('He said, "I want to eat an apple".')
```

---

## Multiline Strings

If our string spans multiple lines, we can create them using triple quotes:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

---

## Accessing Characters of a String

In Python, a string is like an array of characters.  
We can access parts of the string using its index (starting from 0).  
Square brackets `[]` are used to access elements of the string.

```python
print(name[0])
print(name[1])
```

---

## Looping Through the String

We can loop through strings using a `for` loop like this:

```python
for character in name:
    print(character)
```

This code prints all the characters in the string `name`, one by one!

---

[Next Lesson >>](https://replit.com/@codewithharry/12-Day12-Strings-Slicing#.tutorial/Tutorial.md)