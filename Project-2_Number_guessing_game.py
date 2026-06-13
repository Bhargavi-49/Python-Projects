import random
secret_number = random.randint(1,100)

for number in range(secret_number):
    user_number = int(input("please choose a number:"))
    if user_number == secret_number:
        print("you guessed the number")
        break
    elif user_number > secret_number:
        print("The guess number is too high")
    elif user_number < secret_number:
        print("The guess number is too low ")
    else:
        print("Repeat the process")
