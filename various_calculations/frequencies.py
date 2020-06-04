def simple_frequencies(data: list):
    import collections
    import time
    counter = collections.Counter(data)  # Counts each appearance of each number. {(value, count), (value, count)...}

    print("\nValue ==> Frequency ==> Accumulated")
    accumulated = 0  # Accumulated frequency
    for key, value in counter.items():
        accumulated += value
        time.sleep(0.05)
        print("{}   |   {}   |   {}".format(key, value, accumulated))


def group_frequencies(limits, data):
    limits = list(limits)
    data = list(data)
    lst_gr_freq = []  # Limits will be added aside with their frequencies.[((1,3),5), ((4,6), 7), ((7,9), 2)]
    for limit in limits:
        gr_freq = 0
        lower = int(limit[0])  # Lower limit
        upper = int(limit[1]) + 1  # Upper limit. +1 Needed for ranges
        for num in data:
            if num in range(lower, upper):
                gr_freq += 1  # If the number is contained in the actual limit
        lst_gr_freq.append((limit, gr_freq))
    return lst_gr_freq


if __name__ == "__main__":
    testing_data = [1, 2, 5, 5, 7, 8, 8, 8, 8, 9, 9, 11, 13, 15, 15, 16, 18, 18, 18, 20, 20, 22, 24, 25]
    testing_data = sorted(testing_data)
    testing_lst = [(1, 3), (4, 6), (7, 9), (10, 12), (13, 15), (16, 18), (19, 21), (22, 24), (25, 27)]

    simple_frequencies(testing_data)
    print(len(testing_data))

    print("\n")

    results_gr_f = group_frequencies(testing_lst, testing_data)
    for result in results_gr_f:
        print(result)
    print("\n\n")

    testing2 = [(0.5, 3.5), (3.5, 6.5), (6.5, 9.5), (9.5, 12.5), (12.5, 15.5), (15.5, 18.5), (18.5, 21.5), (21.5, 24.5),
                (24.5, 27.5)]
    results_gr_f2 = group_frequencies(testing2, testing_data)
    for result in results_gr_f2:
        print(result)
