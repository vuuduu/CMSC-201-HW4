"""
File:         hw4_part3.py
Author:       Vu Nguyen
Date:         9/30/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program draw a circle inside of a terminal with
              '*' based on the input radius.

"""

if __name__ == "__main__":
    radius = int(input("What is the radius? (between 0 and 20) "))
    diameter = radius * 2
    string = ''

    for x in range(diameter + 1):
        x -= radius
        for y in range(diameter + 1):
            y -= radius
            if (x**2 + y**2) <= (radius**2):
                print('*', end='')
            else:
                print(' ', end='')
        print()

