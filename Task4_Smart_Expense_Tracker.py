# Smart Expense Tracker Application
# ---------------------------------
# This program allows users to add, view, and analyze daily expenses.
# It uses file handling to store data persistently in a text file.

import os

# Define the filename to store expenses
FILENAME = "expenses.txt"


# Function to add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel, etc.): ")
    amount = float(input("Enter amount (₹): "))

    # Open the file in append mode to add new entries
    with open(FILENAME, "a") as file:
        file.write(f"{date},{category},{amount}\n")

    print("✅ Expense added successfully!\n")


# Function to read all expenses from file
def read_expenses():
    expenses = []
    # Check if the file exists
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 3:
                    date, category, amount = data
                    expenses.append({
                        "date": date,
                        "category": category,
                        "amount": float(amount)
                    })
    return expenses


# Function to view all expenses
def view_all_expenses():
    expenses = read_expenses()
    if not expenses:
        print("⚠️ No expenses recorded yet.\n")
        return

    print("\n===== Expenses Recorded =====")
    for exp in expenses:
        print(f"Date: {exp['date']} | Category: {exp['category']} | Amount: ₹{exp['amount']}")
    print("==============================\n")


# Function to calculate total expense
def view_total_expense():
    expenses = read_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expense: ₹{total}\n")


# Function to view category-wise expense summary
def view_category_summary():
    expenses = read_expenses()
    summary = {}
    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n📊 Category Summary:")
    print(summary)
    print()


# Main menu loop
def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expense")
        print("4. View Category Summary")
        print("5. Exit")
        print("===========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_total_expense()
        elif choice == "4":
            view_category_summary()
        elif choice == "5":
            print("👋 Exiting... Thank you for using Expense Tracker!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")


# Run the program
if __name__ == "__main__":
    main()
