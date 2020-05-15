def finterval(rang,min=8,max=19):
    poss_inter = []
    inter_lst = []
    for x in range (min,max):
                poss_inter.append(x)
                if x in poss_inter:
                    pass
    for num_groups in range(2,(int(rang))): #Divisor and class' interval. Starts from 2 because the divisor needs to get substarcted 1 calculate groups' width
        if rang / num_groups in poss_inter:
            groups_width = rang / num_groups 
            inter_lst.append((groups_width, num_groups)) 
    if len(inter_lst) == 0:
        return 0 #Instead of an empty list. Easier to check
    else:
        return inter_lst


if __name__ == "__main__":
    print(finterval(56), "Test") #testing


    

