# Python Slot Machine
import random
import time
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    value = [0, 1, 2, 3, 4]
    results = []

    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
def print_row(row):
    print(f"Spinning...")
    position =[" ", " ", " "]
    add = 0
    for caractere in row:
        position[add] = caractere
        time.sleep(1)
        print(" | ".join(position)) #This method insert this bar between the positions
        add = add + 1
def get_payout(row, bet):
    payment = 0
    if row[0] == row [1] == row[2]:
        if row[0] == '🍒':
            payment = bet * 4
        elif row[0] == '🍉':
            payment = bet * 6
        elif row[0] == '🍋':
            payment = bet * 8
        elif row[0] == '🔔':
            payment = bet * 10
        elif row[0] == '⭐':
            payment = bet * 20
        print(f"Congratulations! You won ${payment} 🎉")
    return payment
def main():
    balance = 100
    print("************************************")
    print("Welcome to Python Slots: ")
    print("Symbols 🍒 - 🍉 - 🍋 - 🔔 - ⭐ ") #To add an emoji type (Windows and .) 
    print("************************************")
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount or type exit: ")
        if bet == 'exit':
            break
        if not bet.isdigit():
            print("Please enter a valid number")
    
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
        if bet <= 0:
            print("Bet must be greater than 0")
        
        balance -= bet
        row = spin_row()
        print_row(row)
        balance += get_payout(row, bet)
    print("Thanks for playing!")


if __name__=='__main__': #This is a convention
    main()
