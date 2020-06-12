#!/usr/bin/env python3.8.3
# _*_ coding: "utf-8" _*_

# Author: Mark Albrand
# License: GNU General Public License v3.0

# Main Scripts
from src.FD import frequency_distributions  # Main functionality of the project as a whole
from src.AV_G import arithmetic_averages_grouped_freq  # Secondary functionality
from src.AV_S import arithmetic_averages_simple_freq  # Secondary functionality
# Python modules
import os
from time import sleep
# Extras
from src.etc.colors import Colors


def main():
    cls()
    text_color = Colors()

    text_color.RED()
    print("\n-------------- v0.4.1-alpha --------------\n")

    text_color.YELLOW()
    print("Choose an option:")
    print("1. Frequency Distributions")
    print("2. Arithmetic Averages for simple frequencies")
    print("3. Arithmetic Averages for grouped frequencies")
    print("4. Help")
    print("5. EXIT")
    text_color.RESET()

    input_loop = True
    while input_loop:
        try:
            decision = int(input("---> "))
            if decision > 5:
                raise ValueError
            else:
                input_loop = False
        except ValueError:
            text_color.RED()
            print("Enter a valid number")
            text_color.RESET()

    if decision == 1:
        cls()
        frequency_distributions()
    elif decision == 2:
        cls()
        arithmetic_averages_simple_freq()
    elif decision == 3:
        cls()
        arithmetic_averages_grouped_freq()
    elif decision == 4:
        help_functions()
        sleep(5)
        main()
    elif decision == 5:
        sleep(1)
        exit()
    else:
        pass


def cls():  # To clear the screen when entering a module.
    sleep(0.05)
    os.system('cls' if os.name == 'nt' else 'clear')  # Also helps to show colors in windows terminals.


def help_functions():
    try:
        function = int(input(" Choose one of the 3 previous options to get help with: "))
    except ValueError:
        print("Enter a valid number")

    if function == 1:
        return help(frequency_distributions)
    elif function == 2:
        return help(arithmetic_averages_simple_freq)
    elif function == 3:
        return help(arithmetic_averages_grouped_freq)
    else:
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
