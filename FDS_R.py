"""
FDS_R is meant to be used when te table is given, but not the data.
This means that the user should also have every grouped frequency.
The program will calculate class centers, and the arithmetic average of the table (using the formula and deviation)
"""

from s_package.get_rest_groups import Get_other_groups
from s_package.exiting import Exiting


def arithmetic_average():
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
    limits = Get_other_groups(first_lower, first_upper, amount_groups)
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



if __name__ == '__main__':
    arithmetic_average()
