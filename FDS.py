#!/usr/bin/env python3.8
#_*_ coding: utf8 _*_

from s_package.interval import finterval
from s_package.m_limits import limits
from s_package.reg_freq import frequency

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
                print(" Enter a number please.") #Ecen though this exception is raised, the user can continue to try to enter data
        data = sorted(data)
        if len(data) <= 1:
            print("\nEnter more than one number, please. Try again.")
            print("Exiting...")
            break
        ##reg_freq = collections.Counter(data) #this will sort data by how many times it appears in the data collection
        max_data = max(data)
        min_data = min(data)
        i_range = max_data - min_data
        min_inter = int(input("\n  How many classes/groups do you at least need? "))
        max_inter = int(input("  How many classes/groups is your max? "))
        max_inter += 1
        p_group_sizes = finterval(i_range,min_inter,max_inter)
        
        print("\n-----------------------------------------------------------------")
        print ("Sorted data: ", data)
        print("Amount of data: ", counter)
        frequency(data)
        ##rint ("Data, and how many times they repeat: ",reg_freq)
        print("\nRange: ", i_range)
        print("-----------------------------------------------------------------")
        if p_group_sizes == 0:
            print("An error ocurred while calculating intervals...")
        else:
            for i in range(len(p_group_sizes)):
                print("\n",i+1,". Possible group size: {} groups".format(p_group_sizes[i][0]),"  This was {} divided by".format(i_range), p_group_sizes[i][1])
        print("-------")
        
        chs_interval = int(input("  Choose a group size: ")) #Options to choose
        chs_interval -= 1
        if p_group_sizes[chs_interval]:
            pass
        else:
            print("Try again")
        
        chosen_group_size = p_group_sizes[chs_interval][0] #Options to choose
        class_int = int(p_group_sizes[chs_interval][1])-1
        print("Group's width: ", class_int)
        
        f_limits = limits(min=min_data,max=max_data,clsi=class_int)
        print("Your intervals are:\n ")
        for x in f_limits:
            print (" ", x)
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