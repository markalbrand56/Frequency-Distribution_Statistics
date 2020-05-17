def f_p_groups(rang,min=8,max=19): #Function for possible groups
    possible_ammounts_groups = [] #This holds every number that could divide the range, to calculate groups' width.
    results = [] #Holds each possible groups' width alongside with the number of groups it should produce.
    for x in range (min,max):
                possible_ammounts_groups.append(x)
                if x in possible_ammounts_groups:
                    pass
    for num_groups in possible_ammounts_groups: #Divisor and class' interval. Starts from 2 because the divisor needs to get substarcted 1 calculate groups' width
        if (rang % num_groups) == 0:
            groups_width = rang / num_groups 
            results.append((groups_width, num_groups)) 
    if len(results) == 0:
        return 0 #Instead of an empty list. Easier to check
    else:
        return results


if __name__ == "__main__":
    print(f_p_groups(24), "Test") #testing


    

