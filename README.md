# Expense Tracker

A command-line application to record and manage daily expenses — add, view, search, update, delete, and generate reports, with data that persists across sessions using a local JSON file.

Built with Python as a learning project to go beyond basic CRUD and practice analytics features like filtering by month and grouping by category.

---

## What it does

You get a simple text menu when you run the app:

```
============================
 Expense Tracker
============================
1. Add Expense
2. View All Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Monthly Summary
7. Category Report
8. Exit
```

Each expense stores five pieces of information: a unique ID, title, amount, category, and date. When you exit using option 8, everything is saved to `expenses_db.json`. The next run loads it right back.

---

## How to run it

You just need Python 3 — no external libraries required.

```bash
python3 main.py
```

---

## Project structure

```
Expense_Tracker_System/
├── main.py             # Entry point — runs the menu loop and handles all user input
├── ExpenseManager.py   # Business logic — all operations on the expenses list
├── Expense.py          # The Expense class — defines what one expense looks like
└── expenses_db.json    # Auto-created on first save — stores your data
```

### How the files relate to each other

- **`Expense.py`** is the blueprint for a single expense. It knows how to display itself, convert itself to a dictionary for JSON saving (`to_dict`), and reconstruct itself from a dictionary when loading (`from_dict`).
- **`ExpenseManager.py`** holds the list of all expenses and handles every operation — adding, searching, updating, deleting, generating summaries, saving to disk, and loading from disk.
- **`main.py`** is the interface layer. It shows the menu, validates all user input, calls the right method on `ExpenseManager`, and prints the result. It doesn't touch data directly.

---

## Features

- **Add an expense** — Validates that title and category aren't blank, amount is a positive number, and date is in `DD-MM-YYYY` format. Each expense gets a unique ID (UUID) automatically.
- **View all expenses** — Lists every expense alphabetically by title with all details.
- **Search by title** — Case-insensitive lookup. Finds "pizza" even if stored as "Pizza".
- **Update an expense** — Change title, amount, category, or date. Leave any field blank to skip it.
- **Delete an expense** — Removes the expense permanently from the list.
- **Monthly summary** — Enter a month and year to see: total spent, number of expenses, highest expense, lowest expense, and average. Only looks at expenses from that specific month.
- **Category report** — Groups all expenses by category and shows the total spent and number of expenses per category in a formatted table.
- **Persistent storage** — Data is saved as JSON on exit and loaded back automatically on the next run. UUIDs and dates are fully preserved across sessions.

---

## What I learned building this

- How to filter a list using list comprehensions with conditions — the foundation of the monthly summary feature
- How to group data into a dictionary: looping through a list, creating a bucket per category if it doesn't exist, and accumulating totals and counts into it
- The JSON date problem: Python's `date` objects can't be serialized directly to JSON — you have to convert to a string with `strftime()` when saving, and parse back with `strptime()` when loading
- The difference between `json.dump()` and `json.dumps()` — the `s` means "to string", not "to file". Getting this wrong silently fails because the error gets swallowed by `try/except`
- Why indentation bugs are tricky — having accumulation logic inside an `if` block instead of outside it means only the first item per group gets counted, and everything else is silently skipped
- How `to_dict()` and `from_dict()` form a pair: every field you serialize in one must be deserialized in the other, and types (like dates) need explicit conversion both ways
