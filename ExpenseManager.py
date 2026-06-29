from Expense import Expense
from datetime import date
import json
import os

class ExpenseManager:

    def __init__(self):
        self.expenses = []
        self.FILENAME = "expenses_db.json"

    def add_expense(self, title: str, amount: int, category: str, date: date) -> None:
        """Processes Expense Insertion. Return true if successful, false if duplicate"""

        for expense in self.expenses:
            if expense.title.lower() == title.lower():
                return False

        new_expense = Expense(title, amount, category, date)
        self.expenses.append(new_expense)
        return True 
    
    def view_expense(self):
        """Displays all expenses and its information stored in Expense List"""
        return sorted(self.expenses, key=lambda exp:exp.title.lower())
    
    def search_expense(self, expense_id: str):
        """Finds an expense by its title."""
        for expense in self.expenses:
            if expense.expense_id == expense_id.lower():
                return expense
        return None
    
    def update_expense(self, expense_id: str, new_title: str = None, new_amount: int = None, new_category: str = None, new_date: date = None):
        """Updates expense details based on title of expense provided"""
        expense = self.search_expense(expense_id)
        if expense:
            if new_title is not None:
                expense.title = new_title
            if new_amount is not None:
                expense.amount = new_amount
            if new_category is not None:
                expense.category = new_category
            if new_date is not None:
                expense.date = new_date
            return True
        return False
            
    def delete_expense(self, expense_id: str):
        """Deletes expense based on provided title"""
        expense = self.search_expense(expense_id)
        if expense:
            self.expenses.remove(expense)
            return True
        return False
    
    def generate_monthly_summary(self, month: int=None, year: int=None):
        """Returns summary stats for all expenses in the given month and year."""
        filtered = [e for e in self.expenses if e.date.month == month and e.date.year == year]

        if not filtered:
            return None
        
        total = sum(e.amount for e in filtered)
        count = len(filtered)
        average = total/count
        highest = max(filtered, key=lambda e: e.amount)
        lowest = min(filtered, key=lambda e:e.amount)

        return {
            "month": month,
            "year": year,
            "total": total,
            "count": count,
            "average": average,
            "highest": highest,
            "lowest": lowest
        }
    
    def generate_category_report(self):
        """Groups expenses by category, returns totals and counts per category"""
        if not self.expenses:
            return None
        
        category_report = {}

        for expense in self.expenses:
            if expense.category not in category_report:
                category_report[expense.category] = {"total": 0, "count": 0}
            category_report[expense.category]["total"] += expense.amount
            category_report[expense.category]["count"] += 1
        
        return category_report
    
    def save_data_to_json(self):
        """Saves all expenses into json file"""
        try:
            with open(self.FILENAME, "w") as file:
                json.dump([e.to_dict() for e in self.expenses], file, indent=4)
            print("\n[System] Data saved successfully to file.")
        except Exception as e:
            print(f"\n[System] Error saving data: {e}")

    def load_data(self):
        """Loads expenses from JSON file into self.expenses as Expense objects"""
        if not os.path.exists(self.FILENAME):
            print(f"\n[System] No previous database file found. Starting fresh.")
            return
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
            for d in data:
                self.expenses.append(Expense.from_dict(d))
            print("[System] Data loaded successfully from disk.")
        except Exception as e:
            print(f"[System] Error loading data: {e}. Starting with an empty list.")