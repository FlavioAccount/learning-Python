#Python Baking Program
#show_balance, deposit, withdraw

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit(balance):
    amount = float(input("Type the amount of money you are going to add: "))
    choice = input(f"You are about to add ${amount:.2f} into your account. Do you confirm that you want to add: yes / no ").lower()
    if choice == "yes" and amount>0:
        balance += amount
        print(f"You added {amount:.2f} into your bank account")
        return balance
    elif choice == "no":
        print("Back to the menu")
    else:
        print("Invalid choice, back to the main menu")
    

def withdraw(balance):
    withdraw = float(input("Get the amount of money of your account: "))
    if withdraw <= balance and withdraw > 0:
        balance -= withdraw
        print(f"You balance is now {balance:.2f}")
        return balance
    else:
        print("Insuficient founds")

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*************Select one of the options bellow:**************")
        print("1: Show balance")
        print("2: Deposit Money")
        print("3: Withdraw")
        print("4: Exit")
        print("------------------------------------------------------------")
        option = input("Enter your input here: ")
        match option:
            case "1":
                show_balance(balance)
            case "2":
                balance = deposit(balance)
            case "3":
                balance = withdraw(balance)
            case "4":
                is_running = False
                pass 
            case _:
                print("Invalid choice! Try again: ")
    print("Thanks for using our bank! Have a nice day")
if __name__ == '__main__':
    main()    
    
