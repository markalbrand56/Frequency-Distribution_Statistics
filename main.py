# Main Scripts
from FDS import frequency_distributions
from AV_G import arithmetic_averages_grouped_freq
from AV_S import arithmetic_averages_simple_freq
# Python modules
import os
from time import sleep
# Extras
from etc.colors import Colors


def main():
    os.system("cls")
    text_color = Colors()
    text_color.RED()
    print("\n------------ v0.4.0-alpha ------------\n")
    text_color.YELLOW()
    print("Choose an option:")
    print("1. Frequency Distributions")
    print("2. Arithmetic Averages for simple frequencies")
    print("3. Arithmetic Averages for grouped frequencies")
    print("4. Help")
    text_color.RESET()
    input_loop = True
    while input_loop:
        try:
            decision = int(input("---> "))
            if decision > 4:
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


def cls():
    sleep(0.05)
    os.system('cls' if os.name == 'nt' else 'clear')


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
