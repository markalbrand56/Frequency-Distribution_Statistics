def finterval(rang,min=8,max=19):
    possible_ammounts_groups = []
    results = []
    for x in range (min,max):
                possible_ammounts_groups.append(x)
                if x in possible_ammounts_groups:
                    pass
    for num_groups in range(2,(int(rang))): #Divisor and class' interval. Starts from 2 because the divisor needs to get substarcted 1 calculate groups' width
        if rang / num_groups in possible_ammounts_groups:
            groups_width = rang / num_groups 
            results.append((groups_width, num_groups)) 
    if len(results) == 0:
        return 0 #Instead of an empty list. Easier to check
    else:
        return results


if __name__ == "__main__":
    print(finterval(24), "Test") #testing


    

