# Python-Projects

# Project-1:Simple Calculator Project

Description:
This project is a simple calculator developed using Python. It performs Addition, Subtraction, Multiplication, and Division using functions stored in a separate module.

Algorithm:

1. Start the program.
2. Input the first number from the user.
3. Input the second number from the user.
4. Display the operation menu:

   * Add
   * Subtract
   * Multiply
   * Divide
5. Read the user's choice.
6. If the choice is 1, call the add() function.
7. If the choice is 2, call the subtract() function.
8. If the choice is 3, call the multiply() function.
9. If the choice is 4, call the divide() function.
10. Display the result returned by the function.
11. If the choice is invalid, display an error message.
12. Stop the program.

Files:

1. Calcultor.py

   * Accepts user input.
   * Displays the menu.
   * Calls the required function.

2. calculator(2).py

   * Contains add(), subtract(), multiply(), and divide() functions.

Concepts Used:

* Functions
* Modules
* User Input
* Conditional Statements
* Return Statements

Expected Output:
The user enters two numbers and selects an operation. The calculator displays the result of the selected operation.

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/cf076831378a3181d62438bf26a4a5d4d5f94b93/Screenshot%202026-06-12%20175125.png)


# Project-2:Number Guessing Game

Description:

A simple Python game where the computer randomly selects a number between 1 and 100, and the user tries to guess it. The program provides hints whether the guessed number is too high or too low until the correct number is guessed.

Features

* Generates a random number between 1 and 100.
* Accepts user input for guesses.
* Gives feedback if the guess is too high or too low.
* Ends the game when the correct number is guessed.

Concepts Used

* Python `random` module
* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`for`)
* `break` statement

Algorithm

1. Import the `random` module.
2. Generate a random number between 1 and 100.
3. Ask the user to guess the number.
4. Compare the guessed number with the secret number.
5. If the guess is correct, display a success message and stop the game.
6. If the guess is higher than the secret number, display "Too High".
7. If the guess is lower than the secret number, display "Too Low".
8. Repeat the process until the correct number is guessed or the loop ends.

Sample Output

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/af870d87e6e54e071faacaeaabfbe57e982bb94c/Screenshot%202026-06-13%20110040.png)


# Project-3:Password Generator

Description: 

A simple Python project that generates a random password based on the length specified by the user. The password consists of uppercase letters, lowercase letters, numbers, and special characters.

Features

* User chooses the password length.
* Generates a random password.
* Includes letters, numbers, and special characters.
* Displays the generated password instantly.

Concepts Used:

* Python `random` module
* Strings
* User Input
* Loops (`for`)
* Variables
* `random.choice()`

Algorithm:

1. Import the `random` module.
2. Create a string containing letters, numbers, and special characters.
3. Ask the user for the desired password length.
4. Create an empty password string.
5. Repeat for the specified number of characters:

   * Select a random character from the character set.
   * Add it to the password.
6. Display the generated password.

## Sample Output

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/bcad65c8a670c7ec18261cdb36d10066849d8c12/Screenshot%202026-06-13%20112220.png)

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/63ac07aa979f89a22c41747f5a25e537f77b99e7/Screenshot%202026-06-13%20112247.png)


# Project-4:Student Grade calculator

Description:
This Python program calculates the total marks, average marks, and grade of a student based on marks entered for four subjects.

Features:
* Accepts marks for:

  * Maths
  * Physics
  * Social
  * English
* Calculates total marks.
* Calculates average marks.
* Assigns a grade based on the average score.

Grade Criteria:

| Average Marks | Grade |
| ------------- | ----- |
| 90 and above  | A     |
| 75 - 89       | B     |
| 60 - 74       | C     |
| 40 - 59       | D     |
| Below 40      | Fail  |

 Algorithm:

1. Input marks for four subjects.
2. Calculate the total marks.
3. Calculate the average marks by dividing the total by 4.
4. Display the total and average.
5. Check the average using conditional statements:

   * If average is 90 or above, assign Grade A.
   * If average is 75 or above, assign Grade B.
   * If average is 60 or above, assign Grade C.
   * If average is 40 or above, assign Grade D.
   * Otherwise, assign Fail.
6. Display the grade.

Sample Output:

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/b70ed741a1614bc3432a9f613ada57ce1ef2771d/Screenshot%202026-06-13%20141408.png)


# Project-5:To do List

Description:

This is a simple Task List Application built using Python. It allows users to add tasks, view tasks, delete tasks, and exit the program through a menu-driven interface.

Features:

* Add a new task
* View all tasks
* Delete an existing task
* Exit the application

Algorithm:

1. Create an empty list to store tasks.
2. Display a menu with available options.
3. Ask the user to enter a choice.
4. If the user selects **Add Task**, get the task name and store it in the list.
5. If the user selects **View Tasks**, display all tasks from the list.
6. If the user selects **Delete Task**, ask for the task name and remove it if it exists.
7. If the task is not found, display an error message.
8. If the user selects **Exit**, stop the program.
9. Repeat the process until the user chooses to exit.


Sample Output


![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/0ba2c32bf47a025df7a3fe13347ec7f059561c0f/Screenshot%202026-06-13%20165540.png)

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/0ba2c32bf47a025df7a3fe13347ec7f059561c0f/Screenshot%202026-06-13%20165603.png)

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/0ba2c32bf47a025df7a3fe13347ec7f059561c0f/Screenshot%202026-06-13%20165617.png)


# Project-4:Temperature Converter

Description:

A simple Python program that converts temperatures between Celsius, Fahrenheit, and Kelvin. This project is beginner-friendly and helps in understanding user input, conditional statements, arithmetic operations, and formatted output in Python.

Features:

* Convert Celsius to Fahrenheit
* Convert Fahrenheit to Celsius
* Convert Celsius to Kelvin
* Convert Kelvin to Celsius
* Simple menu-driven interface
* Handles invalid choices

Algorithm:

1. Start the program.
2. Display the temperature conversion menu.
3. Ask the user to enter a temperature value.
4. Ask the user to choose a conversion option.
5. Check the selected option:

   * If choice is `1`, convert Celsius to Fahrenheit.
   * If choice is `2`, convert Fahrenheit to Celsius.
   * If choice is `3`, convert Celsius to Kelvin.
   * If choice is `4`, convert Kelvin to Celsius.
6. Display the converted temperature.
7. If the user enters an invalid choice, display an error message.
8. End the program.

Conversion Formulas:

1.Celsius to Fahrenheit:

F = (C × 9/5) + 32

Fahrenheit to Celsius:

C = (F − 32) × 5/9

Celsius to Kelvin

K = C + 273.15

Kelvin to Celsius

C = K − 273.15



Sample Output:

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/a38c447eacc8f248c95330304db7a01762463c7e/Screenshot%202026-06-13%20181000.png)


# Project-7:Dice Rolling Simulator

Description:

A simple Python program that simulates rolling a six-sided dice. The user can choose to roll the dice multiple times or exit the game.

Features:

* Roll a dice and get a random number between 1 and 6.
* Continue rolling as many times as you want.
* Exit the game anytime by entering `no`.
* Handles invalid inputs.

Concepts Used:

* Python `random` module
* `while` loop
* Conditional statements (`if`, `elif`, `else`)
* User input
* String methods (`lower()`)

Algorithm:

1. Import the `random` module.
2. Display a welcome message.
3. Start an infinite loop.
4. Ask the user whether they want to roll the dice.
5. If the user enters `yes`:

   * Generate a random number between 1 and 6.
   * Display the rolled number.
6. If the user enters `no`:

   * Display a thank-you message.
   * Exit the loop.
7. Otherwise:

   * Display an invalid input message.
8. Repeat until the user chooses to exit.

Sample Output:

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/c95cc2490ae9af62e6f2d85f1b922feda12fb079/Screenshot%202026-06-15%20160354.png)



# Project-8:Currency Converter

Description:

A simple Python program that converts currency amounts between USD, INR, and EUR using predefined exchange rates.

Features:

* Convert USD to INR and INR to USD
* Convert EUR to INR and INR to EUR
* Convert USD to EUR and EUR to USD
* User-friendly input system
* Displays the converted amount instantly

Concepts Used:

* Variables
* User Input (`input()`)
* Data Type Conversion (`float()`)
* Conditional Statements (`if`, `elif`, `else`)
* String Methods (`upper()`)

Supported Conversions:

| From | To  | Exchange Rate        |
| ---- | --- | -------------------- |
| USD  | INR | 1 USD = 83 INR       |
| INR  | USD | 1 USD = 83 INR       |
| EUR  | INR | 1 EUR = 90 INR       |
| INR  | EUR | 1 EUR = 90 INR       |
| USD  | EUR | 1 USD = 0.85 EUR     |
| EUR  | USD | 1 EUR = 1 / 0.85 USD |

Algorithm:

1. Display the title "Currency Converter".
2. Ask the user to enter the amount.
3. Ask for the source currency.
4. Ask for the target currency.
5. Convert both currency inputs to uppercase.
6. Check the selected currencies using conditional statements.
7. Perform the appropriate conversion.
8. Display the converted amount.
9. If the conversion is not supported, show an error message.

Sample Output:

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/c95cc2490ae9af62e6f2d85f1b922feda12fb079/Screenshot%202026-06-15%20160551.png)


![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/c95cc2490ae9af62e6f2d85f1b922feda12fb079/Screenshot%202026-06-15%20160702.png)



# Project-9:Simple Quize Game

Description:

A simple Python quiz game that asks the user 5 questions and calculates the final score based on correct answers.

Features:

- 5 General Knowledge Questions
- User input for answers
- Score tracking system
- Displays final score out of 10

Questions Included

1. What is the Capital of India?
2. Which planet is closest to the Sun?
3. Sum of 8 + 3?
4. What is the largest ocean on Earth?
5. How many days are in a leap year?

How It Works

1. The program displays a question.
2. The user enters an answer.
3. If the answer is correct, 2 points are awarded.
4. The process repeats for all questions.
5. The final score is displayed at the end.

Algorithm:

1. Store questions and answers in variables.
2. Initialize score to 0.
3. Display each question.
4. Take user input.
5. Compare user input with the correct answer.
6. If correct:
   - Display "Correct!"
   - Add 2 points to the score.
7. Otherwise:
   - Display "Wrong!"
8. Repeat for all questions.
9. Display the final score.

Learning Concepts:

- Variables
- User Input
- Conditional Statements (`if` / `else`)
- String Comparison
- Score Tracking
- Basic Python Programming


Example:

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/240ad89432d86a81da276416acb637e55b1b90f1/Screenshot%202026-06-16%20175401.png)




# Project-10:ATM Stimulation

Description:

A beginner-friendly Python project that simulates basic ATM operations such as checking balance, depositing money, and withdrawing money.

Features:

* Check account balance
* Deposit money into the account
* Withdraw money from the account
* Exit the program
* Menu-driven interface

How It Works:

1. The program starts with an initial balance of 1000.
2. A menu is displayed with available options.
3. The user selects an option:

   * Check Balance
   * Deposit Money
   * Withdraw Money
   * Exit
4. The selected operation is performed.
5. The menu continues to appear until the user chooses to exit.

Algorithm:

1. Set the initial balance to 1000.
2. Start an infinite loop.
3. Display the ATM menu.
4. Take the user's choice as input.
5. If the choice is:

   * **1**: Display the current balance.
   * **2**: Ask for a deposit amount and add it to the balance.
   * **3**: Ask for a withdrawal amount and subtract it from the balance.
   * **4**: Exit the program.
6. If the user enters an invalid choice, display an error message.
7. Repeat until the user exits.

Concepts Used:

* Variables
* Loops (`while`)
* Conditional Statements (`if`, `elif`, `else`)
* User Input
* Basic Arithmetic Operations

Example Output:

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/240ad89432d86a81da276416acb637e55b1b90f1/Screenshot%202026-06-16%20180639.png)




#Project-11:Billing System

Description:

The Billing System is a simple Python project that generates bills for multiple items. Users can enter item details such as name, quantity, and price. The program calculates the subtotal, applies discounts and taxes, and displays the final bill amount. This project is useful for learning Python basics including loops, user input, variables, and arithmetic operations.

Features:

* Add multiple items to a bill
* Calculate item-wise amount
* Calculate subtotal automatically
* Apply discount percentage
* Apply tax percentage
* Display final bill amount
* Easy-to-use console interface

Algorithm:

1. Start the program.
2. Ask the user for the number of items.
3. Initialize subtotal as 0.
4. Repeat for each item:

   * Enter item name.
   * Enter quantity.
   * Enter price.
   * Calculate amount = quantity × price.
   * Add amount to subtotal.
   * Display item amount.
5. Display subtotal.
6. Ask for discount percentage.
7. Calculate discount amount.
8. Subtract discount from subtotal.
9. Ask for tax percentage.
10. Calculate tax amount.
11. Add tax to the discounted amount.
12. Display the final bill.
13. End the program.

Concepts Used:

* Variables
* Input and Output
* Loops (`for`)
* Arithmetic Operations
* User Input Handling
* Basic Billing Logi

Formula Used:

Item Amount = Quantity × Price

Discount Amount = (Subtotal × Discount) / 100

Amount After Discount = Subtotal - Discount Amount

Tax Amount = (Amount After Discount × Tax) / 100

Total Bill = Amount After Discount + Tax Amount

Example output:

![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/86bfe0cd5be6d6cace833f4e3509072002beb29f/Screenshot%202026-06-16%20184044.png)

# Project-12:Rock Paper Scissors

Description:

The Rock Paper Scissors Game is a simple Python console application where the user plays against the computer. The computer randomly selects either **Rock**, **Paper**, or **Scissors**, and the program compares both choices to determine the winner. After each round, the user can choose to play again or exit the game.

Features:

* Play against the computer.
* Computer makes a random choice every round.
* Detects win, loss, or tie.
* Displays both the user's and computer's choices.
* Replay option to play multiple rounds.
* Simple and beginner-friendly Python project.

Algorithm:

1. Import the `random` module.
2. Create a list containing **Rock**, **Paper**, and **Scissors**.
3. Start an infinite loop to allow multiple rounds.
4. Ask the user to enter their choice.
5. Randomly select the computer's choice from the list.
6. Compare the user's choice with the computer's choice.
7. Display whether the user wins, the computer wins, or the game is a tie.
8. Print both choices.
9. Ask the user if they want to play again.
10. If the user enters **"no"**, display a thank-you message and end the program. Otherwise, repeat the game.


Sample Output:



![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/bdb9d7828cf4b1dc2dce8eaf79e242d064089c7c/Screenshot%202026-06-18%20171346.png)

# Project-13:Countdown Timer

Description:

The Countdown Timer is a simple Python project that counts down from a user-specified time. The user enters the number of hours, minutes, and seconds, and the program converts the total time into seconds. It then displays the remaining time every second until the countdown reaches zero, after which it prints **"Time's Up"**.

Features:

* Accepts hours, minutes, and seconds as input.
* Converts the entered time into total seconds.
* Displays the countdown in real time.
* Updates every second using Python's `time` module.
* Prints **"Time's Up"** when the countdown ends.

Algorithm:

1. Import the `time` module.
2. Ask the user to enter hours, minutes, and seconds.
3. Convert the entered time into total seconds.
4. Start a loop that runs while the total time is greater than zero.
5. Display the remaining time in seconds.
6. Pause the program for one second using `time.sleep(1)`.
7. Decrease the total time by one second.
8. When the countdown reaches zero, display **"Time's Up"**.


Sample Output:


![watch demo](https://youtu.be/yElR6MWa6eY?si=Aj7b-zEuAsMWYhpM)



# Project-14:Alarm Clock

Description:

The Alarm Clock is a simple Python application that allows users to set an alarm by entering the desired hour, minute, and AM/PM. The program continuously checks the current system time and triggers an alarm sound when the specified time is reached.

Features:

* Set an alarm using a 12-hour time format (AM/PM).
* Displays the current system time every second.
* Continuously monitors the current time.
* Plays a beep sound when the alarm time matches the current time.
* Stops automatically after the alarm is triggered.

Algorithm:

1. Import the `datetime`, `time`, and `winsound` modules.
2. Display the alarm clock title.
3. Ask the user to enter the alarm hour, minute, and AM/PM.
4. Start an infinite loop.
5. Get the current system time.
6. Extract the current hour, minute, and AM/PM.
7. Display the current time on the screen.
8. Compare the current time with the user-defined alarm time.
9. If both times match:

   * Display **"Wake Up!"**
   * Play a beep sound using `winsound.Beep()`.
   * Exit the loop.
10. Otherwise, wait for one second and repeat the process.

Note:

* This project uses the `winsound` module, which is available only on Windows.
* On Linux or macOS, an alternative library such as `playsound` can be used.

Sample Output:

![watch demo](https://youtu.be/cC8SyR8PdwQ?si=c8KsQeNG8BurqQI0)

# Project-15:Hangman Game

Description:

The Hangman Game is a simple Python console application where the player tries to guess a randomly selected word one letter at a time. The program displays underscores for hidden letters and reveals them as the player makes correct guesses. The player has a limited number of attempts to guess the word.

Features:

* Randomly selects a word from a predefined list.
* Displays hidden letters using underscores (`_`).
* Reveals correctly guessed letters in their positions.
* Prevents guessing the same revealed letter multiple times.
* Limits the number of incorrect attempts.
* Displays a congratulatory message when the word is guessed successfully.

Algorithm:

1. Import the `random` module.
2. Create a list of words.
3. Randomly select one word from the list.
4. Convert the selected word to lowercase.
5. Create a list of underscores representing each letter in the word.
6. Set the number of allowed attempts.
7. Display the current progress of the word.
8. Ask the user to guess a letter.
9. If the guessed letter is in the secret word:

   * Reveal all matching letters.
   * Check if the entire word has been guessed.
   * If yes, display a success message and end the game.
10. If the guessed letter is incorrect:

    * Decrease the remaining attempts by one.
    * Display the number of attempts left.
11. Repeat the process until the word is guessed or all attempts are used.


Sample Output:




![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/bdb9d7828cf4b1dc2dce8eaf79e242d064089c7c/Screenshot%202026-07-01%20111442.png)

# Project-16:Typing Speed Test


## Description

The Typing Speed Test is a simple Python console application that measures a user's typing speed and accuracy. The program displays a sentence for the user to type, records the time taken to complete it, calculates the typing speed in **Words Per Minute (WPM)**, and determines the typing accuracy.

## Features

* Displays a sentence for the user to type.
* Measures the time taken to complete the sentence.
* Calculates typing speed in Words Per Minute (WPM).
* Calculates typing accuracy.
* Displays typing statistics after the test.
* Beginner-friendly Python project.

## Algorithm

1. Import the `datetime` module.
2. Create a list of sample sentences.
3. Select a sentence for the typing test.
4. Display the sentence to the user.
5. Record the start time.
6. Accept the user's typed input.
7. Record the end time.
8. Calculate the total time taken.
9. Count the number of words typed.
10. Calculate the typing speed using the formula:

    * **WPM = (Total Words × 60) ÷ Time Taken**
11. Compare the user's input with the original sentence.
12. Calculate the typing accuracy.
13. Display the time taken, words typed, typing speed, and accuracy.

Note:

* The current version calculates **100% accuracy only when the typed sentence exactly matches the original sentence**. Otherwise, the accuracy is reported as **0%**.
* Typing speed is calculated in **Words Per Minute (WPM)** based on the total number of words typed and the time taken.

Sample Output:

![watch demo](https://youtu.be/12qTQHxS3GY?si=qOJoEzgrQ3v49rb3)


# Project-17:QR Code Generator

Description:

The QR Code Generator is a simple Python application that creates a QR code from user input. The user can enter a website URL, phone number, text, or any other data, and the program generates a QR code image that is saved as **`qr_code.png`**.

Features:

* Generate QR codes from text, URLs, phone numbers, or other data.
* Uses the `qrcode` library to create QR codes.
* Saves the generated QR code as a PNG image.
* Simple and beginner-friendly Python project.
* Customizable QR code settings such as version, box size, border, and error correction.

Algorithm:

1. Import the `qrcode` library and the `Image` module from Pillow.
2. Ask the user to enter a URL, phone number, or text.
3. Create a `QRCode` object with the required settings.
4. Add the user's input to the QR code.
5. Generate the QR code.
6. Create the QR code image with a black foreground and white background.
7. Save the image as **`qr_code.png`**.
8. Display a success message.

 Sample Output:


Enter URL or number to generate QR code:
https://github.com



![image alt](https://github.com/Bhargavi-49/Python-Projects/blob/bdb9d7828cf4b1dc2dce8eaf79e242d064089c7c/Screenshot%202026-07-01%20120241.png)

Note:

* The generated QR code is saved in the current project directory as **`qr_code.png`**.
* The QR code can store text, URLs, phone numbers, email addresses, and other supported data.

# Project-18:Text to Speech Converter

Description:
The Text to Speech Converter is a simple Python application that converts user-entered text into speech. It uses the **Google Text-to-Speech (gTTS)** library to generate an audio file and the **playsound** library to play it. After playback, the temporary audio file is automatically deleted.

Features:

* Convert text into speech.
* Uses Google's Text-to-Speech (gTTS) service.
* Plays the generated speech automatically.
* Deletes the temporary audio file after playback.
* Allows users to convert multiple texts in a single session.
* Simple and beginner-friendly Python project.

Algorithm:

1. Import the required libraries (`gTTS`, `playsound`, and `os`).
2. Start an infinite loop.
3. Ask the user to enter text.
4. Check if the input is empty.

   * If empty, display an error message and ask again.
5. Convert the text into speech using the `gTTS` library.
6. Save the generated speech as **`speech.mp3`**.
7. Play the audio file using the `playsound` library.
8. Delete the temporary audio file using the `os` module.
9. Ask the user whether they want to continue.
10. If the user enters anything other than **"yes"**, display a thank-you message and exit the program.

Sample Output:

![watch demo](https://youtu.be/NgWb8zNnDCc?si=1iReGP6GwHsdY5Nv)


## Author

Bhargavi








































