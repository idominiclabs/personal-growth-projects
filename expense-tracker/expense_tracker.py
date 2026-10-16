#Expense tracker
import time

expenses = []

def add_expense():
    try:
        name = input("Enter Expense name: ").strip().lower()
        amount = int(input("Enter amount: ").strip())
        category = input("Enter category: ").strip().lower()
        
        if name and amount > 0 and category:
            expense = {
                "name": name,
                "amount": amount,
                "category": category
            }
            expenses.append(expense)
            print("Expense has been added successully!")
            
        else:
            print("Enter valid characters!")
            
    except ValueError:
        print("Enter a valid amount!")

        
def view_expenses():
    temp_expense_list = []
    if expenses:
        print("All expenses")
        for expense in expenses:
            expense_str = f"Expense name: {expense.get("name").title()}\n\tAmount: ₦{expense.get("amount")}\n\tCategory: {expense.get("category").title()}"
            temp_expense_list.append(expense_str)
            
        for number,each in enumerate(temp_expense_list, start=1):
            print(f"{number}. {each}")
            
    else:
           print("Can't view, add expense to view!")
           
         
def total_spending():
    total = 0
    if expenses:
        for expense in expenses:
            total += expense.get("amount")
            
        print(f"Total expense: ₦{total}")
        
    else:
        print("Can't calculate total spending, add expense to calculate!")
        
        
def highest_spending():
    if expenses:
        highest = 0
        for expense in expenses:
            if expense.get("amount") > highest:
                highest = expense.get("amount")
            
        print(f"Highest spending: ₦{highest}")
        
    else:
        print("Can't calculate highest spending, add an expense to calculate!")
    
    
def category_spending():
    if expenses:
        category = {}
        for expense in expenses:
            if expense.get("category") not in category:
                category[expense.get("category")] = expense.get("amount")
                
            else:
                category[expense.get("category")] += expense.get("amount")
                
        print("Spending by category")
        for key,value in category.items():
            print(f"{key.title()}: ₦{value}")
            
    else:
        print("Add expense to view spending by category!")
         

def highest_category():
    if expenses:
        category = {}
        for expense in expenses:
            if expense.get("category") not in category:
                category[expense.get("category")] = expense.get("amount")
                
            else:
                category[expense.get("category")] += expense.get("amount")
        
        category1 = category.items()
        category = 0
        highest = ""
        for key,value in category1:
            if value > category:
                highest = [key,value]
                category = value
            
        print("Highest category")
        print(f"{highest[0].title()}: ₦{highest[1]}")
        
        
def delete_expense():
    if expenses:
        view_expenses()
        try:
            prompt = int(input("Enter the serial number of the expense you want to delete: ").strip())
            if 0 < prompt <= len(expenses):
                expenses.pop(prompt - 1)
                print("The expense has been deleted successfully!")
                
            else:
                print("Enter a valid serial number!")
                
        except ValueError:
            print("Enter a valid serial number!")
            
    else:
        print("Deletion failed, add an expense to delete!")
    
            
print("===== Expense tracker =====")
while True:
    user_prompt = input("\n1. Add expense\n2. View all expenses\n3. Total spending\n4. Highest spending\n5. Spending by category\n6. Category with the highest spending\n7. Delete an expense\n8. Exit\n> ").replace(" ","").lower()
    if user_prompt in ("1","addexpense"):
        add_expense()
    
    elif user_prompt in ("2","viewallexpense"):
        view_expenses()
        
    elif user_prompt in ("3","totalspending"):
        total_spending()
        
    elif user_prompt in ("4","highestspending"):
        highest_spending()
        
    elif user_prompt in ("5","spendingbycategory"):
        category_spending()
        
    elif user_prompt in ("6","categorywiththehigestspending"):
        highest_category()
        
    elif user_prompt in ("7","deleteanexpense"):
        delete_expense()
    
    elif user_prompt in ("8","exit"):
        print("Exiting...")
        time.sleep(3)
        print("Exited!")
        break
        
    else:
        print("Invalid command!")