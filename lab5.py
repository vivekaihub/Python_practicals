print("=====Monthly expense tracker=====")

n = int(input("enter expense number"))

expenses = []
total=0

for i in range(n):
    amount = float(input(f"enter expense {i + 1}:"))
    expenses.append(amount)
    total+=amount

while True:
    print("\n-----Expense Tracker Menu-----")
    print("1. show all expenses")
    print("2. show total expense")
    print("3. add new expense")
    print("4. exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        print("\nexpense list")
        for i in range(len(expenses)):
            print(f"expense {i + 1}: {expenses[1]}")

    elif choice ==2:
        print("total monthly expense=", total)

    elif choice == 3:
        new_expense = float(input("enter new expense: "))
        expenses.append(new_expense)
        total += new_expense
        print("expense add successfully.")

    elif choice ==4:
        print("Thank you for using Monthly expense tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
                
       