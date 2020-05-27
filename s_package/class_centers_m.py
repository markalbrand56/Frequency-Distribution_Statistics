def Class_center(tupl): #Recieves the tuple of a limit
    lower_limit = tupl[0]
    upper_limit= tupl[1]
    center_ls = (float(lower_limit) + float(upper_limit) ) / 2
    return center_ls



if __name__ == "__main__":
    print (Class_center((25, 27)))
    print (Class_center((25, 28)))