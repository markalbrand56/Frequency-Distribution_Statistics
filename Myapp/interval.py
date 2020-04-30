def range_iterval(list):
    i_range = max(list) - min(list)
    print (i_range)
    def interval(num):
        poss_inter = []
        inter_lst = []
        for i in range(1,(int(i_range))): #NEEDS REVISION    
             for x in range (8,19):
                poss_inter.append(x)

             if i_range / i in poss_inter:
                 i_interval = i_range / i 
                 inter_lst.append(i_interval)


        print (inter_lst)
    interval(i_range)