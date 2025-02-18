This is a simple **Hangman** game implemented in Python. The game randomly selects a word from a predefined list and asks the player to guess the word letter by letter. The player has **6 attempts** to guess the correct word before losing.  

### **Key Features of the Code:**
- Uses `random.choice()` to select a word.
- Displays the word with underscores `_` for unguessed letters.
- Keeps track of guessed letters to avoid duplicate inputs.
- Reduces attempts if the guessed letter is incorrect.
- Ends when the player either correctly guesses the word or runs out of attempts.  

The game runs in a loop until the player wins or loses.
