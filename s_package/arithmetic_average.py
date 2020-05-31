def Aritmetic_average(groups, centers):
    accumulated_freq = 0
    for i in range(len(groups)):
        freq = groups[i][1]
        accumulated_freq += freq
    subtotals = []
    for i in range(len(groups)):
        subtotal = groups[i][1] * centers[i]
        subtotals.append(subtotal)
    total = 0
    for subttl in subtotals:
        total += subttl

    arithmetic_average = total / accumulated_freq
    arithmetic_average = round(arithmetic_average, 2)
    return arithmetic_average



if __name__ == '__main__':
    test_grp = [((750, 799), 10), ((800, 849), 13), ((850, 899), 8), ((900, 949), 9)]
    test_centers = [774.5, 824.5, 874.5, 924.5]
    print(Aritmetic_average(test_grp, test_centers))