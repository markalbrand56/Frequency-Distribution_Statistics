def finterval(rang,min=8,max=19):
    poss_inter = []
    inter_lst = []
    for x in range (min,max):
                poss_inter.append(x)
                if x in poss_inter:
                    pass
    for div in range(2,(int(rang))): #Divisor and class' interval. Starts from 2 because the divisor needs to get substarcted 1 calculate groups' width
        if rang / div in poss_inter:
            num_groups = rang / div 
            inter_lst.append((num_groups,div)) 
    if len(inter_lst) == 0:
        return 0 #Instead of an empty list. Easier to check
    else:
        return inter_lst


if __name__ == "__main__":
    print(finterval(45), "Test") #testing


    

