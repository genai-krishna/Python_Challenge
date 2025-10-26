import datetime

# File name to store tasks
TASK_FILE = "tasks.txt"

# Function to add a new task
def add_task():
    task = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    # Save task and due date to the file
    with open(TASK_FILE, "a") as file:
        file.write(f"{task}|{due_date}\n")
    print("✅ Task added successfully!\n")

# Function to view all tasks
def view_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks found.\n")
            return
        print("\nAll Tasks:")
        for index, line in enumerate(tasks, start=1):
            task, due = line.strip().split("|")
            print(f"{index}. {task} (Due: {due})")
        print()
    except FileNotFoundError:
        print("No task file found. Add a task first.\n")

# Function to remove a task
def remove_task():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks to remove.\n")
            return
        
        view_tasks()
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            with open(TASK_FILE, "w") as file:
                file.writelines(tasks)
            print(f"🗑️ Removed: {removed_task.split('|')[0]}\n")
        else:
            print("Invalid task number.\n")
    except FileNotFoundError:
        print("No task file found. Add a task first.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to check due or overdue tasks
def check_due_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
        if not tasks:
            print("No tasks found.\n")
            return
        
        today = datetime.date.today()
        print("\nTasks due today or overdue:")
        found = False
        for line in tasks:
            task, due = line.strip().split("|")
            due_date = datetime.datetime.strptime(due, "%Y-%m-%d").date()
            if due_date <= today:
                print(f"- {task} (Due: {due})")
                found = True
        if not found:
            print("No tasks are due today or overdue.\n")
        print()
    except FileNotFoundError:
        print("No task file found. Add a task first.\n")

# Main program loop
def main():
    while True:
        print("===== To-Do Reminder App =====")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Check Due Tasks")
        print("5. Exit")
        print("==============================")
        
        choice = input("Enter your choice: ")
        print()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            check_due_tasks()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
