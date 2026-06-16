question1 = "What is the Capital Of India?"
answer1 = "New Delhi"
question2 = "Which planet is closet to Sun?"
answer2 = "Mercury"
question3 = "Sum of 8 + 3?"
answer3 = "11"
question4 = "What is the largest ocean on Earth?"
answer4 = "Pacific ocean"
question5 = "How many days are in a leap year?"
answer5 = "366"
score = 0

print(question1)
user_answer = input("Enter your answer1:")
if user_answer == answer1.lower():
    print("Correct!")
    score +=2
else:
    print("Wrong!")


print(question2)
user_answer = input("Enter your answer2:")
if user_answer == answer2.lower():
    print("Correct!")
    score +=2
else:
    print("Wrong!")


print(question3)
user_answer = input("Enter your answer3:")
if user_answer == answer3:
    print("Correct!")
    score +=2

print(question4)
user_answer = input("Enter your answer3:")
if user_answer == answer4.lower():
    print("Correct!")
    score +=2
else:
    print("Wrong!")

print(question5)
user_answer = input("Enter your answer3:")
if user_answer == answer5.lower():
    print("Correct!")
    score +=2
else:
    print("Wrong!")

print(f"Your final score is {score} out of 10")