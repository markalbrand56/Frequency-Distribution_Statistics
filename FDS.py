#!/usr/bin/env python3.8
#_*_ coding: "utf-8" _*_

from s_package.interval import finterval
from s_package.m_limits import limits
from s_package.reg_freq import frequency
from s_package.grp_freq import group_frequencies

import collections

def frecuencias():
    data = []
    counter = 0
    print("\nInstructions:\nEnter one number at a time.\nWhen you finish, enter '0' to move to the next step\n")
    tr = True
    while tr:
        while True:
            try:
                var = float(input("  Enter a number: "))
                if var == 0.0:
                    break #0 is for finishing the input process
                else:
                    counter += 1
                    data.append(var)
            except ValueError:
                print(" Enter a number please.") #Even though this exception is raised, the user can continue to try to enter data
        data = sorted(data)
        if len(data) <= 1:
            print("\nEnter more than one number, please. Try again.")
            print("Exiting...")
            break

        max_data = max(data)
        min_data = min(data)
        i_range = max_data - min_data #Range
        min_inter = int(input("\n  How many classes/groups do you at least need? "))
        max_inter = int(input("  How many classes/groups is your max? "))
        max_inter += 1 #This makes the max number of intervals actually be considered in the range.
        p_group_sizes = finterval(i_range,min_inter,max_inter) #Possible group sizes in a list
        
        print("\n\n\n\n-----------------------------------------------------------------")
        print ("Sorted data: ", data)
        print("Amount of data: ", counter)
        print("\nRange: ", i_range)
        frequency(data) #this will sort data by how many times it appears in the data collection

        print("-----------------------------------------------------------------")
        if p_group_sizes == 0:
            print("An error ocurred while calculating intervals...")
            exit() #Without a possible group size it cannot continue with the calculations
        else:
            for i in range(len(p_group_sizes)):
                print("\n",i+1,". Possible group size: {} groups".format(p_group_sizes[i][0]),"  This was {} divided by".format(i_range), p_group_sizes[i][1])
        print("-------")

        if len(p_group_sizes) == 1:
            chs_interval = 0
        else:
            chs_interval = int(input("  Choose a group size: ")) #Options to choose the width of the gruops
            chs_interval -= 1
            if chs_interval in range (0,len(p_group_sizes)):
                pass
            else:
                print("\n   The option you entered doesn't exist. I assigned the second option.") #Error while working with a width of 1
                chs_interval = 1
                pass

        
        chosen_group_size = p_group_sizes[chs_interval][0] #Options to choose
        gr_width = int(p_group_sizes[chs_interval][1])-1 #C
        print("Group's width: ", gr_width, "\n")

        f_limits = limits(min=min_data,max=max_data,width=gr_width) #returns list with the limits.
        result_gr_f = group_frequencies(f_limits, data)
        acc_g_f = 0
        
        print("Your groups, and their frequencies are:")
        for freq in result_gr_f:
            acc_g_f += freq[1]
            print (freq[0], "  |  ", freq[1], "   |   ", acc_g_f)
        print ("---------------------------Accumulated frequency: ", acc_g_f)
    
        if len(f_limits) == chosen_group_size:
            pass
        elif len(f_limits) > chosen_group_size:
            print("  \nThe groups created were more than the group size you chose by", int(len(f_limits))-int(chosen_group_size)) #Not always an error
        else:
            print("  \nThe groups created were less than the group size you chose by", int(chosen_group_size)-int(len(f_limits))) #Not always an error

        while True:
            exiting = input("Do you want to exit? y/n ")
            if exiting == "y" or exiting == "Y":
                tr = False
                break
            else:
                print("Ok, when you're ready exit by pressing 'CTRL'+'C' ")
                while True:
                    pass


if __name__ == "__main__":
    try:
        frecuencias()
    except KeyboardInterrupt:
        print("\nExiting...\n")
        exit