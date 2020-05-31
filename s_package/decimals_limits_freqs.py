# Together for testing
def one_decimal_limits(min_value, max_value, width):  # Minimum and maximum value of the data set, and groups' width.
    limits_lst = []  # Limits
    for x in range((int(min_value)), int(max_value)):
        if min_value >= max_value:  # Because later on the program increases min's value
            break
        else:
            t_lim = (min_value, min_value + width)  # Temporary limit. This will generate each limit.
            min_value = round((min_value + 0.1), 1)
            limits_lst.append(t_lim)
            min_value += width
    return limits_lst


def one_decimal_group_frequencies(limits, data):  # Real groups and Decimals
    limits = list(limits)
    data = list(data)
    lst_gr_freq = []  # Limits will be added aside with their respective frequencies.[((1,3),5), ((4,6), 7), ((7,9), 2)]
    for limit in limits:
        gr_freq = 0
        lower = float(limit[0]) - 0.05  # Lower limit- -0.05 Needed for comparisons
        upper = float(limit[1]) + 0.05  # Upper limit. +0.05 Needed for comparisons
        for num in data:
            num = round(num, 1)
            if lower < num < upper:
                gr_freq += 1  # If the number is contained in the actual limit
            else:
                pass
        lst_gr_freq.append((limit, gr_freq))
    return lst_gr_freq


if __name__ == "__main__":
    limits_testing = one_decimal_limits(1.2, 24.1, 3)
    print(limits_testing)
    testing_data = [1.2, 1.5, 2.0, 2.5, 2.6, 3.0, 3.5, 4.0, 4.5, 5.0, 7.0, 7.0, 8.2, 8.2, 8.5, 8.8, 9.9, 10.1, 10.7,
                    11.0, 12.0, 13.0, 15.0, 15.0, 16.0, 16.1, 17.5, 17.7, 17.7, 17.8, 18.1, 18.5, 20.0, 21.0, 21.0,
                    22.0, 23.5, 24.0, 24.0, 24.1]
    testing_data = sorted(testing_data)
    print(len(testing_data))

    print("\nTest1")
    results_gr_f = one_decimal_group_frequencies(limits_testing, testing_data)
    for result in results_gr_f:
        print(result)
    print("\n\n")

    print("\nTest1")
    testing_data2 = [1, 2, 5, 5, 7, 8, 8, 8, 8, 9, 9, 11, 13, 15, 15, 16, 18, 18, 18, 20, 20, 22, 24, 25]
    testing2 = [(0.5, 3.5), (3.5, 6.5), (6.5, 9.5), (9.5, 12.5), (12.5, 15.5), (15.5, 18.5), (18.5, 21.5), (21.5, 24.5),
                (24.5, 27.5)]
    results_gr_f2 = one_decimal_group_frequencies(testing2, testing_data2)
    for result in results_gr_f2:
        print(result)
