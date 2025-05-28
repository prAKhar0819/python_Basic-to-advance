import pandas
import hashlib
import os

print("Hi")

csv_file = "/home/prakhar/python-learning/python_Basic-to-advance/Day_3/one.csv"

if os.path.isfile(csv_file):
    df = pandas.read_csv(csv_file)
    print(df)
else:
    print(f"File '{csv_file}' not found. Please add the file in the working directory.")

m = hashlib.sha256()
