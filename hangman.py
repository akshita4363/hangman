import random

def choose_random_word():
    words = ["hangman", "python", "programming", "computer", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_random_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")

    while True:
        print("\nAttempts left:", attempts_left)
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts_left -= 1
            print("Incorrect guess!")

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

        if attempts_left == 0:
            print("You've run out of attempts. The word was:", word)
            break

if __name__ == "__main__":
    hangman()
