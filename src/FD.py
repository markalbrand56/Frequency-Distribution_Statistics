#!/usr/bin/env python3.8.3
# _*_ coding: "utf-8" _*_

# Various calculations
from src.various_calculations.poss_groups import possible_groups
from src.various_calculations.limits import regular_limits
from src.various_calculations.frequencies import simple_frequencies
from src.various_calculations.frequencies import group_frequencies
from src.various_calculations.class_centers_m import class_center
from src.various_calculations.real_groups_m import get_real_groups
from src.various_calculations.poss_groups import force_groups  # Forcing a group
from src.etc.exiting import exiting
from src.various_calculations.averages import average
from src.various_calculations.simple_frequencies_input import input_simple_frequencies
# Working with decimals
from src.various_calculations.decimals_limits_freqs import one_decimal_limits
from src.various_calculations.decimals_limits_freqs import one_decimal_group_frequencies
from src.various_calculations.comprobations import has_decimals
from src.various_calculations.real_groups_m import decimal_real_groups
# Python Packages
import time
# Extras
from src.etc.colors import Colors


def frequency_distributions():
    """
    'Frequency Distributions' is meant to create the tables of simple and grouped frequencies for a set of numbers.
    The only thing the user needs is the data set.
    This program will calculate all possibilities of group arrangements for whole numbers. This can be controlled by the
    user, because the user can set a minimum of created groups and a maximum.
    If the previous step fails (the division between range and width is not a whole number) the user can force a width.
    This program also calculates real groups.
    """

    counter = 0  # Counter for how many numbers the user inputs
    timer = 0.1  # For the user to see each thing at a time. Data focused
    timer_groups = 0.05  # Timer for the rows of tables. Faster than data
    text_color = Colors()

    Instructions_FDS()

    time.sleep(1)
    main_loop = True  # To end the program when the user is ready.
    while main_loop:
        data = input_simple_frequencies()  # This holds every raw number introduced by the user

        for number in data:
            counter += 1

        verification = has_decimals(data)
        max_data = max(data)
        min_data = min(data)
        i_range = round((max_data - min_data), 1)  # Range
        data_average = average(data, counter)
        try:
            min_groups = int(input("\n  How many classes/groups do you at least need? "))
            max_groups = int(input("  How many classes/groups is your max? "))
        except ValueError:
            text_color.RED()
            print("  Invalid values.")
            print("  I assigned 8 as the minimum amount and 18 as the maximum")
            min_groups = 8  # Default values
            max_groups = 18  # Default values
            text_color.RESET()

        max_groups += 1  # This makes the max number of intervals actually be considered in the range.
        p_group_sizes = possible_groups(i_range, min_groups, max_groups)  # Possible group sizes in list of tuples (w,#)

        text_color.GREEN()
        print("\n\n\n\n-----------------------------------------------------------------")
        time.sleep(timer)
        print("Sorted data: ", data)
        time.sleep(timer)
        print("Amount of data: ", counter)
        time.sleep(timer)
        print("Range: ", i_range)
        time.sleep(timer)
        print("Average: ", data_average)
        print("-----------------------------------------------------------------")
        time.sleep(timer)
        text_color.BLUE()
        simple_frequencies(data)  # this will sort data by how many times it appears in the data collection
        print("\n\n-----------------------------------------------------------------\n")

        if p_group_sizes == 0:  # Exiting because the program can't do any more calculations
            text_color.RED()
            print("An error occurred while calculating intervals...")
            forcing = input(" Do you want to choose a width to force the creation of groups? y/n ")
            text_color.RESET()
            if forcing == "y" or forcing == "Y":
                try:
                    forced_width = int(input("\nEnter the width you want to use: "))
                    if forced_width > 1:
                        p_group_sizes = force_groups(i_range, forced_width)
                    else:
                        text_color.RED()
                        print("Invalid width")
                        text_color.RESET()
                        exiting()
                except ValueError:
                    text_color.RED()
                    print("Enter a number")
                    text_color.RESET()
            else:
                exiting()  # Without a possible group size it cannot continue with the calculations

        else:
            text_color.GREEN()
            time.sleep(timer)
            for i in range(len(p_group_sizes)):
                time.sleep(timer)
                print("{}. Possible groups' width: {} ".format((i + 1), p_group_sizes[i][0]),
                      "  This will give you {} groups".format(p_group_sizes[i][1]))
        print("\n\n-----------------------------------------------------------------\n")
        text_color.RESET()

        if len(p_group_sizes) == 1:
            chs_option = 0  # Chosen amount of groups. Assigns (number_of_groups, divisor).
        else:
            chs_option = int(input("  Choose an option for the groups' size: "))  # Options for the width of the groups
            chs_option -= 1  # Match list index
            if chs_option in range(0, len(p_group_sizes)):
                pass
            else:
                print("\n   The option you entered doesn't exist. I assigned the second option.")
                chs_option = 1  # The len(p_group_sizes) has to be greater/equal than 1 for this to be evaluated
                pass

        chosen_group_size = p_group_sizes[chs_option][1]  # Variable for the amount of groups that should be crated.
        og_groups_width = int(p_group_sizes[chs_option][0])  # Variable for the untouched width
        gr_width = int(p_group_sizes[chs_option][0]) - 1  # This is the number that will be used to create the groups.

        text_color.GREEN()
        print("\nGroup's width: ", og_groups_width)  # Information for the user
        print("Amount of groups:  ", chosen_group_size, "\n")
        text_color.RESET()

        if verification == 0:  # No decimals
            f_limits = regular_limits(minimum=min_data, maximum=max_data, width=gr_width)  # returns list with limits.
            result_gr_f = group_frequencies(f_limits, data)
        else:
            f_limits = one_decimal_limits(min_value=min_data, max_value=max_data, width=gr_width)  # list with  limits.
            result_gr_f = one_decimal_group_frequencies(f_limits, data)

        acc_g_f = 0  # Accumulated group's frequency

        time.sleep(timer)
        text_color.BLUE()
        print("-----------------------------------------------------------------")
        print("Your groups, and their frequencies are:\n")
        print("Groups  |  Class Center  |  Frequency  |  Accumulated Frequency")
        for freq in result_gr_f:
            center = class_center(freq[0])
            center = round(center, 1)
            acc_g_f += freq[1]  # accumulated group's frequency
            time.sleep(timer_groups)
            print(freq[0], "  |  ", center, "  |  ", freq[1], "   |   ",
                  acc_g_f)  # [0] holds the limits, [1] holds the frequency
        print("-----------------------------------------------------------------\n")
        text_color.GREEN()
        print("Accumulated frequency: ", acc_g_f)

        text_color.RESET()
        if len(f_limits) == chosen_group_size:
            pass
        elif len(f_limits) > chosen_group_size:
            print("  \nThe groups created were more than the group size you chose by",
                  int(len(f_limits)) - int(chosen_group_size))  # Not always an error
        else:
            print("  \nThe groups created were less than the group size you chose by",
                  int(chosen_group_size) - int(len(f_limits)))  # Not always an error

        decision_real_groups = input("  Do you want to show the real groups? y/n ")
        if decision_real_groups.upper() == "Y":
            if verification == 0:
                real_groups = get_real_groups(f_limits)
                results_real_g_freq = one_decimal_group_frequencies(real_groups, data)
            else:
                real_groups = decimal_real_groups(f_limits)
                results_real_g_freq = one_decimal_group_frequencies(real_groups, data)

            text_color.BLUE()
            print("\n-----------------------------------------------------------------")
            print("Your real groups, and their frequencies are:\n")
            print("Real groups  |  Class Center  |  Frequency  |  Accumulated Frequency")
            acc_r_g_f = 0
            for freq in results_real_g_freq:
                center = class_center(freq[0])
                center = round(center, 1)
                # Define a variable for the center, and make it an object for the class
                acc_r_g_f += freq[1]  # accumulated group's frequency
                time.sleep(timer_groups)
                print(freq[0], "  |  ", center, "  |  ", freq[1], "   |   ",
                      acc_r_g_f)  # [0] holds the limits, [1] holds the frequency
            print("-----------------------------------------------------------------\n")
            text_color.GREEN()
            print("Accumulated frequency: ", acc_r_g_f)
            text_color.RESET()

        exiting()


def Instructions_FDS():
    print("\n  INSTRUCTIONS:\nEnter one number at a time, and enter each instance of every number.")
    print("This program accepts numbers with up to 1 decimal position.")
    print("When you finish, enter '0' to move to the next step.\n\n")


if __name__ == "__main__":
    try:
        frequency_distributions()
    except KeyboardInterrupt:
        print("\nExiting...\n")
        exit()
