"""
File:         hw4_part5.py
Author:       Vu Nguyen
Date:         9/30/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This is a guessing game, where it keep asking
              the user the number until they answer it right.
              Also, it'll tell the user whether their guess is
              too low or too high. 
"""
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":
    computer_guess = ra
    ndint(1, 100)
    user_guess = int(input("Guess a number between 1 and 100: " ))
    num_guesses = 1

    while user_guess != computer_guess:
        if user_guess > computer_guess:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

        user_guess = int(input("Guess a number between 1 and 100: "))
        num_guesses += 1

    print("You guessed the value! It took you", num_guesses, "steps\n")
