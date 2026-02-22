import random

# low = 1
# high = 6
#number = random.randint(low, high) #if you want to print a random number. It can place variables also, since it contains integers
#number = random.random() #If you want to sort a random float number betweem zero and one, use this method
# options = ("rock", "paper", "scissors")
# option = random.choice(options) #use this method to pick one option inside options
# cards = ["2", "3", "4", "5", "6", "7"]
# random.shuffle(cards)
# print(cards)

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Import random game

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# while is_running:
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess > answer:
#             print("Too high. Try again!")
#         elif guess < answer:
#             print("Too low. Try again!")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")

# ---------------------------------------------------------------------------------------------------------------------------
# Rock, scissors and paper

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True

while running:
    player = None
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        
        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It is a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win")
        elif player == "paper" and computer == "rock":
            print("You win")
        elif player == "scissors" and computer == "paper":
            print("You win")
        else:
            print("You lose")
        
        play_again = input("Play again? (y / n): ").lower() #Lower case for this input
        if not play_again == "y":
            running = False

print("Thanks for playing! ")