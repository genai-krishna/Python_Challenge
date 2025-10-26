# Employee Performance & Bonus Management System
# -----------------------------------------------
# This program reads employee performance data, calculates total performance score,
# assigns a bonus grade, sorts employees by performance, and displays a report.
# Concepts used: file handling, functions, sorting, exception handling, loops.

# File name to store employee data
EMP_FILE = "employees.txt"

# Function to add employee data into the file
def add_employee():
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    try:
        sales = float(input("Enter Monthly Sales/Output: "))
        projects = int(input("Enter No. of Projects Completed: "))
        rating = float(input("Enter Performance Rating (out of 5): "))
    except ValueError:
        print("⚠️ Invalid input! Please enter numbers correctly.\n")
        return

    # Write data to file (append mode)
    with open(EMP_FILE, "a") as file:
        file.write(f"{name}|{dept}|{sales}|{projects}|{rating}\n")
    print("✅ Employee record added successfully!\n")

# Function to calculate performance score
def calculate_score(sales, projects, rating):
    # Basic formula for total performance score
    score = (sales * 0.5) + (projects * 2000) + (rating * 10000)
    return score

# Function to determine bonus grade
def assign_bonus(score):
    if score >= 100000:
        return "A"
    elif score >= 85000:
        return "B"
    else:
        return "C"

# Function to generate and display report
def generate_report():
    try:
        with open(EMP_FILE, "r") as file:
            lines = file.readlines()
        if not lines:
            print("No employee records found.\n")
            return
    except FileNotFoundError:
        print("No data file found. Please add employee records first.\n")
        return

    employees = []

    # Process each record
    for line in lines:
        name, dept, sales, projects, rating = line.strip().split("|")
        sales = float(sales)
        projects = int(projects)
        rating = float(rating)
        score = calculate_score(sales, projects, rating)
        grade = assign_bonus(score)
        employees.append({
            "name": name,
            "dept": dept,
            "score": score,
            "grade": grade
        })

    # Sort employees by score (descending order)
    employees.sort(key=lambda x: x["score"], reverse=True)

    # Display formatted report
    print("\n===== Employee Performance & Bonus Management System =====\n")
    print("Name     | Department  | Score           | Bonus Grade")
    print("-------------------------------------------------------")
    for emp in employees:
        print(f"{emp['name']:<10} | {emp['dept']:<12} | {emp['score']:<15.1f} | {emp['grade']}")

    # Display top performer
    top = employees[0]
    print(f"\n🏆 Top Performer: {top['name']} — Score {top['score']:.1f} (Bonus Grade: {top['grade']})\n")

# Main program loop
def main():
    while True:
        print("===== Employee Performance Menu =====")
        print("1. Add Employee Record")
        print("2. Generate Performance Report")
        print("3. Exit")
        print("=====================================")
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            add_employee()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
if __name__ == "__main__":
    main()
