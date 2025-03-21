import random

user_wins = 0
bot_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit: ").lower()
    
    if user_input == "q":  # Exit condition
        break
    
    if user_input not in options:  # Validate input
        continue
    
    bot_pick = options[random.randint(0, 2)]  # Random bot choice
    print("Bot picked", bot_pick)

    # Check win/loss and update scores
    if user_input == "rock" and bot_pick == "scissors":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and bot_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissors" and bot_pick == "paper":
        print("You Won!")
        user_wins += 1
    elif user_input == bot_pick:
        print("Tied")
    else:
        print("You Lost!")
        bot_wins += 1

    print(f"You won {user_wins} times.")
    print(f"Bot won {bot_wins} times.")
