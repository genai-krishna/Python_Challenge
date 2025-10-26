import datetime

# =====================================================
# Smart Student Attendance & Performance Tracker
# =====================================================

# Dictionary to store student data
# Format:
# students[roll_no] = {"name": "Aditi", "attendance": [], "marks": []}
students = {}

# --------------------------
# Function: Add new student
# --------------------------
def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("⚠️ Student with this roll number already exists!\n")
        return

    students[roll] = {"name": name, "attendance": [], "marks": []}
    print(f"✅ Student added successfully! ({name}, Roll No: {roll})\n")

# --------------------------
# Function: Mark attendance
# --------------------------
def mark_attendance():
    if not students:
        print("⚠️ No students available. Add students first!\n")
        return

    print("\nMark Attendance (P = Present, A = Absent)")
    for roll, data in students.items():
        status = input(f"{data['name']} ({roll}): ").strip().upper()
        if status not in ["P", "A"]:
            print("⚠️ Invalid input! Marking as Absent by default.")
            status = "A"
        data["attendance"].append(status)
    print("\n✅ Attendance marked successfully!\n")

# --------------------------
# Function: Enter marks
# --------------------------
def enter_marks():
    if not students:
        print("⚠️ No students available. Add students first!\n")
        return

    print("\nEnter marks out of 100:")
    for roll, data in students.items():
        try:
            mark = float(input(f"{data['name']} ({roll}): "))
            if mark < 0 or mark > 100:
                print("⚠️ Invalid mark! Setting to 0.")
                mark = 0
            data["marks"].append(mark)
        except ValueError:
            print("⚠️ Invalid input! Setting mark to 0.")
            data["marks"].append(0)
    print("\n✅ Marks recorded successfully!\n")

# --------------------------
# Function: View attendance report
# --------------------------
def view_attendance_report():
    if not students:
        print("⚠️ No student data available!\n")
        return

    print("\n----------------------------------------------------------")
    print("Name           Roll No   Attendance %   Status")
    print("----------------------------------------------------------")

    for roll, data in students.items():
        total = len(data["attendance"])
        present = data["attendance"].count("P")
        attendance_percent = (present / total * 100) if total > 0 else 0

        if attendance_percent >= 90:
            status = "Excellent"
        elif attendance_percent >= 75:
            status = "Good"
        else:
            status = "Needs Improvement"

        print(f"{data['name']:<14} {roll:<8} {attendance_percent:>6.0f}%         {status}")

    print("----------------------------------------------------------\n")

# --------------------------
# Function: Generate performance summary
# --------------------------
def generate_performance_summary():
    if not students:
        print("⚠️ No student data available!\n")
        return

    file_name = "student_performance_report.txt"
    with open(file_name, "w") as f:
        f.write("----------------------------------------------------------\n")
        f.write("Student Performance Summary\n")
        f.write(f"Date: {datetime.date.today()}\n")
        f.write("----------------------------------------------------------\n")
        f.write("Name          Roll No   Attendance%   Marks   Grade\n")

        total_marks = []
        for roll, data in students.items():
            # Attendance %
            total_att = len(data["attendance"])
            present = data["attendance"].count("P")
            attendance_percent = (present / total_att * 100) if total_att > 0 else 0

            # Average marks
            avg_mark = sum(data["marks"]) / len(data["marks"]) if data["marks"] else 0
            total_marks.append(avg_mark)

            # Grade logic
            if avg_mark >= 85:
                grade = "A"
            elif avg_mark >= 70:
                grade = "B"
            elif avg_mark >= 60:
                grade = "C"
            else:
                grade = "D"

            f.write(f"{data['name']:<13} {roll:<8} {attendance_percent:>6.0f}%         {avg_mark:>5.1f}     {grade}\n")

        # Class average
        class_avg = sum(total_marks) / len(total_marks) if total_marks else 0
        f.write("----------------------------------------------------------\n")
        f.write(f"Class Average: {class_avg:.1f}%\n")
        f.write("----------------------------------------------------------\n")

    print("\nGenerating report...")
    print(f"✅ Performance Summary saved as '{file_name}'\n")

# --------------------------
# Main program loop
# --------------------------
def main():
    while True:
        print("===== Smart Student Attendance & Performance Tracker =====")
        print("1. Add New Student")
        print("2. Mark Attendance")
        print("3. Enter Marks")
        print("4. View Attendance Report")
        print("5. Generate Performance Summary")
        print("6. Exit")
        print("==========================================================")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            enter_marks()
        elif choice == "4":
            view_attendance_report()
        elif choice == "5":
            generate_performance_summary()
        elif choice == "6":
            print("👋 Exiting... Thank you for using the Student Tracker!")
            break
        else:
            print("⚠️ Invalid choice! Please try again.\n")

# Run program
if __name__ == "__main__":
    main()
