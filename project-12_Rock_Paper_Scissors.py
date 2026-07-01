import random
game_options = ["Rock", "Paper", "Scissors"]
while True:
    user_choice = input("Enter your choice: ").strip().capitalize()
    computer_choice = random.choice(game_options)
    if user_choice == computer_choice:
        print("It is a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
         print("You win!")
    else:
        print("Computer wins!")
    print("Your_choice:",user_choice)
    print("computer_choice:",computer_choice)
    Replay = input("Do you want to play again?(yes/no):")
    if Replay == "no":
        print("Thanks for playing!")
        break
