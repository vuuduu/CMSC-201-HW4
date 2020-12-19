"""
File:         hw4_part1.py
Author:       Vu Nguyen
Date:         9/30/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  Create a game where user enter rock, paper, or scissor.
              There's a random generate list w/ rock, paper or scissor.
              If the user win, lose or tie, inform then and continue
              asking until they type in stop.

"""
import sys
from random import choice, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

if __name__ == "__main__":

    the_choice = choice(['rock', 'paper', 'scissor'])
    user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
    while user_input != 'stop':
        if user_input == 'rock':
            if the_choice == 'rock':
                print('Both rock, there is a tie.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
            elif the_choice == 'paper':
                print('Paper covers rock, you lose.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
            else:
                print('Rock beat scissors, you win.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()

        elif user_input == 'paper':
            if the_choice == 'rock':
                print('Paper covers rock, you win.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
            elif the_choice == 'paper':
                print('Both paper, there is a tie.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
            else:
                print('Scissor cuts paper, you lose.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
        elif user_input == 'scissor':
            if the_choice == 'rock':
                print('Rock beat scissor, you lose')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
            elif the_choice == 'paper':
                print('Scissor cuts paper, you win.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()
            else:
                print('Both scissor, there is a tie.')
                user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()

        else:
            print('You need to select rock, paper or scissors')
            user_input = (input("Enter rock, paper, or scissors to play, stop to end. ").strip()).lower()