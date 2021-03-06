def average(data, count):
    average_v = 0
    for number in data:
        average_v = average_v + float(number)

    result = round((average_v / count), 4)
    return result


def arithmetic_average_groups(groups, centers):
    accumulated_freq = 0
    for number in range(len(groups)):
        freq = groups[number][1]
        accumulated_freq += freq
    subtotals = []
    for number in range(len(groups)):
        subtotal = groups[number][1] * centers[number]
        subtotals.append(subtotal)
    total = 0
    for subttl in subtotals:
        total += subttl

    resulting_average = total / accumulated_freq
    resulting_average = round(resulting_average, 2)
    return resulting_average


if __name__ == "__main__":
    testing_lst = [1, 2, 5, 5, 7, 8, 8, 8, 8, 9, 9, 11, 13, 15, 15, 16, 18, 18, 18, 20, 20, 22, 24, 25]
    print(average(testing_lst, 24))

    test_grp = [((750, 799), 10), ((800, 849), 13), ((850, 899), 8), ((900, 949), 9)]
    test_centers = [774.5, 824.5, 874.5, 924.5]
    print(arithmetic_average_groups(test_grp, test_centers))
