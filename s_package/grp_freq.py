
def group_frequencies(limits, data):
    limits = list(limits)
    data = list(data)
    lst_gr_freq = [] #Here will be added the limits aside with their respective frequencies. Like [((1,3),5), ((4,6), 7), ((7,9), 2)] From 1-3 are 5 numbers
    for limit in limits:
        gr_freq = 0
        lower = int(limit[0]) #Lower limit
        upper = int(limit[1]) + 1 #Upper limit. +1 Needed for ranges
        for num in data:
            if num in range(lower,upper):
                gr_freq += 1 #If the number is contained in the actual limit
        lst_gr_freq.append((limit, gr_freq)) 
    return lst_gr_freq


def class_center(tupl): #Recieves the tuple of a limit
    lower_limit = tupl[0]
    upper_limit= tupl[1]
    center_ls = (int(lower_limit) + int(upper_limit) ) / 2
    return center_ls

