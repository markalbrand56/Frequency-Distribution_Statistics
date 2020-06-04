def possible_groups(rang, minimum=8, maximum=19):  # Function for possible groups
    possible_amounts_groups = []  # This holds every number that could divide the range, to calculate groups' width.
    results = []  # Holds each possible groups' width alongside with the number of groups it should produce.

    for x in range(minimum, maximum):  # Range of amount of groups
        possible_amounts_groups.append(x)

    for num_groups in possible_amounts_groups:
        if (rang % num_groups) == 0 and (rang / num_groups) != 1:
            groups_width = rang / num_groups
            results.append((groups_width, num_groups))
        else:
            pass

    if len(results) == 0:
        return 0  # Instead of an empty list. Easier to check
    else:
        return results


def force_groups(rang, width):
    results = []
    num_groups = float(rang / width)
    num_groups = round(num_groups, 2)  # If the user forces the creation of groups, the amount of groups will be decimal
    result = (width, num_groups)
    results.append(result)
    return results


if __name__ == "__main__":
    print(possible_groups(24), "Test")  # testing
    print(force_groups(23, 3))
