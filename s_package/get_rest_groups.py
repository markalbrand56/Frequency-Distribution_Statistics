def get_other_groups(lower_limit, upper_limit, amount_groups):
    """
    One group is needed to calculate the rest. It's also needed the amount of groups to create
    """
    width = upper_limit - lower_limit
    lower = lower_limit
    upper = upper_limit
    limits = []
    for i in range(amount_groups):
        limit = (lower, upper)
        limits.append(limit)
        lower = lower + width + 1
        upper = upper + width + 1
    return limits


if __name__ == '__main__':
    try:
        print(get_other_groups(60, 69, 6))
    except:
        print("error")
