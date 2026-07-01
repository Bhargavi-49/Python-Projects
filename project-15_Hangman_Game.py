import random
word_list = ["Mango", "Tiger", "apple", "lion", "programming"]
secret_word = random.choice(word_list).lower()
guessed_letters = []
for letter in secret_word:
    guessed_letters.append("_")
attempts = 10
while attempts > 0:
    print(" ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_letters[i] = guess
        print(" ".join(guessed_letters))
        if "_" not in guessed_letters:
            print("Congratulations! You guessed the word:", secret_word)
            break
    else:
        attempts -= 1
        print("Incorrect guess. Attempts left:", attempts)