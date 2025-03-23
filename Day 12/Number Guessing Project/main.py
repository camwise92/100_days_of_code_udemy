"""
Number Guessing Game (Day 12 of Udemy 100 Days of Code)

File: main.py
Description: A number guessing game where the user tries to guess a randomly chosen number between 1 and 100.
Author: Cameron Carlisle
Date created: 23/03/2024
Last modified: 23/03/2024
Version: 1.0

This script allows users to play a number guessing game with two difficulty levels (easy and hard).
The user has a limited number of attempts to guess the correct number, and feedback is provided after each guess.

Usage:
1. Choose a difficulty level (easy or hard).
2. Guess the number within the allowed attempts.
3. Receive feedback on whether the guess is too high or too low.
4. Continue guessing until the correct number is found or attempts run out.
5. Game can then be replayed or user can quit.

Dependencies:
- Requires the 'art' module for ASCII art display.
- Requires the 'random' module for generating random numbers.

Contact: cameroncarlisle1992@gmail.com
"""
import art
import random
import sys

EASY = 10
HARD = 5

def main():
    """ Prints logo, initialises game play and allows for game to be replayed at the end of each session. """
    while True:
        print(art.logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        game(level())
        while True:
            play_again = input("Do you want to play again? ('y'/'n'): ").lower().strip()
            if play_again == 'n':
                sys.exit("Goodbye!")
            elif play_again == 'y':
                main()
            else:
                print("Please input valid response")

def level():
    """ Inputs what difficulty user chooses and returns number of guesses allowed based upon difficulty level. """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    if difficulty == 'hard':
        guess = HARD
        print(f"You have {guess} guesses.")
        return guess
    else:
        guess = EASY
        print(f"You have {guess} guesses.")
        return guess

def game(guess):
    """
    Chooses a random number between 1 and 100. The user can guess and a comparison is made between user's guess and number (too high/low).
    Number of remaining guesses left is displayed to user, until they run out of guesses or guess correctly.
    """
    chosen_num = random.randint(1, 100)
    # print(f"CHEATSHEET Chosen num is {chosen_num}")

    while True:
        try:
            user_guess = int(input("Please guess the number: "))
            if user_guess == chosen_num:
                print("You guessed correctly!")
                break
            else:
                guess -= 1
                if user_guess > chosen_num:
                    print("Too High.")
                else:
                    print("Too Low.")
                print(f"You have a {guess} attempts remaining.")
                if guess == 0:
                    print("You've ran out of guesses.")
                    break
        except ValueError:
            print("Please enter valid digit.")

if __name__ == "__main__":
    main()