"""
File:         hw4_part4.py
Author:       Vu Nguyen
Date:         9/30/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This programs take in the size of a board-game and then
              draw an alternating pattern.
"""

board_size = int(input("What size of board do you want? (between 1 and 50) ").strip())
symbol_list = ['\u2660', '\u2665', '\u2666', '\u2663']

for x in range(board_size):
    for y in range(board_size):
        if (x+y) % 4 == 0:
            print(symbol_list[0], end='')
        elif (x+y) % 4 == 1:
            print(symbol_list[1], end='')
        elif (x+y) % 4 == 2:
            print(symbol_list[2], end='')
        else:
            print(symbol_list[3], end='')
    print()
