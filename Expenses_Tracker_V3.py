import json

def load_data():
    with open("expenses.json", "r", encoding="utf-8") as file:
        expenses = json.load(file)
    return expenses

def save_data(expenses):
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)


def payment_type():
    while True:
        keyin = inputchk("現金請輸入1,刷卡請輸入2:")
        if keyin == 1:
            return "現金"
        elif keyin == 2:
            return "刷卡"
        print("輸入錯誤，現金請輸入1，刷卡請輸入2:")
        
            

def add_expense(expenses):
    amount = inputchk(f"請輸入金額:")
    category = input(f"請輸入項目:")
    payment = payment_type()
    expense={
        "amount":amount,
        "category":category,
        "payment":payment
    }
    if confirm("確定要增加嗎?Y/N:"):    
        expenses.append(expense)

def show_expenses(expenses):
    print("\n=====今日支出=====")
    if len(expenses) == 0:
        print("目前沒有任何支出")
        return
    for index,expense in enumerate(expenses, start=1):
        print(
            f'{index}.'
            f'{expense["category"]}:'
            f'{expense["amount"]}元'
            f'使用{expense["payment"]}'
        )

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def delete_expense(expenses):
    index = input_expenses_index("請輸入要刪除的項目編號:",expenses)
    if confirm("確定要刪除嗎?Y/N:"):
        expenses.pop(index)


def fix_expense(expenses):
    index = input_expenses_index("請輸入要修改的支出編號:"),expenses)
    new_amount = inputchk("請輸入正確的金額:")
    if confirm("確定要修改嗎?Y/N:"):
        expenses[index]["amount"] = new_amount

def inputchk(message):
    while True:
        try:
            keyin = int(input(message))
            return keyin
        except ValueError:
            print("輸入錯誤，請重新輸入數字！")
        
def input_expenses_index(message,expenses):
    index = inputchk(message)
    while True:
        if 0 < index <= len(expenses):
            return index-1
        index = inputchk("輸入錯誤，請輸入小於已有的編號！")

def confirm(message):
    while True:
        check = input(message).upper()
        if check == "Y":
            return True
        elif check == "N":
            return False
        else:
            print ("請重新輸入:")
            

def menu():
    print("""
        ======== Expense Tracker ========\n\n
        1. 新增支出\n
        2. 刪除支出\n
        3. 修改支出\n
        4. 查看所有支出\n
        5. 查看總支出\n
        6. 離開\n\n
        =================================  
        """
    )
    while True : 
        
        choose = inputchk("請選擇:")
        if 1 <= choose <= 6 :
            return choose
        print("請輸入 1~6!")


def main():
    expenses = load_data()
    while True : 
        choose = menu()
        if choose == 1:
            add_expense(expenses)
            save_data(expenses)
        elif choose == 2:
            show_expenses(expenses)
            if len(expenses) == 0:
                continue
            delete_expense(expenses)
            save_data(expenses)
        elif choose == 3:
            show_expenses(expenses)
            if len(expenses) == 0:
                continue
            fix_expense(expenses)  
            save_data(expenses)

        elif choose == 4:
            show_expenses(expenses)
            print("\n")
        elif choose == 5:
            total=calculate_total(expenses)
            print(f"總支出為 : {total}\n")
        elif choose == 6:
            break
main()
