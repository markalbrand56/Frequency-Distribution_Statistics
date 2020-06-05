#!/usr/bin/env python3.8.3
# _*_ coding: "utf-8" _*_

from various_calculations.poss_groups import possible_groups  # Function for possible groups
from various_calculations.limits import regular_limits
from various_calculations.frequencies import simple_frequencies
from various_calculations.frequencies import group_frequencies
from various_calculations.class_centers_m import class_center
from various_calculations.real_groups_m import get_real_groups
from various_calculations.poss_groups import force_groups  # Forcing a group
from various_calculations.exiting import exiting
from various_calculations.averages import average
# Working with decimals
from various_calculations.decimals_limits_freqs import one_decimal_limits
from various_calculations.decimals_limits_freqs import one_decimal_group_frequencies
from various_calculations.comprobations import has_decimals
from various_calculations.real_groups_m import decimal_real_groups
# Python Packages
import time
import collections

# TODO Give color to results
def frequency_distributions():
    """
    'Frequency Distributions' is meant to create the tables of simple and grouped frequencies for a set of numbers.
    The only thing the user needs is the data set.
    This program will calculate all possibilities of group arrangements for whole numbers. This can be controlled by the
    user, because the user can set a minimum of created groups and a maximum.
    If the previous step fails (the division between range and width is not a whole number) the user can force a width.
    This program also calculates real groups.
    """

    data = []  # This holds every raw number introduced by the user
    counter = 0  # Counter for how many numbers the user inputs
    timer = 0.1  # For the user to see each thing at a time. Data focused
    timer_groups = 0.05  # Timer for the rows of tables. Faster than data

    Instructions_FDS()

    time.sleep(1)
    main_loop = True  # To end the program when the user is ready.
    while main_loop:
        while True:  # To keep receiving data from the user
            try:
                num = float(input("  Enter a number: "))
                if num == 0.0:
                    break  # 0 is for finishing the input process
                elif num > 0:
                    counter += 1
                    data.append(num)
                else:
                    pass  # Negative numbers won't be added
            except ValueError:
                print(" Enter a number please.")  # With this exception raised, the user can continue entering data
        data = sorted(data)
        if len(data) <= 1:
            print("\nEnter more than one number, please. Try again.")
            print(" Exiting...")
            break

        verification = has_decimals(data)
        max_data = max(data)
        min_data = min(data)
        i_range = round((max_data - min_data), 1)  # Range
        data_average = average(data, counter)
        min_groups = int(input("\n  How many classes/groups do you at least need? "))
        max_groups = int(input("  How many classes/groups is your max? "))
        max_groups += 1  # This makes the max number of intervals actually be considered in the range.
        p_group_sizes = possible_groups(i_range, min_groups, max_groups)  # Possible group sizes in list of tuples (w,#)

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
        simple_frequencies(data)  # this will sort data by how many times it appears in the data collection
        print("\n-----------------------------------------------------------------\n")

        if p_group_sizes == 0:  # Exiting because the program can't do any more calculations
            print("An error occurred while calculating intervals...")
            forcing = input(" Do you want to choose a width to force the creation of groups? y/n ")
            if forcing == "y" or forcing == "Y":
                try:
                    forced_width = int(input("\nEnter the width you want to use: "))
                    if forced_width >= 0:
                        p_group_sizes = force_groups(i_range, forced_width)
                    else:
                        print("Invalid width")
                        exiting()
                except ValueError:
                    print("Enter a number")
            else:
                exiting()  # Without a possible group size it cannot continue with the calculations

        else:
            time.sleep(timer)
            for i in range(len(p_group_sizes)):
                time.sleep(timer)
                print("\n", i + 1, ". Possible groups' width: {} ".format(p_group_sizes[i][0]),
                      "  This will give you {} groups".format(p_group_sizes[i][1]))
        print("-----------------------------------------------------------------")

        if len(p_group_sizes) == 1:
            chs_option = 0  # Chosen amount of groups. Assigns (number_of_groups, divisor).
        else:
            chs_option = int(
                input("  Choose an option for the groups' size: "))  # Options to choose the width of the groups
            chs_option -= 1  # Match list index
            if chs_option in range(0, len(p_group_sizes)):
                pass
            else:
                print("\n   The option you entered doesn't exist. I assigned the second option.")
                chs_option = 1  # The len(p_group_sizes) has to be greater/equal than 1 for this to be evaluated
                pass

        chosen_group_size = p_group_sizes[chs_option][
            1]  # This is the variable for the amount of groups that should be crated.
        og_groups_width = int(p_group_sizes[chs_option][0])  # Variable for the untouched width
        gr_width = int(p_group_sizes[chs_option][0]) - 1  # This is the number that will be used to create the groups.
        print("\nGroup's width: ", og_groups_width)  # Information for the user
        print("Amount of groups:  ", chosen_group_size, "\n")

        if verification == 0:  # No decimals
            f_limits = regular_limits(minimum=min_data, maximum=max_data, width=gr_width)  # returns list with limits.
            result_gr_f = group_frequencies(f_limits, data)
        else:
            f_limits = one_decimal_limits(min_value=min_data, max_value=max_data, width=gr_width)  # list with  limits.
            result_gr_f = one_decimal_group_frequencies(f_limits, data)

        acc_g_f = 0  # Accumulated group's frequency

        time.sleep(timer)
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
        print("---------------------------Accumulated frequency: ", acc_g_f)

        if len(f_limits) == chosen_group_size:
            pass
        elif len(f_limits) > chosen_group_size:
            print("  \nThe groups created were more than the group size you chose by",
                  int(len(f_limits)) - int(chosen_group_size))  # Not always an error
        else:
            print("  \nThe groups created were less than the group size you chose by",
                  int(chosen_group_size) - int(len(f_limits)))  # Not always an error

        decison_rl_grps = input("  Do you want to show the real groups? y/n ")
        if decison_rl_grps.upper() == "Y":
            if verification == 0:
                real_groups = get_real_groups(f_limits)
                results_real_g_freq = one_decimal_group_frequencies(real_groups, data)
            else:
                real_groups = decimal_real_groups(f_limits)
                results_real_g_freq = one_decimal_group_frequencies(real_groups, data)

            print("-----------------------------------------------------------------")
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
            print("---------------------------Accumulated frequency: ", acc_r_g_f)
            # Need to enter the list without the frequencies

        exiting()


def Instructions_FDS():
    print("\n  INSTRUCTIONS:\nEnter one number at a time, and enter each instance of every number.")
    print("This program accepts numbers with up to 1 decimal position")
    print("When you finish, enter '0' to move to the next step")


if __name__ == "__main__":
    try:
        frequency_distributions()
    except KeyboardInterrupt:
        print("\nExiting...\n")
        exit
