
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


def class_center(list):
    for group in list:
        center = ( int(group[0]) + int(group[1]) ) / 2
        #Define a way to put the class center to the side of each group.
