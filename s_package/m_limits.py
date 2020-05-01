def limits(min,max,clsi):
    i = clsi - 1
    l_lst = []
    min -=1 
    for x in range((int(min)),int(max)):
        if min >= max:
            break
        else:
            min += 1
            t_lim = (min,min + i)
            l_lst.append(t_lim)
            min += i
    return (l_lst)

#print(limits(1,24,12)) #TESTING
    

