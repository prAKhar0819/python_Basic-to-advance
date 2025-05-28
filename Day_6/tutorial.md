
# Day 6 - Variables and Data Types

## What is a variable?
A variable is like a container that holds data — very similar to how our kitchen containers hold sugar, salt, etc. Creating a variable is like creating a placeholder in memory and assigning it some value. In Python it's as easy as writing:

```python
a = 1
b = True
c = "Harry"
d = None
```

These are four variables of different data types.

---

## What is a Data Type?
A data type specifies the type of value a variable holds. This is required in programming to perform various operations without causing an error.

In Python, we can print the type of any variable using the `type()` function:

```python
a = 1
print(type(a))

b = "1"
print(type(b))
```

---

## Built-in Data Types in Python

### 1. Numeric Data: `int`, `float`, `complex`
- **int**: `3`, `-8`, `0`
- **float**: `7.349`, `-9.0`, `0.0000001`
- **complex**: `6 + 2i`

---

### 2. Text Data: `str`
- **str**: `"Hello World!!!"`, `"Python Programming"`

---

### 3. Boolean Data
Boolean data consists of values `True` or `False`.

---

### 4. Sequenced Data: `list`, `tuple`

#### `list`
A list is an ordered collection of data with elements separated by commas and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:

```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```

Output:
```
[8, 2.3, [-4, 5], ['apple', 'banana']]
```

#### `tuple`
A tuple is an ordered collection of data with elements separated by commas and enclosed within parentheses. Tuples are immutable and cannot be modified after creation.

Example:

```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```

Output:
```
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

---

### 5. Mapped Data: `dict`

#### `dict`
A dictionary is an unordered collection of data containing key:value pairs. These pairs are enclosed within curly brackets.

Example:

```python
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
```

Output:
```
{'name': 'Sakshi', 'age': 20, 'canVote': True}
```