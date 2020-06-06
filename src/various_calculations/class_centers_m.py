def class_center(group: tuple):  # Receives the tuple of a limit
    lower_limit = group[0]
    upper_limit = group[1]
    center_ls = (float(lower_limit) + float(upper_limit)) / 2
    return center_ls


if __name__ == "__main__":
    print(class_center((25, 27)))
    print(class_center((25, 28)))
