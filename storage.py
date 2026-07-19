import json

def load_data():
    with open("expenses.json", "r", encoding="utf-8") as file:
        expenses = json.load(file)
    return expenses

def save_data(expenses):
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)
