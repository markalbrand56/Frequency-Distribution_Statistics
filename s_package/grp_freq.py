##({147.0: 3, 123.0: 2, 152.0: 2, 156.0: 2, 159.0: 2, 162.0: 2, 164.0: 2, 184.0: 2, 198.0: 2, 110.0: 1, 132.0: 1, 134.0: 1, 145.0: 1})


#test = [(110.0, 116.0), (117.0, 123.0), (124.0, 130.0), (131.0, 137.0), (138.0, 144.0), (145.0, 151.0)]
#test1 =  [110.0, 123.0, 123.0, 132.0, 134.0, 145.0, 147.0, 147.0, 151.0]

def group_frequencies(limits, data):
    limits = list(limits)
    data = list(data)
    lst_gr_freq = []
    for limit in limits:
        gr_freq = 0
        lower = int(limit[0])
        upper = int(limit[1]) + 1
        for num in data:
            if num in range(lower,upper):
                gr_freq += 1
        lst_gr_freq.append((limit, gr_freq)) 
    return lst_gr_freq


#print (group_frequencies(test, test1))

