import json
from expense import Expense

def load_data():
    with open("expenses.json", "r", encoding="utf-8") as file:
        expenses = json.load(file)
    expense_objects = []
    for expense in expenses:
        expense_objects.append(Expense.from_dict(expense))
    return expense_objects

def save_data(expenses):
    saveexpenses = []
    for expense in expenses:
        saveexpenses.append(expense.to_dict())
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(saveexpenses, file, ensure_ascii=False, indent=4)
