def payment_type(keyin):
    if keyin == 1:
        return "現金"
    elif keyin == 2:
        return "刷卡"
    else:
        return "未知"

def add_expense(expenses):
    amount = int(input(f"請輸入金額:"))
    category = input(f"請輸入項目:")
    payment = payment_type(int(input("現金請輸入1,刷卡請輸入2:")))
    expense={
        "amount":amount,
        "category":category,
        "payment":payment
    }
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
    delete_number = int(input("請輸入要刪除的項目編號:"))
    expenses.pop(delete_number - 1)

def fix_expense(expenses):
    fix_num = int(input("請輸入要修改的支出編號:"))
    fix_expense = int(input("請輸入正確的金額:"))
    expenses[fix_num-1]["amount"]=fix_expense


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
        choose = int(input("請選擇："))
        if 1 <= choose <= 6 :
            break
    return choose


def main():
    expenses = []
    while True : 
        choose = menu()
        if choose == 1:
            add_expense(expenses)
        elif choose == 2:
            show_expenses(expenses)
            if len(expenses) == 0:
                continue
            delete_expense(expenses)
        elif choose == 3:
            show_expenses(expenses)
            if len(expenses) == 0:
                continue
            fix_expense(expenses)  

        elif choose == 4:
            show_expenses(expenses)
            print("\n")
        elif choose == 5:
            total=calculate_total(expenses)
            print(f"總支出為 : {total}\n")
        elif choose == 6:
            break

main()
