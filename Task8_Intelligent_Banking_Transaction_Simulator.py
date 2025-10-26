import csv
from datetime import datetime

# ======================================
# Intelligent Banking Transaction Simulator
# ======================================

# Dictionary to store all bank accounts in memory
# Format: accounts[account_number] = {"name": "John", "balance": 1000, "transactions": []}
accounts = {}

# Function to create a new bank account
def create_account():
    name = input("Enter your name: ")
    acc_no = input("Enter new account number: ")

    if acc_no in accounts:
        print("⚠️ Account already exists!\n")
        return

    # Create new account with zero balance
    accounts[acc_no] = {"name": name, "balance": 0.0, "transactions": []}
    print(f"✅ Account created successfully for {name}!\n")

# Function to deposit money
def deposit():
    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
        print("⚠️ Account not found!\n")
        return

    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("⚠️ Invalid amount!\n")
            return
    except ValueError:
        print("⚠️ Please enter a valid number!\n")
        return

    accounts[acc_no]["balance"] += amount
    # Record transaction with timestamp
    accounts[acc_no]["transactions"].append(
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Deposit", amount, accounts[acc_no]["balance"])
    )
    print(f"💰 Deposited ₹{amount:.2f}. New Balance: ₹{accounts[acc_no]['balance']:.2f}\n")

# Function to withdraw money
def withdraw():
    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
        print("⚠️ Account not found!\n")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("⚠️ Invalid amount!\n")
            return
    except ValueError:
        print("⚠️ Please enter a valid number!\n")
        return

    if amount > accounts[acc_no]["balance"]:
        print("❌ Insufficient balance!\n")
        return

    accounts[acc_no]["balance"] -= amount
    # Record transaction
    accounts[acc_no]["transactions"].append(
        (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Withdraw", -amount, accounts[acc_no]["balance"])
    )
    print(f"💸 Withdrawn ₹{amount:.2f}. Remaining Balance: ₹{accounts[acc_no]['balance']:.2f}\n")

# Function to check balance
def check_balance():
    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
        print("⚠️ Account not found!\n")
        return

    print(f"🏦 Current Balance for {accounts[acc_no]['name']}: ₹{accounts[acc_no]['balance']:.2f}\n")

# Function to view transaction history
def view_history():
    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
        print("⚠️ Account not found!\n")
        return

    transactions = accounts[acc_no]["transactions"]
    if not transactions:
        print("No transactions found.\n")
        return

    print(f"\n📜 Transaction History for {accounts[acc_no]['name']}:")
    print("Date & Time           | Type      | Amount    | Balance After")
    print("-------------------------------------------------------------")
    for t in transactions:
        print(f"{t[0]} | {t[1]:<9} | {t[2]:>8.2f} | {t[3]:>13.2f}")
    print()

# Function to download bank statement as CSV file
def download_statement():
    acc_no = input("Enter your account number: ")
    if acc_no not in accounts:
        print("⚠️ Account not found!\n")
        return

    transactions = accounts[acc_no]["transactions"]
    if not transactions:
        print("No transactions to download.\n")
        return

    # File name includes account number
    file_name = f"BankStatement_{acc_no}.csv"
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date & Time", "Type", "Amount", "Balance After"])
        writer.writerows(transactions)

    print(f"📁 Bank statement saved as '{file_name}' successfully!\n")

# Main program menu
def main():
    while True:
        print("===== Intelligent Banking Transaction Simulator =====")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Download Bank Statement")
        print("7. Exit")
        print("=====================================================")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_history()
        elif choice == "6":
            download_statement()
        elif choice == "7":
            print("Thank you for using the Intelligent Banking System! 👋")
            break
        else:
            print("⚠️ Invalid choice! Please try again.\n")

# Run the simulator
if __name__ == "__main__":
    main()
