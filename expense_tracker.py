import re
import os
from datetime import datetime

# ==========================================
# 1. MIXIN CLASS (Demonstrating Multiple Inheritance)
# ==========================================
class LoggerMixin:
    """A mixin class to add logging functionality to transactions."""
    def log_action(self):
        print(f"[LOG] Successfully processed transaction on {self.date}.")


# ==========================================
# 2. BASE & SUBCLASSES (OOP, super(), Class Variables)
# ==========================================
class Transaction:
    # Class variable to keep track of total transaction count across all instances
    total_count = 0

    def __init__(self, amount, description, date):
        self.amount = amount            # Instance variable
        self.description = description  # Instance variable
        self.date = date                # Instance variable
        Transaction.total_count += 1

    def to_file_string(self):
        """Converts object data into a comma-separated string for file saving."""
        return f"GENERIC,{self.date},{self.amount},{self.description}\n"


# Expense inherits from Transaction AND LoggerMixin (Multiple Inheritance)
class Expense(Transaction, LoggerMixin):
    def __init__(self, amount, description, date, category):
        # Using super() to initialize attributes from the Transaction base class
        super().__init__(amount, description, date)
        self.category = category

    def to_file_string(self):
        # Polymorphism / Method Overriding
        return f"EXPENSE,{self.date},{self.amount},{self.category},{self.description}\n"


class Income(Transaction):
    def __init__(self, amount, description, date, source):
        super().__init__(amount, description, date)
        self.source = source

    def to_file_string(self):
        return f"INCOME,{self.date},{self.amount},{self.source},{self.description}\n"


# ==========================================
# 3. HELPER FUNCTIONS (Regex & File I/O)
# ==========================================
def validate_date(date_str):
    """Validates if the date string strictly matches YYYY-MM-DD using Regex."""
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date_str):
        raise ValueError("Invalid date format! Please use YYYY-MM-DD.")
    return date_str


def save_transaction(transaction_obj):
    """Saves a transaction object to a text file using File I/O."""
    try:
        with open("tracker_data.txt", "a") as file:
            file.write(transaction_obj.to_file_string())
    except IOError:
        print("Error: Could not save data to the file.")


def load_transactions():
    """Reads past transactions from file and returns a list of strings."""
    if not os.path.exists("tracker_data.txt"):
        return []
    
    try:
        with open("tracker_data.txt", "r") as file:
            return file.readlines()
    except IOError:
        print("Error: Could not read data from the file.")
        return []


# ==========================================
# 4. MAIN PROGRAM CONTROLLER (Loops & Conditionals)
# ==========================================
def main():
    # Load past records on startup
    records = load_transactions()
    print(f"--- Welcome to Expense & Budget Tracker ---")
    print(f"Loaded {len(records)} past records from storage.\n")

    # Main Application Loop
    while True:
        print("\nChoose an option:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary & History")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        # Conditional Logic for Menu Selection
        if choice == "1":
            try:
                amount = float(input("Enter income amount: "))
                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                
                source = input("Enter income source (e.g., Salary, Freelance): ").strip()
                description = input("Enter description: ").strip()
                
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                if not date_input:
                    date_input = datetime.now().strftime("%Y-%m-%d")
                
                # Validate date using regex helper
                validated_date = validate_date(date_input)

                # Create Income Object
                inc = Income(amount, description, validated_date, source)
                save_transaction(inc)
                print("Income added successfully!")

            except ValueError as e:
                # Exception Handling for wrong input formats
                print(f"Input Error: {e}")

        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: "))
                if amount <= 0:
                    raise ValueError("Amount must be greater than zero.")
                
                category = input("Enter category (e.g., Food, Rent, Transport): ").strip()
                description = input("Enter description: ").strip()
                
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                if not date_input:
                    date_input = datetime.now().strftime("%Y-%m-%d")
                
                validated_date = validate_date(date_input)

                # Create Expense Object (Demonstrates multiple inheritance with mixin)
                exp = Expense(amount, description, validated_date, category)
                save_transaction(exp)
                exp.log_action() # Calling method from LoggerMixin
                print("Expense added successfully!")

            except ValueError as e:
                print(f"Input Error: {e}")

        elif choice == "3":
            # View Summary using File I/O reloading
            current_records = load_transactions()
            if not current_records:
                print("No transactions recorded yet.")
                continue

            print("\n--- Transaction History ---")
            total_income = 0.0
            total_expense = 0.0

            for line in current_records:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    t_type = parts[0]
                    t_date = parts[1]
                    t_amount = float(parts[2])

                    if t_type == "INCOME":
                        total_income += t_amount
                        print(f"[INCOME] Date: {t_date} | Amount: +${t_amount:.2f} | Source: {parts[3]} | Desc: {parts[4]}")
                    elif t_type == "EXPENSE":
                        total_expense += t_amount
                        print(f"[EXPENSE] Date: {t_type if False else t_date} | Amount: -${t_amount:.2f} | Cat: {parts[3]} | Desc: {parts[4]}")

            print("-" * 30)
            print(f"Total Income:  ${total_income:.2f}")
            print(f"Total Expenses: ${total_expense:.2f}")
            print(f"Net Balance:    ${(total_income - total_expense):.2f}")
            print(f"Total Transactions Created (Class Variable Tracker): {Transaction.total_count}")

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()