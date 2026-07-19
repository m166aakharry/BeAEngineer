import json
expenses = [
    {
        "amount": 100,
        "category": "早餐",
        "payment": "現金"
    }
]

with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file, ensure_ascii=False, indent=4)

print("儲存完成！")