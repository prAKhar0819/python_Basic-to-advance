# Day 3 - Modules and pip in Python

## What is a Module?

A **module** is like a code library that we can borrow and use in our Python programs. There are two types of modules in Python:

### 1. Built-in Modules
These modules come pre-installed with the Python interpreter.  
You can import and use them directly without any extra installation.

### 2. External Modules
These modules are created by third parties and need to be installed before use.  
You can install them using package managers like `pip` or `conda`.  
Over time, different versions of the same module may become available.

---

## The `pip` Command

`pip` is a package manager used to install Python modules.  
For example, to install the module `pandas`, run:

```bash
pip install pandas
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')

print(df)  # This will display the first few rows from the 'words.csv' file

```

If you want, I can also generate a nicely styled PDF or convert it to HTML for you!
