from gtts import gTTS
from playsound import playsound
import os

while True:
    text = input("Enter text: ")

    if text.strip() == "":
        print("Please enter some text.")
        continue

    tts = gTTS(text=text, lang="en")
    tts.save("speech.mp3")

    playsound("speech.mp3")
    os.remove("speech.mp3")

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you!")
        break