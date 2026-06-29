from datetime import date, datetime
import uuid

class Expense:

    def __init__(self, title: str, amount: int, category: str, date: date, expense_id : str = None):
        self.expense_id = expense_id if expense_id else str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        """Controls how expense details look like when you print it"""
        return f"ExpenseID: {self.expense_id} | Title: {self.title} | Amount: {self.amount} | Category: {self.category} | Date: {self.date}"

    def display_expense(self):
        """Displays Expense details in formatted way"""
        print(self)

    def to_dict(self):
        """Converts object data back to a dictionary layout for easy JSON saving"""
        return {
            "expense_id": self.expense_id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%d-%m-%Y")
        }
    
    @classmethod
    def from_dict(cls, data):
        parsed_date = datetime.strptime(data["date"], "%d-%m-%Y").date()
        return cls(data["title"], data["amount"], data["category"], parsed_date, data["expense_id"])