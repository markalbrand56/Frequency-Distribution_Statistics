def Get_real_groups(list):
    real_groups_lst = []
    difference = 0.5
    for group in list:
        lower = int(group[0]) - difference
        upper = int(group[1]) + difference
        real_groups_lst.append((lower, upper))
    return real_groups_lst


def Decimal_real_groups(list):
    real_groups_lst = []
    difference = 0.05
    for group in list:
        lower = round((float(group[0]) - difference), 2)
        upper = round((float(group[1]) + difference), 2)
        real_groups_lst.append((lower, upper))
    return real_groups_lst


if __name__ == "__main__":
    testing = [(1, 3), (4, 6), (7, 9), (10, 12)]
    print(Get_real_groups(testing))
