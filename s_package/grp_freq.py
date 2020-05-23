
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


if __name__ == "__main__":
    testing_lst = [(1, 3), (4, 6), (7, 9), (10, 12), (13, 15), (16, 18), (19, 21), (22, 24), (25, 27)]
    testing_data = [1,2,5,5,7,8,8,8,8,9,9,11,13,15,15,16,18,18,18,20,20,22,24,25]
    results = group_frequencies(testing_lst, testing_data)
    for result in results:
        print(result)


