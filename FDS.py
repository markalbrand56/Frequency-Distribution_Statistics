#!/usr/bin/env python3.8.3
# _*_ coding: "utf-8" _*_

from s_package.poss_groups import Possible_groups  # Function for possible groups
from s_package.limits import Limits
from s_package.frequencies import Simple_frequencies
from s_package.frequencies import Group_frequencies
from s_package.class_centers_m import Class_center
from s_package.real_groups_m import Get_real_groups
from s_package.poss_groups import Force_groups  # Forcing a group
from s_package.exiting import Exiting
from s_package.average import Average
# Working with decimals
from s_package.decimals_limits_freqs import One_Decimal_Limits
from s_package.decimals_limits_freqs import One_Decimal_Group_frequencies
from s_package.comprobations import Has_Decimals
from s_package.real_groups_m import Decimal_real_groups
# Python Packages
import time
import collections


def frequency_distributions():
    print("------------ v0.3.0 ------------")
    data = []  # This holds every raw number introduced by the user
    counter = 0  # Counter for how many numbers the user inputs
    timer = 0.1  # For the user to see each thing at a time. Data focused
    timer_groups = 0.05  # Timer for the rows of tables. Faster than data
    print(
        "\nInstructions:\nEnter one number at a time. This program accepts numbers with up to 1 decimal position\nWhen you finish, enter '0' to move to the next step\n")
    time.sleep(1)
    tr = True  # To end the program when the user is ready.
    while tr:
        while True:  # To keep recieving data from the user
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
                print(" Enter a number please.")  # Even though this exception is raised, the user can continue entering data
        data = sorted(data)
        if len(data) <= 1:
            print("\nEnter more than one number, please. Try again.")
            print(" Exiting...")
            break

        verification = Has_Decimals(data)
        max_data = max(data)
        min_data = min(data)
        i_range = round((max_data - min_data), 1)  # Range
        average = Average(data, counter)
        min_inter = int(input("\n  How many classes/groups do you at least need? "))
        max_inter = int(input("  How many classes/groups is your max? "))
        max_inter += 1  # This makes the max number of intervals actually be considered in the range.
        p_group_sizes = Possible_groups(i_range, min_inter, max_inter)  # Possible group sizes in a list of tuples (width, ammount of groups). Decimals will have to force a width

        print("\n\n\n\n-----------------------------------------------------------------")
        time.sleep(timer)
        print("Sorted data: ", data)
        time.sleep(timer)
        print("Amount of data: ", counter)
        time.sleep(timer)
        print("Range: ", i_range)
        time.sleep(timer)
        print("Average: ", average)
        print("-----------------------------------------------------------------")
        time.sleep(timer)
        Simple_frequencies(data)  # this will sort data by how many times it appears in the data collection
        print("\n-----------------------------------------------------------------\n")

        if p_group_sizes == 0:  # Exiting because the program can't do any more calculations
            print("An error occurred while calculating intervals...")
            forcing = input(" Do you want to choose a width to force the creation of groups? y/n ")
            if forcing == "y" or forcing == "Y":
                try:
                    forced_width = int(input("\nEnter the width you want to use: "))
                    if forced_width >= 0:
                        p_group_sizes = Force_groups(i_range, forced_width)
                    else:
                        print("Invalid width")
                        Exiting()
                except ValueError:
                    print("Enter a number")
            else:
                Exiting()  # Without a possible group size it cannot continue with the calculations

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

        chosen_group_size = p_group_sizes[chs_option][1]  # This is the variable for the amount of groups that should be crated.
        og_groups_width = int(p_group_sizes[chs_option][0])  # Variable for the untouched width
        gr_width = int(p_group_sizes[chs_option][0]) - 1  # This is the number that will be used to create the groups.
        print("\nGroup's width: ", og_groups_width)  # Information for the user
        print("Amount of groups:  ", chosen_group_size, "\n")

        if verification == 0:  # No decimals
            f_limits = Limits(minimum=min_data, maximum=max_data, width=gr_width)  # returns list with all the limits.
            result_gr_f = Group_frequencies(f_limits, data)
        else:
            f_limits = One_Decimal_Limits(min=min_data, max=max_data, width=gr_width)  # list with all the limits.
            result_gr_f = One_Decimal_Group_frequencies(f_limits, data)

        acc_g_f = 0  # Accumulated group's frequency

        time.sleep(timer)
        print("-----------------------------------------------------------------")
        print("Your groups, and their frequencies are:\n")
        print("Groups  |  Class Center  |  Frequency  |  Accumulated Frequency")
        for freq in result_gr_f:
            center = Class_center(freq[0])
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
                real_groups = Get_real_groups(f_limits)
                results_real_g_freq = One_Decimal_Group_frequencies(real_groups, data)
            else:
                real_groups = Decimal_real_groups(f_limits)
                results_real_g_freq = One_Decimal_Group_frequencies(real_groups, data)

            print("-----------------------------------------------------------------")
            print("Your real groups, and their frequencies are:\n")
            print("Real groups  |  Class Center  |  Frequency  |  Accumulated Frequency")
            acc_r_g_f = 0
            for freq in results_real_g_freq:
                center = Class_center(freq[0])
                center = round(center, 1)
                # Define a variable for the center, and make it an object for the class
                acc_r_g_f += freq[1]  # accumulated group's frequency
                time.sleep(timer_groups)
                print(freq[0], "  |  ", center, "  |  ", freq[1], "   |   ",
                      acc_r_g_f)  # [0] holds the limits, [1] holds the frequency
            print("---------------------------Accumulated frequency: ", acc_r_g_f)
            # Need to enter the list without the frequencies

        Exiting()


if __name__ == "__main__":
    try:
        frequency_distributions()
    except KeyboardInterrupt:
        print("\nExiting...\n")
        exit
