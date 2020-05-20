def f_p_groups(rang,min=8,max=19): #Function for possible groups
    possible_ammounts_groups = [] #This holds every number that could divide the range, to calculate groups' width.
    results = [] #Holds each possible groups' width alongside with the number of groups it should produce.
    
    for x in range (min,max): #Range of ammount of groups
        possible_ammounts_groups.append(x)

    for num_groups in possible_ammounts_groups: 
        if (rang % num_groups) == 0 and (rang/num_groups) != 1:
            groups_width = rang / num_groups 
            results.append((groups_width, num_groups))
        else:
            pass

    if len(results) == 0:
        return 0 #Instead of an empty list. Easier to check
    else:
        return results


if __name__ == "__main__":
    print(f_p_groups(24), "Test") #testing


    

