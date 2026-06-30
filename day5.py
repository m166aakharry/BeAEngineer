def payment_type(keyin):
    if keyin==1:
        return "現金"
    elif keyin==2:
        return "刷卡"
    else:
        return "未知"
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
for num2 in expenses:
    print(num2["category"],":",num2["amount"],num2["payment"])