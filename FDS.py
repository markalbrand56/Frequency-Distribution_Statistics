#!/usr/bin/env python3.8
#_*_ coding: "utf-8" _*_

from s_package.poss_groups import f_p_groups #Function for possible groups
from s_package.m_limits import limits
from s_package.reg_freq import simple_frequencies
from s_package.grp_freq import group_frequencies
from s_package.class_centers_m import class_center
from s_package.real_groups_m import get_real_groups

import collections

def frequency_distributions():
    data = [] #This holds every raw number introduced by the user
    counter = 0 #Counter for how many numbers the user inputs
    print("------------ v0.3.0-alpha ------------")
    print("\nInstructions:\nEnter one number at a time.\nWhen you finish, enter '0' to move to the next step\n")
    tr = True #To end the program when the user is ready.
    while tr:
        while True: #To keep recieving data from the user
            try:
                num = float(input("  Enter a number: ")) 
                if num == 0.0:
                    break #0 is for finishing the input process
                else:
                    counter += 1
                    data.append(num)
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
        p_group_sizes = f_p_groups(i_range,min_inter,max_inter) #Possible group sizes in a list of tuples (width, ammount of groups)
        
        print("\n\n\n\n-----------------------------------------------------------------")
        print ("Sorted data: ", data)
        print("Amount of data: ", counter)
        print("Range: ", i_range)
        
        print("-----------------------------------------------------------------")
        simple_frequencies(data) #this will sort data by how many times it appears in the data collection
        print("\n-----------------------------------------------------------------\n")

        if p_group_sizes == 0: #Exiting because the program can't do any more calculations, but giving the option to wait so the user can see the data that waas already calculated
            print("An error ocurred while calculating intervals...")
            while True:
                exiting = input("   Do you want to exit? y/n ")
                if exiting == "y" or exiting == "Y":
                    tr = False
                    break
                else:
                    print("   Ok, when you're ready exit by pressing 'CTRL'+'C' ")
                    while True:
                        pass
            #Without a possible group size it cannot continue with the calculations
        else:
            for i in range(len(p_group_sizes)):
                print("\n",i+1,". Possible groups' width: {} ".format(p_group_sizes[i][0]),"  This will give you {} groups".format(p_group_sizes[i][1]))
        print("-------")

        if len(p_group_sizes) == 1:
            chs_option = 0 #Chosen ammount of groups. Assigns (number_of_groups, divisor). Divisor is only used before to specify how was calculated the number of groups
        else:
            chs_option = int(input("  Choose an option for the groups' size: ")) #Options to choose the width of the groups
            chs_option -= 1 #Match list index
            if chs_option in range (0,len(p_group_sizes)):
                pass
            else:
                print("\n   The option you entered doesn't exist. I assigned the second option.") #Error while working with a width of 1
                chs_option = 1 #The len(p_group_sizes) has to be greater/equeal than 1 for this to be evaluated
                pass

        
        chosen_group_size = p_group_sizes[chs_option][1] #This is the variable for the ammount of groups that should be crated.
        og_groups_width = int(p_group_sizes[chs_option][0]) #Variable for the untouched width
        gr_width = int(p_group_sizes[chs_option][0]) - 1 #This is the number that will be used to create the groups. 
        print("\nGroup's width: ", og_groups_width ) #Information for the user
        print("Ammount of groups:  ", chosen_group_size, "\n")

        f_limits = limits(min=min_data,max=max_data,width=gr_width) #returns list with all the limits.
        result_gr_f = group_frequencies(f_limits, data)
        acc_g_f = 0 #Accumulated group's frequency
        
        print("-----------------------------------------------------------------")
        print("Your groups, and their frequencies are:\n")
        print("Groups  |  Class Center  |  Frequency  |  Accumulated Frequency")
        for freq in result_gr_f:
            center = class_center(freq[0])
            #Define a variable for the center, and make it an object for the class
            acc_g_f += freq[1] #accumulated group's frequency
            print (freq[0], "  |  ", center, "  |  ", freq[1], "   |   ", acc_g_f) #[0] holds the limits, [1] holds the frequency
        print ("---------------------------Accumulated frequency: ", acc_g_f)
    
        if len(f_limits) == chosen_group_size:
            pass
        elif len(f_limits) > chosen_group_size:
            print("  \nThe groups created were more than the group size you chose by", int(len(f_limits))-int(chosen_group_size)) #Not always an error
        else:
            print("  \nThe groups created were less than the group size you chose by", int(chosen_group_size)-int(len(f_limits))) #Not always an error

        decison_rl_grps = input("Do you want to show the real groups? y/n ")
        if decison_rl_grps.capitalize() == "Y":
            real_groups = get_real_groups(f_limits)
            results_real_g_freq = group_frequencies(real_groups, data)
            print("-----------------------------------------------------------------")
            print("Your real groups, and their frequencies are:\n")
            print("Real groups  |  Class Center  |  Frequency  |  Accumulated Frequency")
            acc_r_g_f = 0
            for freq in results_real_g_freq:
                center = class_center(freq[0])
                #Define a variable for the center, and make it an object for the class
                acc_r_g_f += freq[1] #accumulated group's frequency
                print (freq[0], "  |  ", center, "  |  ", freq[1], "   |   ", acc_r_g_f) #[0] holds the limits, [1] holds the frequency
            print ("---------------------------Accumulated frequency: ", acc_r_g_f)
            #Need to enter the list withou the frequencies

        while True:
            exiting = input("   Do you want to exit? y/n ")
            if exiting == "y" or exiting == "Y":
                tr = False
                break
            else:
                print("   Ok, when you're ready exit by pressing 'CTRL'+'C' ")
                while True:
                    pass


if __name__ == "__main__":
    try:
        frequency_distributions()
    except KeyboardInterrupt:
        print("\nExiting...\n")
        exit