import datetime
sentences = [
    "Python is easy to learn",
    "Practice makes perfect",
    "Typing speed improves with regular practice"

]
sentence = sentences[0]
print("Type the following sentence as fast as you can:")
start_time = datetime.datetime.now()
user_input = input("type sentence: ")
end_time = datetime.datetime.now()
time_taken = (end_time - start_time).total_seconds()
total_words = len(user_input.split())
WPM = (total_words * 60 )/ time_taken
if user_input == sentence:
    correct_characters = len(sentence)
else:
    correct_characters = 0
total_characters = len(sentence)  
accuracy = (correct_characters / total_characters) * 100

print("Time Taken: ", round(time_taken, 2), "seconds")
print("Words Typed: ", total_words)
print("Typing Speed: ", round(WPM,2), "WPM")
print("Accuracy: ", accuracy, "%")