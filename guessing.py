#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: November 2020
# This program determines if the user guesses correctly

import math
import constants


def main():
    # This function obtains an input from the user and
    # determines if the user's guess is correct

    print("This program makes the user guess the number that"
          "the computer has saved.")
    print("")
    guess = int(input("Please input a number (from 0 to 9): "))
    if guess == constants.program_number:
        print("You guessed correctly!")


if __name__ == "__main__":
    main()
