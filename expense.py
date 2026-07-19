from utils import input_new_expense, input_expenses_index, inputchk, confirm, update_data

class ExpenseTracker:
    def __init__(self,expenses):
        self.expenses = expenses
    
    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total
    
    def show_expenses(self):
        print("\n=====今日支出=====")
        for index,expense in enumerate(self.expenses, start=1):
            print(
                f'{index}.'
                f'{expense["category"]}:'
                f'{expense["amount"]}元'
                f'使用{expense["payment"]}'
            )
    
    def add_expense(self):
        #取得資料
        expense = input_new_expense()
        #存入資料庫
        if confirm("確定要增加嗎?Y/N:"):    
            self.expenses.append(expense)
            return True
        return False
    
    def delete_expense(self):
        index = input_expenses_index("請輸入要刪除的項目編號:",self.expenses)
        if confirm("確定要刪除嗎?Y/N:"):
            self.expenses.pop(index)
            return True
        return False


    def update_expense(self):
        index = input_expenses_index("請輸入要修改的支出編號:",self.expenses)
        new_amount = inputchk("請輸入正確的金額:")
        if confirm("確定要修改嗎?Y/N:"):
            update_data(self.expenses[index],new_amount)
            return True
        return False