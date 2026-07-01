def payment_type(keyin):
    if keyin==1:
        return "現金"
    elif keyin==2:
        return "刷卡"
    else:
        return "未知"

def add_expense():
    expenses=[]
    howmany=int(input("請輸入今天有幾筆開銷："))
    for num in range(howmany):
        amount=int(input(f"請輸入金額{num+1}:"))
        category=input(f"請輸入項目{num+1}:")
        payment=payment_type(int(input("現金請輸入1,刷卡請輸入2:")))
        expense={
            "amount":amount,
            "category":category,
            "payment":payment
        }
        expenses.append(expense)
    return expenses

def show_expenses(expenses):
    print("\n=====今日支出=====")
    for expense in expenses:
        print(
            f'{expense["category"]}:'
            f'{expense["amount"]}元'
            f'使用{expense["payment"]}'
        )

def calculate_total(expenses):
    total=0
    for expense in expenses:
        total+=expense["amount"]
    return total


def main():
    expenses=add_expense()
    income=int(input("請輸入今日收入:"))
    show_expenses(expenses)
    total=calculate_total(expenses)
    remaining=income-total
    print(f"\n=====今日收支=====")
    print(f"收入:{income}元")
    print(f"支出:{total}元")
    print(f"剩餘:{remaining}元")
    print("==================")

main()
