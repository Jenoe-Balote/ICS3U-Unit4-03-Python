#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program runs a factorial loop for positive integers

import string


def main():
    # this function uses a while loop

    # this function runs the "factorial loop" program
    # input
    print("Welcome!")
    number_integer = str(input("Please enter a positive integer: "))

    # process and output
    try:
        number_integer = int(number_integer)
        if number_integer >= 0:
            for loop_counter in range(number_integer + 1):
                total = loop_counter ** 2
                print("{0}² = {1}".format(loop_counter, total))
        elif number_integer < 0:
            print("That integer is a negative number!")
    except Exception:
        print("{0} is invalid data.".format(number_integer))
    finally:
        print("")
        print("Thanks for participating!")


if __name__ == "__main__":
    main()
