# Initialize an empty list to store expenses
expenses = []

print("=== Personal Expense Tracker (CLI) ===")

# Loop runs until the user chooses to exit (Option 4)
while True:
    print("\n--- MENU ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Total Spent")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")

    if choice == "1":
        item = input("Enter expense name (e.g., Coffee): ")
        cost = float(input("Enter cost ($): "))
        # Store as a dictionary inside our expenses list
        expenses.append({"item": item, "cost": cost})
        print(f"✅ Added: {item} - ${cost:.2f}")

    elif choice == "2":
        if not expenses:
            print("⚠️ No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            for index, exp in enumerate(expenses, 1):
                print(f"{index}. {exp['item']}: ${exp['cost']:.2f}")

    elif choice == "3":
        total = sum(exp["cost"] for exp in expenses)
        print(f"\n💵 Total Spent: ${total:.2f}")

    elif choice == "4":
        print("Exiting Expense Tracker. Great job practicing!")
        break  # Stops the loop

    else:
        print("❌ Invalid selection. Please enter 1, 2, 3, or 4.")