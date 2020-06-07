def has_decimals(data: list):
    subtotal = 0
    for number in data:
        number = float(number)
        subtotal += number

    data_verification = float(subtotal - int(subtotal))
    if data_verification == 0:
        return 0  # Data doesn't include decimals
    else:
        return 1  # Data includes decimals


if __name__ == "__main__":
    testing_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    testing_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9.5, 10]
    print(has_decimals(testing_list))
    print(has_decimals(testing_list) == 1)
    print(has_decimals(testing_list2))
    print(has_decimals(testing_list2) == 1)
