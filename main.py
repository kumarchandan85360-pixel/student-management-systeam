import numpy as np
import pandas as pd

students = ["chandan", "pankaj", "aman", "kundan", "rahul"]

marks = np.array([
    [85, 78, 90],
    [70, 65, 72],
    [88, 92, 95],
    [60, 98, 62],
    [75, 80, 78]
])

df = pd.DataFrame(marks, columns=["Math", "Science", "English"])
df["Student"] = students

df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 60 else "Fail")

print("\nStudent Marks Analysis\n")
print(df)

print("\nClass Statistics:")
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())
print("Class Average:", df["Average"].mean())

