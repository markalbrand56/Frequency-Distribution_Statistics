from s_package.get_rest_groups import get_other_groups
from s_package.exiting import exiting
from s_package.class_centers_m import class_center
from s_package.arithmetic_avrg import arithmetic_average


def arithmetic_averages_grouped_freq():
    """
    AV_G is meant to be used when te table is given, but not the data.
    This means that the user should also have every grouped frequency.
    The program will calculate class centers, and the arithmetic average of the table (using the formula and deviation)
    """

    input_loop = True
    frequencies_loop = True

    while input_loop:
        try:
            first_lower = int(input("Whats the lower limit of the first group? "))
            first_upper = int(input("Whats the upper limit of the first group? "))
            width = first_upper - first_lower + 1
            amount_groups = int(input("How many groups does the table have? "))
            input_loop = False
        except ValueError:
            print("Enter a number, please")

    if amount_groups == 0:
        print("You can't have 0 groups")
        exiting()

    limits = get_other_groups(first_lower, first_upper, amount_groups)
    print(limits)

    groups_frequencies = []
    for limit in limits:
        try:
            frequency = int(input("Enter the frequency for {} : ".format(limit)))
            group_freq = (limit, frequency)
            groups_frequencies.append(group_freq)
        except ValueError:
            print("Enter a number, please")
            exiting()

    print(groups_frequencies)

    class_centers = []
    for limit in limits:
        center = class_center(limit)
        class_centers.append(center)
    print(class_centers)

    a_average = arithmetic_average(groups_frequencies, class_centers)
    print("Your arithmetic average is: {}".format(a_average))

    # TODO Arithmetic average with deviation
    frequency_total = 0
    for element in groups_frequencies:
        freq = element[1]
        frequency_total += freq

    dev_loop = True
    while dev_loop:
        try:
            deviation_position = int(input("In what position do you want to set the center of the deviation? "))
            deviation_position -= 1
            dev_loop = False
        except ValueError:
            print("Enter a number please")

    deviations = []
    for num in range(len(groups_frequencies)):
        value = groups_frequencies[num][1]  # limit
        d = int(num - deviation_position)
        deviation = (value, d)
        deviations.append(deviation)

    print(deviations)

    deviations_subtotal = 0
    for element in deviations:
        f = element[0]
        d = element[1]
        result = f * d
        deviations_subtotal += result

    print(deviations_subtotal)
    print(frequency_total)
    print(class_centers[deviation_position])
    deviations_result = class_centers[deviation_position] + (deviations_subtotal / frequency_total) * width
    deviations_result = round(deviations_result, 2)
    print(deviations_result)


if __name__ == '__main__':
    arithmetic_averages_grouped_freq()
