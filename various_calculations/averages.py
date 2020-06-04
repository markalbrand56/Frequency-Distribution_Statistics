def average(data, count):
    average_v = 0
    for number in data:
        average_v = average_v + int(number)

    result = round((average_v / count), 4)
    return result


if __name__ == "__main__":
    testing_lst = [1, 2, 5, 5, 7, 8, 8, 8, 8, 9, 9, 11, 13, 15, 15, 16, 18, 18, 18, 20, 20, 22, 24, 25]
    print(average(testing_lst, 24))
