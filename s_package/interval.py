def finterval(rang,min=8,max=19):
    poss_inter = []
    inter_lst = []
    for x in range (min,max):
                poss_inter.append(x)
                if x in poss_inter:
                    pass
    for i in range(1,(int(rang))):   
        if rang / i in poss_inter:
            i_interval = rang / i 
            inter_lst.append((i_interval,i)) ## i
    #print(poss_inter) #testing
    #print(inter_lst) #testing
    if len(inter_lst) == 0:
        return 0
    else:
        return inter_lst


print(finterval(24)) #testing


    

