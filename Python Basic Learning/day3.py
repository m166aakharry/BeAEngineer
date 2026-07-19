'''
x=[100,200,300]
z=0
for y in x:
    z+=y
print(z)

count=1
while count<=5:
    print(count)
    count+=1
'''
count=int(input("今天有幾筆開銷："))
expenses=[]
for i in range(count):
    expense=int(input("請輸入支出："))
    expenses.append(expense)
total=sum(expenses)
print(f"總支出為{total}")