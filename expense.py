
import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the expense file.")
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    title = input("What did you buy? ").strip()
    if not title:
        print("Expense name cannot be empty.")
        return

    category = input(
        "Category (Food/Travel/Shopping/Other): "
    ).strip().capitalize()

    if category not in ["Food", "Travel", "Shopping", "Other"]:
        print("Please choose Food, Travel, Shopping, or Other.")
        return

    try:
        amount = float(input("Enter amount (₹): "))

        if not 0 < amount < float("inf"):
            print("Enter a valid positive amount.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    expense = {
        "title": title,
        "category": category,
        "amount": round(amount, 2)
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense recorded successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n====== YOUR EXPENSES ======")

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def show_report(expenses):
    if not expenses:
        print("No data available for a report.")
        return

    total = sum(item["amount"] for item in expenses)
    biggest = max(expenses, key=lambda item: item["amount"])

    print("\n====== SPENDING REPORT ======")
    print(f"Total expenses: ₹{total:.2f}")
    print(f"Number of purchases: {len(expenses)}")
    print(
        f"Biggest expense: {biggest['title']} "
        f"(₹{biggest['amount']:.2f})"
    )

    print("\nSpending by category:")

    categories = {}

    for item in expenses:
        category = item["category"]
        categories[category] = (
            categories.get(category, 0) + item["amount"]
        )

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n💸 SMART SPENDING DETECTIVE")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Spending report")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_report(expenses)
        elif choice == "4":
            print("Goodbye! Keep tracking your spending.")
            break
        else:
            print("Invalid choice. Enter 1-4.")


if __name__ == "__main__":
    main()
