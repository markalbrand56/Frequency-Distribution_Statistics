# Calculations
from various_calculations.get_rest_groups import get_other_groups
from various_calculations.class_centers_m import class_center
from various_calculations.arithmetic_avrg import arithmetic_average_groups

# Extras
from time import sleep
from etc.colors import Colors
from etc.exiting import exiting


# TODO Give color to results
def arithmetic_averages_grouped_freq():
    """
      'Arithmetic Averages for grouped frequencies' is meant to be used when a table of grouped frequencies is given,
    but not the data itself.
      This means that the user should have: Groups and the Frequency for each group.
      The program will calculate class centers, and the arithmetic average of the table (using the standard formula and
    deviation)
    """

    input_loop = True
    timer_groups = 0.05
    text_color = Colors()

    Instructions_AVG()

    while input_loop:
        try:
            first_lower = int(input("Whats the lower limit of the first group? "))
            first_upper = int(input("Whats the upper limit of the first group? "))
            width = first_upper - first_lower + 1
            amount_groups = int(input("How many groups does the table have? "))
            input_loop = False
        except ValueError:
            text_color.RED()
            print("Enter a number, please")
            text_color.RESET()

    if amount_groups == 0 or amount_groups == 1:
        print("You can't have {} groups".format(amount_groups))
        exiting()
    else:
        pass

    limits = get_other_groups(first_lower, first_upper, amount_groups)

    groups_frequencies = []
    for limit in limits:
        try:
            frequency = int(input("Enter the frequency for {} : ".format(limit)))
            group_freq = (limit, frequency)
            groups_frequencies.append(group_freq)
        except ValueError:
            text_color.RED()
            print("Enter a number, please")
            text_color.RESET()
            exiting()

    class_centers = []
    for limit in limits:
        center = class_center(limit)
        class_centers.append(center)
    text_color.GREEN()
    a_average = arithmetic_average_groups(groups_frequencies, class_centers)
    print("  The arithmetic average is: {}".format(a_average))
    text_color.RESET()
    frequency_total = 0
    for element in groups_frequencies:
        freq = element[1]
        frequency_total += freq

    dev_loop = True  # Deviations loop
    while dev_loop:
        try:
            deviation_position = int(input("In what position do you want to set the center of the deviation? "))
            if deviation_position > len(limits) or deviation_position < 0:
                raise ValueError
            deviation_position -= 1
            dev_loop = False
        except ValueError:
            text_color.RED()
            print(" Enter a valid number please")
            text_color.RESET()

    deviations = []
    for num in range(len(groups_frequencies)):
        value = groups_frequencies[num][1]  # frequency
        d = int(num - deviation_position)
        deviation = (value, d)
        deviations.append(deviation)

    deviations_subtotal = 0
    for element in deviations:
        f = element[0]
        d = element[1]
        result = f * d
        deviations_subtotal += result
    text_color.BLUE()
    print("\n Group | Frequency | Deviation")
    for element in range(len(class_centers)):
        individual_group = groups_frequencies[element][0]
        individual_frequency = groups_frequencies[element][1]
        individual_deviation = deviations[element][1]
        sleep(timer_groups)
        print(" {}  |  {}  |  {}".format(individual_group, individual_frequency, individual_deviation))

    deviations_result = class_centers[deviation_position] + (deviations_subtotal / frequency_total) * width
    deviations_result = round(deviations_result, 2)
    text_color.GREEN()
    print("\n  The result of the arithmetic average using deviation is: {}".format(deviations_result))
    text_color.RESET()

    exiting()

def Instructions_AVG():
    print("\n  INSTRUCTIONS:")
    print("Enter one number at a time. \nYou only need to enter the first group of the table. ")
    print("You will enter the frequencies after the table is generated.")
    print("When you reach the section for Arithmetic Average with deviation, the position refers to the row number\n\n")


if __name__ == '__main__':
    arithmetic_averages_grouped_freq()
