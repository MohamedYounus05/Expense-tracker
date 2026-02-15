# ==============================
# 💰 Smart Expense Tracker App
# ==============================

expenses_list = []

print("\n===================================")
print("      💰 WELCOME TO EXPENSE TRACKER")
print("===================================\n")

while True:
    print("\n========= 📌 MAIN MENU =========")
    print("1️⃣  Add Expense")
    print("2️⃣  View All Expenses")
    print("3️⃣  View Total Spending")
    print("4️⃣  Exit")
    print("================================")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    # ==============================
    # 1️⃣ ADD EXPENSE
    # ==============================
    if choice == 1:
        print("\n------ ➕ Add New Expense ------")

        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (Food/Travel/Shopping/Books/etc): ")
        description = input("Enter description: ")

        try:
            amount = float(input("Enter amount: ₹ "))
        except ValueError:
            print("❌ Invalid amount. Please enter numbers only.")
            continue

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses_list.append(expense)
        print("✅ Expense added successfully!")

    # ==============================
    # 2️⃣ VIEW ALL EXPENSES
    # ==============================
    elif choice == 2:
        print("\n------ 📋 All Expenses ------")

        if len(expenses_list) == 0:
            print("⚠️ No expenses recorded yet.")
        else:
            print("\n{:<5} {:<12} {:<15} {:<25} {:<10}".format(
                "No.", "Date", "Category", "Description", "Amount"
            ))
            print("-" * 75)

            for index, expense in enumerate(expenses_list, start=1):
                print("{:<5} {:<12} {:<15} {:<25} ₹{:<10.2f}".format(
                    index,
                    expense["date"],
                    expense["category"],
                    expense["description"],
                    expense["amount"]
                ))

    # ==============================
    # 3️⃣ VIEW TOTAL SPENDING
    # ==============================
    elif choice == 3:
        total = sum(expense["amount"] for expense in expenses_list)
        print("\n💵 Total Spending: ₹ {:.2f}".format(total))

    # ==============================
    # 4️⃣ EXIT
    # ==============================
    elif choice == 4:
        print("\n👋 Thank you for using Expense Tracker!")
        print("Have a productive day! 🚀")
        break

    else:
        print("❌ Invalid choice. Please select between 1 and 4.")
