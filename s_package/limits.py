
def regular_limits(minimum, maximum, width):  # Minimum and maximum value of the data set, and groups' width.
    limits_lst = []  # Limits
    minimum -= 1
    for x in range((int(minimum)), int(maximum)):
        if minimum >= maximum:  # Because later on the program increases min's value
            break
        else:
            minimum += 1
            t_lim = (minimum, minimum + width)  # Temporary limit. This will generate each limit.
            limits_lst.append(t_lim)
            minimum += width
    return limits_lst


if __name__ == "__main__":
    print(regular_limits(34, 96, 7), " Testing")
