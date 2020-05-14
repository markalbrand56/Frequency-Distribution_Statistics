def limits(min,max,clsi): #Clsi == Class Interval
    grp_wdth = clsi - 1 #Groups width is Class Interval - 1
    limits_lst = [] #Limits
    min -=1 
    for x in range((int(min)),int(max)):
        if min >= max: #Because later on the program increases min's value
            break 
        else:
            min += 1
            t_lim = (min, min + grp_wdth+1)
            limits_lst.append(t_lim)
            min += grp_wdth
    return (limits_lst)

if __name__ == "__main__":
    print(limits(1,24,12)," Testing")
    

