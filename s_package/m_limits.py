#Module Limits

def limits(min,max,width): #Minimum value of the data set, maximun value of the data set, and groups' width.
    limits_lst = [] #Limits
    min -=1 
    for x in range((int(min)),int(max)):
        if min >= max: #Because later on the program increases min's value
            break 
        else:
            min += 1
            t_lim = (min, min + width) #Temporary limit. This will generate each limit.
            limits_lst.append(t_lim)
            min += width
    return (limits_lst)

if __name__ == "__main__":
    print(limits(34,96,7)," Testing")
    

