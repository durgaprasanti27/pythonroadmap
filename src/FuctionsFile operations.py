import json
import os

FILE_NAME = "expenses.json"

# Function to load existing data from file
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except Exception:
        return []

# Function to save data to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def main():
    expenses = load_expenses()
    print("=== Persistent Expense Tracker ===")
    print(f"Loaded {len(expenses)} existing expense(s) from {FILE_NAME}.\n")

    while True:
        print("--- MENU ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        choice = input("Select (1-3): ")

        if choice == "1":
            item = input("Expense name: ")
            cost = float(input("Cost ($): "))
            expenses.append({"item": item, "cost": cost})
            save_expenses(expenses)
            print("✅ Saved to file!")

        elif choice == "2":
            if not expenses:
                print("⚠️ No expenses found.")
            else:
                for idx, exp in enumerate(expenses, 1):
                    print(f"{idx}. {exp['item']} - ${exp['cost']:.2f}")

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()