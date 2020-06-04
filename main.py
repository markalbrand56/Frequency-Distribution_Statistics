from FDS import frequency_distributions
from AV_G import arithmetic_averages_grouped_freq
from AV_S import arithmetic_averages_simple_freq

import os
from time import sleep


def main():
    print("\n------------ v0.4.0-alpha ------------\n")

    print("Choose an option:")
    print("1. Frequency Distributions")
    print("2. Arithmetic Averages for simple frequencies")
    print("3. Arithmetic Averages for grouped frequencies")

    input_loop = True
    while input_loop:
        try:
            decision = int(input("---> "))
            if decision > 3:
                raise ValueError
            else:
                input_loop = False
        except ValueError:
            print("Enter a valid number")

    if decision == 1:
        cls()
        frequency_distributions()
    elif decision == 2:
        cls()
        arithmetic_averages_simple_freq()
    elif decision == 3:
        cls()
        arithmetic_averages_grouped_freq()


def cls():
    sleep(0.05)
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    main()
