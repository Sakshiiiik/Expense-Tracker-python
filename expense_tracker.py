import csv
import os

filename = "expenses.csv"
expenses = []

# ✅ Load old expenses from file (if file exists)
if os.path.exists(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])  # convert amount back to float
            expenses.append(row)

while True:
    print("\n====== Expense Tracker App 💰 ======")
    print("1. Add Expense ➕")
    print("2. View All Expenses 📄")
    print("3. Total Expense 💸")
    print("4. Search by Category 🔍")
    print("5. Exit ❌")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n---- Add Expense ➕ ----")

        date = input("Enter date (DD-MM-YYYY): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category (food/travel/shopping): ")
        note = input("Enter note: ")

        expense = {
            "date": date,
            "amount": amount,
            "category": category,
            "note": note
        }

        expenses.append(expense)

        # ✅ Save to CSV file
        with open(filename, "w", newline="") as file:
            fieldnames = ["date", "amount", "category", "note"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for e in expenses:
                writer.writerow(e)

        print("\nExpense Added Successfully ✅ (Saved in file) 💾")

    elif choice == "2":
        print("\n---- All Expenses 📄 ----")

        if len(expenses) == 0:
            print("No expenses added yet 😅")
        else:
            for e in expenses:
                print(f"Date: {e['date']} | Amount: ₹{e['amount']} | Category: {e['category']} | Note: {e['note']}")

    elif choice == "3":
        print("\n---- Total Expense 💸 ----")

        total = 0
        for e in expenses:
            total = total + e["amount"]

        print("Total Expense = ₹", total)

    elif choice == "4":
        print("\n---- Search by Category 🔍 ----")

        search_cat = input("Enter category to search: ")
        found = False

        for e in expenses:
            if e["category"].lower() == search_cat.lower():
                print(f"Date: {e['date']} | Amount: ₹{e['amount']} | Category: {e['category']} | Note: {e['note']}")
                found = True

        if found == False:
            print("No expenses found in this category 😅")

    elif choice == "5":
        print("\nThanks for using Expense Tracker 💛 Byeee 👋")
        break

    else:
        print("\nInvalid choice 😅 Please enter 1-5")