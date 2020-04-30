def limits(min,max,cls):
    i = cls - 1
    l_lst = []
    for x in range(int(min),int(max)):
        t_lim = (min,min + i)
        l_lst.append(t_lim)
        min += i
    return (l_lst)

#print(limits(1,10,3)) #TESTING
    

