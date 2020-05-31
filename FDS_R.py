from s_package.get_rest_groups import get_other_groups
from s_package.exiting import exiting
from s_package.class_centers_m import class_center
from s_package.arithmetic_avrg import arithmetic_average


def fd_arithmetic_averages():
    """
    FDS_R is meant to be used when te table is given, but not the data.
    This means that the user should also have every grouped frequency.
    The program will calculate class centers, and the arithmetic average of the table (using the formula and deviation)
    """

    input_loop = True
    frequencies_loop = True

    while input_loop:
        try:
            first_lower = int(input("Whats the lower limit of the first group? "))
            first_upper = int(input("Whats the upper limit of the first group? "))
            amount_groups = int(input("How many groups does the table have? "))
            input_loop = False
        except ValueError:
            print("Enter a number, please")
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

    print(groups_frequencies)

    class_centers = []
    for limit in limits:
        center = class_center(limit)
        class_centers.append(center)
    print(class_centers)

    a_average = arithmetic_average(groups_frequencies, class_centers)
    print("Your arithmetic average is: {}".format(a_average))

    # TODO Arithmetic average with deviation


if __name__ == '__main__':
    fd_arithmetic_averages()
