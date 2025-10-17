# ================================================
# Task 2: Student Marks Organizer
# ================================================
# Description:
# You are given information about students and their marks
# in different subjects. Using Python data structures (list,
# tuple, set, and dictionary), perform:
#   1. Calculate average marks for each student
#   2. Find unique marks across all subjects
#   3. Find students who scored more than 85 in Math
# ================================================

# Step 1: Create a dictionary with student names and their marks
# Each student's marks are stored in another dictionary
students = {
    "Alice": {"Math": 90, "Science": 85, "English": 88},
    "Bob": {"Math": 80, "Science": 78, "English": 82},
    "Charlie": {"Math": 95, "Science": 92, "English": 88}
}

# Step 2: Calculate average marks for each student
print("Average marks:")
for name, marks in students.items():
    # Get all subject marks as a list
    scores = list(marks.values())
    # Calculate average
    average = sum(scores) / len(scores)
    print(f"{name}: {average:.2f}")
print()  # blank line for spacing

# Step 3: Collect all unique marks from all students using a set
all_marks = set()
for marks in students.values():
    all_marks.update(marks.values())

print(f"Unique marks: {all_marks}\n")

# Step 4: Find students who scored more than 85 in Math
high_math_students = [name for name, marks in students.items() if marks["Math"] > 85]

print(f"Students with more than 85 in Math: {high_math_students}")
