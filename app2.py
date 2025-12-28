import streamlit as st
import numpy as np
import pandas as pd

# Data
students = ["chandan", "pankaj", "aman", "kundan", "rahul"]

marks = np.array([
    [85, 78, 90],
    [70, 65, 72],
    [88, 92, 95],
    [60, 98, 62],
    [75, 80, 78]
])

# DataFrame
df = pd.DataFrame(marks, columns=["Math", "Science", "English"])
df["Student"] = students
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 60 else "Fail")

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("📊 Student Marks Analyzer App")
st.write("Analyze student performance, results, and class statistics.")

# Show data table
st.subheader("📄 Student Marks Data")
st.dataframe(df)

# Class Statistics
st.subheader("📌 Class Statistics")
st.write("*Highest Average:* ", df["Average"].max())
st.write("*Lowest Average:* ", df["Average"].min())
st.write("*Class Average:* ", round(df["Average"].mean(), 2))

# Result Summary
st.subheader("🎯 Result Summary")
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()
st.write(f"✅ Pass: {pass_count}")
st.write(f"❌ Fail: {fail_count}")

# Visualization (Optional)
st.subheader("📈 Marks Comparison Chart")
st.bar_chart(df.set_index("Student")[["Math", "Science", "English"]])
