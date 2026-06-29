from datetime import datetime
from ExpenseManager import ExpenseManager

expenseManager = ExpenseManager()

expenseManager.load_data()

while True:

    print("============================")
    print("Expense Tracker")
    print("============================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Monthly Expense")
    print("7. Category Report")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        print("\nPlease fill below details of Expenses to be added: \n")
        expense_title = input("\nEnter the title of expense: ")
        while expense_title=="":
            expense_title = input("\nExpense title can't be empty; please enter the title of expense: ").strip()

        while True:
            try:
                expense_amount = int(input("\nEnter the amount of expense: "))
                if expense_amount <= 0:
                    expense_amount = int(input("\nExpense Amount can't be less than 0, please enter the amount of expense: "))
                break
            except ValueError as e:
                print("\nInvalid input amount. Amount needs to be valid integer")

        expense_category = input("\nEnter the category of expense: ")
        while expense_category == "":
            expense_category = input("\nCEnter the category of expense: ").strip()

        while True:
            user_date_str = input("\nEnter the date of expense (DD-MM-YYYY): ").strip()
            try:
                # Convert string format directly into a date object
                expense_date = datetime.strptime(user_date_str, "%d-%m-%Y").date()
                break  # Date is valid, exit the loop   
            except ValueError:
                print("\nInvalid date format! Please write it as DD-MM-YYYY (e.g., 27-06-2026).")
        
        new_expense = expenseManager.add_expense(expense_title, expense_amount, expense_category, expense_date)

        if new_expense:
            print(f"\n{expense_title} added successfully!")
        else:
            print(f"\n{expense_title} already exists in expenses list. Please add new expenses.")

    elif choice == "2":
        records = expenseManager.view_expense()
        if not records:
            print("\nNo records found in history. Start adding new expenses using Option 1.")
        else:
            print("\nExpenses and their details: ")
            for expense in records:
                expense.display_expense()

    elif choice == "3":
        print("\nExpenses and their details for you to select Expense ID: ")
        for expense in records:
            expense.display_expense()

        expense_id = input("\nPlease enter the expenseID for which you want to search: ")
        while expense_id == "":
            expense_id = input("\nExpense ID can't be empty; please enter the ID of expense which you want to search: ")
            break
        searched_expense = expenseManager.search_expense(expense_id)
        if searched_expense is None:
            print("\nSearched Expense doesn't exist in directory; please add that expense using Option 1")
        else:
            print(f"\nSearched expense with {expense_id} and its details: ")
            searched_expense.display_expense()

    elif choice == "4":
        print("\nExpenses and their details for you to select Expense ID: ")
        for expense in records:
            expense.display_expense()

        expense_id = input("\nPlease enter the ID of expense which you want to update: ").strip()
        while expense_id == "":
            expense_id = input("\nExpense ID can't be empty for which you want to update expense; please enter the title of expense: ").strip()
            
        new_title = input(f"\nPlease enter the new title of expense for {expense_id}: (keep it blank to skip)")
        if new_title == "":
            new_title = None
        
        new_amount = None
        while True:

            amount_input = (input(f"\nPlease enter then new amount for the expense {expense_id}: (Keep it blank to skip)"))
            if amount_input == "":
                break
            try:
                new_amount = int(amount_input)
                if new_amount > 0:
                    break
                print("\nAmount must be grater than 0.")
            except ValueError:
                print("\nInvalid input! Amount must be a valid integer!")

        new_category = input(f"\nPlease enter the new category of expense {expense_id}: (Keep it blank to skip)")
        
        if new_category == "":
            new_category = None

        new_expense_date = None
        while True:
            new_date_str = input(f"\nEnter the new date of expense (DD-MM-YYYY) for '{expense_id}' (keep it blank to skip): ").strip()

            if new_date_str == "":
                break
            try:
                new_expense_date = datetime.strptime(new_date_str, "%d-%m-%Y").date()
                break
            except ValueError:
                print("\nInvalid date format! Please write it as DD-MM-YYYY (e.g., 27-06-2026).")
        update_expense = expenseManager.update_expense(expense_id, new_title, new_amount, new_category, new_expense_date)
        if update_expense:
            print(f"\nDetails updated for expense {expense_id}")
        else:
            print(f"\nDetails can't be updated for expense {expense_id}")

    elif choice == "5":
        print("\nExpenses and their details for you to select Expense ID: ")
        for expense in records:
            expense.display_expense()

        expense_id = input(f"\nPlease enter the ID of the expense which you want to delete: ")
        while expense_id == "":
            expense_id = input(f"\nTitle can't be empty for which you want to delete; please enter the title: ").strip()
        
        remove_expense = expenseManager.delete_expense(expense_id)
        if remove_expense:
            print(f"\nExpense ({expense_id}) is successfully deleted!")
        else:
            print(f"\nExpense ({expense_id}) doesn't exist in list!")
    
    elif choice == "6":
        month = None

        month = input("\n Enter the month for which you want to see summary of expenses: ").strip()
        while month == "":
            month = input("\n Month can't be empty, please enter the month for which you want to see summary of expenses: ").strip()

        while True:
            try:
                month_input = int(month)

                if month_input < 1 or month_input > 12:
                    month_input = int(input("\nMonth must be between 1-12; please add correct month number: "))
                    continue
                break
            except ValueError:
                month = input("\nInvalid input! Please enter a valid number for the month (1-12): ").strip()  
        year = None

        year = input("\n Enter the year for which you want to see summary of expenses: ").strip()
        while year == "":
            year = input("\n Year can't be empty, please enter the month for which you want to see summary of expenses: ").strip()

        while True:
            year_input = int(year)

            if year_input < 0:
                year_input = int(input("\nyear can't be less than 0; please add correct year: "))
            break
        
        summary = {}
        summary = expenseManager.generate_monthly_summary(month_input, year_input)

        if summary is None:
            print("\n No monthly expense generated!")
        else:
            print(f"\nMonthly summary of expenses for {month_input} and {year_input}:  ")
            print(f"\nTotal Expense in {summary["month"]} and {summary["year"]}: {summary["total"]}")
            print(f"\nTotal number of Expenses in {summary["month"]} and {summary["year"]}: {summary["count"]}")
            print(f"\Average of Expenses in {summary["month"]} and {summary["year"]}: {summary["average"]}")
            print(f"\nHighest Expense in {summary["month"]} and {summary["year"]}: {summary["highest"]}")
            print(f"\nLowest in {summary["month"]} and {summary["year"]}: {summary["lowest"]}")
        
    elif choice == "7":
        category_report = expenseManager.generate_category_report()
        
        if category_report is None:
            print("\nCategory report couldn't be generated! Please add few expenses in different categories!")
        
        print("\n===============================")
        print("     CATEGORY WISE REPORT      ")
        print("===============================")
        print(f"{'Category':<15} | {'Total Spent':<12} | {'Count'}")
        print("-" * 45)

        # 3. Unpack and loop through your nested dictionary data structure
        for category, stats in category_report.items():
            total_amount = stats["total"]
            expense_count = stats["count"]
            
            # Format output with neat alignments and two decimal place formatting
            print(f"{category:<15} | ₹{total_amount:<11.2f} | {expense_count} items")
        
        print("===============================")

    elif choice == "8":
        print("\nSaving database records before shutdown...")
        expenseManager.save_data_to_json() # Save everything right before exiting
        print("Exiting program. Goodbye! ")
        break

    else:
        print("\nInvalid choice! Please enter 1, 2, 3, 4, 5, 6, 7 or 8.")
        
