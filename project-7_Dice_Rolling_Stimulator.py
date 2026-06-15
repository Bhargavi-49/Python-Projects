import random
print("Dice Rolling Simulator!")
while True:
    user_input = input("Roll the dice? (yes/no): ")
    if user_input.lower() == "yes":

        number_of_dice= random.randint(1, 6)
        print("Dice rolled:", number_of_dice)
    elif user_input.lower() == "no":
        print("Thanks for playing!")    
        break
    else:
        print("Invalid input")