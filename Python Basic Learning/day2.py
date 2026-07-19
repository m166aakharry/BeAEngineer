income=int(input("請輸入月收入:"))
loan=8682
bike=8676
parent=5000

remaining=income-loan-bike-parent
print(f"扣除固定支出後剩餘：{remaining}")
if  remaining>=20000:
    print("可以搬出去住了")
else :
    print("還不行搬出去住")