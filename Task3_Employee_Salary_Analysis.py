# Task 3: Employee Salary Analysis
# Description:
# A simple Python program to store employee names and their salaries,
# calculate the average salary, identify the highest-paid employee,
# and display who earns above the average salary.

# Step 1: Store employee names and salaries using a dictionary
employees = {
    "Rahul": 55000,
    "Priya": 75000,
    "Amit": 48000,
    "Sneha": 62000,
    "Vikram": 50000
}

# Step 2: Display all employee names and their salaries
print("=== Employee Salary Details ===")
for name, salary in employees.items():
    print(f"{name}: ₹{salary:,}")  # comma formatting for readability

# Step 3: Calculate the average salary
total_salary = sum(employees.values())
average_salary = total_salary / len(employees)

print("\nAverage Salary: ₹{:.2f}".format(average_salary))

# Step 4: Find the highest-paid employee
highest_paid = max(employees, key=employees.get)
print(f"Highest Paid Employee: {highest_paid} (₹{employees[highest_paid]:,})")

# Step 5: Find employees earning above average
above_average = [name for name, salary in employees.items() if salary > average_salary]

print("\nEmployees earning above average salary:")
if above_average:
    for emp in above_average:
        print(f"- {emp}")
else:
    print("No employees earn above average.")
