def Has_Decimals (list: list):
    sum = 0
    for number in list:
        number = float(number)
        sum += number
    
    #int_i = int(sum)
    data_verification = float(sum - int(sum))
    if data_verification == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    testing_list = [1,2,3,4,5,6,7,8,9,10]
    testing_list2 = [1,2,3,4,5,6,7,8,9.1,10]
    print(Has_Decimals(testing_list))
    print(Has_Decimals(testing_list) == 1)
    print(Has_Decimals(testing_list2))
    print(Has_Decimals(testing_list2) == 1)