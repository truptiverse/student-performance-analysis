import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/student_performance.csv")

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

# Average scores
print("\nAverage Scores:")
print(df[["math_score", "science_score", "english_score"]].mean())

# Average study hours
print("\nAverage Study Hours:")
print(df["study_hours"].mean())

# Average attendance
print("\nAverage Attendance:")
print(df["attendance"].mean())

# Find the top-performing students
df["average_score"] = df[
    ["math_score", "science_score", "english_score"]
].mean(axis=1)

top_students = df.sort_values(
    "average_score", ascending=False
).head(5)

print("\nTop 5 Students:")
print(top_students[
    ["student_id", "average_score"]
])

# Study hours vs average score
plt.scatter(df["study_hours"], df["average_score"])
plt.xlabel("Study Hours")
plt.ylabel("Average Score")
plt.title("Study Hours vs Average Score")
plt.show()
