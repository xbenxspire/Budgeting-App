'''
Date: Sep 12, 2023
Name: Benjamin Pierce
This program will ask the user to enter an amount that he/she budgeted for the month.
A loop should prompt the user to enter each expense for the month and keep a running total.
When the loop finishes, the program should display the amount that the user is over/under budget.
'''
def main():
    numberBudget = float(input("Enter dollar amount you have budgeted for this month: "))
    print(f"Your budget this month allows for ${numberBudget:.2f}")
    totalExpenses = 0.0
    count = 0
    terminateLoop = '-'
    while True:
        expense = input(f"Enter your expense amount for item {count+1} (enter '-' to end): ")
        if expense == terminateLoop:
            break
        else:
            expense = float(expense)
            totalExpenses += float(expense)
            count += 1
            
    print(f"Your total expenses: ${totalExpenses:.2f}")
    
    if totalExpenses == numberBudget:
        print("Excellent, you are within your monthly budget!")
    elif totalExpenses > numberBudget:
        print(f"You are over budget by ${totalExpenses - numberBudget:.2f}.")
    else:
        print(f"You have ${numberBudget - totalExpenses:.2f} leftover in your budget.")

if __name__ == '__main__':
    main()