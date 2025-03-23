# Number Guessing Game

A simple number guessing game where the user tries to guess a randomly chosen number between 1 and 100.

---

## Description

This project is a Python number guessing game. The user selects a difficulty level (easy or hard), which determines the 
number of attempts they have to guess the correct number. After each guess, the game provides feedback on whether the 
guess is too high or too low. The game continues until the user guesses the correct number or runs out of attempts.

---

## Features

- Two difficulty levels: Easy (10 attempts) and Hard (5 attempts). These are set as global variables.
- Randomly generated number between 1 and 100.
- Feedback on each guess (too high or too low).
- Option to play again after finishing a game.

---

## How to Play

1. Run the Python script.
2. Choose a difficulty level by typing 'easy' or 'hard'.
3. Guess the number within the allowed attempts.
4. Receive feedback on whether your guess is too high or too low.
5. Continue guessing until you find the correct number or run out of attempts.
6. Play again or exit the game.

---

## Installation

1. Clone the repository or download the Python script.
2. Ensure you have Python 3 installed.
3. Install the required dependencies using pip:
   '''bash
   pip install art
Run the script using the command:

bash
Copy
python main.py
Dependencies
Python 3.x

art module (install using pip install art).

random module (included in Python's standard library).

Example:
  Welcome to the Number Guessing Game!
  I'm thinking of a number between 1 and 100.
  Choose a difficulty. Type 'easy' or 'hard': hard
  You have 5 guesses.
  Please guess the number: 50
  Too High.
  You have 4 attempts remaining.
  Please guess the number: 25
  Too Low.
  You have 3 attempts remaining.
  Please guess the number: 37
  You guessed correctly!
  Do you want to play again? ('y'/'n'): n
  Goodbye!

License
This project is open-source and available under the MIT License.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Credits
Developed by Cameron Carlisle.

ASCII art provided by the art module.

Part of the Udemy 100 Days of Code course.

Contact
For questions or feedback, please contact:
Cameron Carlisle
Email: cameroncarlisle1992@gmail.com

