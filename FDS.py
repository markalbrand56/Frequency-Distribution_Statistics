#!/usr/bin/env python3.8
#_*_ coding: utf8 _*_

import collections
from s_package.interval import finterval
from s_package.m_limits import limits

def frecuencias():
    data = []
    counter = 0
    print("\nInstructions:\nEnter one number at a time.\nWhen you finish, enter '0' to move to the next step\n")
    tr = True
    while tr:
        while True:
            var = float(input("  Enter a number: "))
            if var == 0.0:
                break #0 is for finishing the input process
            else:
                counter += 1
                data.append(var)
        data = sorted(data)
        countrep = collections.Counter(data) #this will sort data by how many times it appears in the data collection
        max_data = max(data)
        min_data = min(data)
        i_range = max_data - min_data
        min_inter = int(input("  How many intervals do you at least need? "))
        max_inter = int(input("  How many intervals is your max? "))
        max_inter += 1
        p_group_sizes = finterval(i_range,min_inter,max_inter)
        
        print("\n-------------------------------------------------------")
        print ("Sorted data: ", data)
        print("Amount of data: ", counter)
        print ("Data, and how many times they repeat: ",countrep)
        print("Range: ", i_range)
        print("-------------------------------------------------------")
        if p_group_sizes == 0:
            print("An error ocurred while calculating intervals...")
        else:
            for i in range(len(p_group_sizes)):
                print("\n",i+1,". Possible group size ",p_group_sizes[i][0],"  This was {} divided by".format(i_range), p_group_sizes[i][1])
        print("-------")
        
        chs_interval = int(input("  Choose a group size: "))
        chs_interval -= 1
        if p_group_sizes[chs_interval]:
            pass
        else:
            print("Try again")
        
        chosen_group_size = p_group_sizes[chs_interval][0] #NEEDS TO BE ABLE TO CHOOSE
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
            print("  \nThe groups created were less than the group size you chose by", int(chosen_group_size)-int(len(f_limits)))

        while True:
            exiting = input("Do you want to exit? y/n ")
            if exiting == "y" or exiting == "Y":
                tr = False
                break
            else:
                print("Ok, when you're ready exit by pressing 'CTRL'+'C' ")
                while True:
                    xax = 1


if __name__ == "__main__":
    try:
        frecuencias()
    except KeyboardInterrupt:
        print("Exiting...\n")
        exit