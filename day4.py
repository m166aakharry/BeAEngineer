def remaining(income):
    loan=8682
    bike=8676
    parent=5000
    return income-loan-bike-parent

income=int(input("請輸入今日收入"))
today=remaining(income)
print(f"扣除固定支出後剩餘：{today}")
if  today>=20000:
    print("可以搬出去住了")
else :
    print("還不行搬出去住")