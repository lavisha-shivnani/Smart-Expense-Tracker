import json
from datetime import datetime
expenses = []
categories = ["Food", "Travel", "Shopping", "Bills", "Medical", "Education", "Entertainment", "Other"]
def display_menu():
    print("\n"+"="*40)
    print("Smart Expense Tracker")
    print("="*40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Category Summary")
    print("7. Expense Statistics")
    print("8. Save Data")
    print("9. Exit")

def get_choice():
        while True:
            try:
                choice=int(input("Enter your choice (1-9):  "))
                if( 1<= choice <= 9):
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input.Please enter a valid number between 1 and 9.")

def add_expense():
    print("\n=============== Add Expense ===============")

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Invalid amount.")

    print("\nSelect Category:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Enter category number: "))

            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break

            print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

    description = input("Enter description: ")

    expense = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(expense)
    save_data()

    print("Expense added successfully!")

def view_expenses():
     print("\n ===============View Expenses===============")
     if len(expenses) == 0:
          print("No expenses recorded.")
          return

     print(f"{'ID':<5}{'DATE':<20}{'CATEGORY':<15}{'AMOUNT':<12}{'DESCRIPTION'}")
     print("-" * 70)

     for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<20}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<11.2f}"
            f"{expense['description']}"
        )

def search_expenses():
     print("\n ===============Search Expenses===============")
     category = input("Enter category to search: ")
     found=False
     print(f"{'ID':<5}{'DATE':<20}{'CATEGORY':<15}{'AMOUNT':<12}{'DESCRIPTION'}")
     print("-" * 70)
     for expense in expenses:
          if expense["category"].lower()== category.lower():
               print(
    f"{expense['id']:<5}"
    f"{expense['date']:<20}"
    f"{expense['category']:<15}"
    f"₹{expense['amount']:<11.2f}"
    f"{expense['description']}"
)
               found=True
     if not found:
               print("No expenses found for the given category.")

def edit_expense():
     print("\n ===============Edit Expense===============")
     while True:
        try:
             expense_id = int(input("Enter the ID of the expense to edit: "))
             break
        except ValueError:
             print("Please enter a valid ID.")
    
     for expense in expenses:
           if expense["id"]==expense_id:

                expense["amount"]=float(input("Enter new amount: "))
                print("\nSelect Category:")
                for index, category in enumerate(categories, start=1):
                     print(f"{index}. {category}")
                while True:
                       try:
                               choice = int(input("Enter category number: "))
                               if 1 <= choice <= len(categories):
                                    expense["category"] = categories[choice - 1]
                                    break
                               print("Invalid choice.")
                       except ValueError:
                            print("Please enter a valid number.")
                
                expense["description"]=input("Enter new description: ")
                save_data()
                print("Expense updated successfully!")

                return

     print("Expense with the given ID not found.")

def delete_expense():
     print("\n ===============Delete Expense===============")
     while True:
        try:
             expense_id = int(input("Enter the ID of the expense to delete: "))
             break
        except ValueError:
             print("Please enter a valid ID.")
     for expense in expenses:
          if expense["id"] == expense_id:
              confirm = input("Are you sure you want to delete this expense? (y/n): ").lower()
              if confirm == "y":
                   expenses.remove(expense)
                   save_data()
                   print("Expense deleted successfully!")
                   return
              else:
                   print("Deletion cancelled.")
                   return
     print("Expense with the given ID not found.")

def category_summary():
    print("\n========== CATEGORY SUMMARY ==========")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]
        else:
            summary[category] = expense["amount"]

    print("\nCategory\tTotal Amount")
    print("-" * 30)

    for category, total in summary.items():
        print(f"{category:<15} ₹{total:.2f}")

def expense_statistics():
    print("\n========== EXPENSE STATISTICS ==========")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    amounts = []

    for expense in expenses:
        amounts.append(expense["amount"])

    total_amount = sum(amounts)
    highest = max(amounts)
    lowest = min(amounts)
    average = total_amount / len(amounts)

    print(f"Total Expenses : {len(expenses)}")
    print(f"Total Amount   : ₹{total_amount:.2f}")
    print(f"Highest Expense: ₹{highest:.2f}")
    print(f"Lowest Expense : ₹{lowest:.2f}")
    print(f"Average Expense: ₹{average:.2f}")
          
def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Data saved successfully!")

def load_data():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []

     

def main():
        load_data()
        while True:
             display_menu()
             choice = get_choice()
             if choice == 1:
                  add_expense()
             elif choice == 2:
                  view_expenses()
             elif choice == 3:
                  search_expenses()
             elif choice == 4:
                  edit_expense()
             elif choice == 5:
                    delete_expense()
             elif choice == 6:
                    category_summary()
             elif choice == 7:
                    expense_statistics()
             elif choice == 8:
                  save_data()

             elif choice == 9:
                  print("Thankyou for using the Smart Expense Tracker. Goodbye!")
                  break
             else:
                  print("This feature is not implemented yet. Please choose another option.")

        

if __name__ == "__main__":
    main()