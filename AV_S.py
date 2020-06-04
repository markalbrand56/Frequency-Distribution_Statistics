from s_package.exiting import exiting


def arithmetic_averages_simple_freq():
    """
    AV_S is meant to be used when the table is given, but not the data itself.
    This means that the user should also have every frequency for each number.
    The program will calculate class centers, and the arithmetic average of the table (using the formula and deviation)
    """
    data = []
    data_counter = 0
    main_loop = True
    while main_loop:
        while True:  # To keep receiving data from the user
            try:
                num = float(input("  Enter a number: "))
                if num == 0.0:
                    break  # 0 is for finishing the input process
                elif num in data:
                    pass  # The numbers of the table should be given, not each value
                elif num > 0:
                    data.append(num)
                else:
                    pass  # Negative numbers won't be added
            except ValueError:
                print(" Enter a number please.")  # With this exception raised, the user can continue entering data
        data = sorted(data)
        if len(data) <= 1:
            print(" \nEnter more than one number, please. Try again.")
            print(" Exiting...")
            break

        data_frequencies = []
        for number in data:
            try:
                input_frequency = int(input("What is the frequency of: {} ? ".format(number)))
                frequency = (number, input_frequency)
                data_frequencies.append(frequency)
            except ValueError:
                print(" \nEnter a number, and try again ")
                exiting()

        for element in data_frequencies:
            freq = element[1]
            data_counter += freq

        cumulative_data = 0  # the sum of every number
        for element in data_frequencies:
            num = element[0]
            list_frequency = element[1]
            subtotal = num * list_frequency
            cumulative_data += subtotal

        arithmetic_average = cumulative_data / data_counter
        arithmetic_average = round(arithmetic_average, 2)
        print("\n  The arithmetic average is: {}\n".format(arithmetic_average))

        dev_loop = True  # Deviation loop
        while dev_loop:
            try:
                deviation_position = int(input("In what position do you want to set the center of the deviation? "))
                if deviation_position > len(data) or deviation_position < 0:
                    raise ValueError
                deviation_position -= 1  # List order
                dev_loop = False
            except ValueError:
                print("Enter a valid number please")

        deviations_list = []
        for num in range(len(data_frequencies)):
            value = data_frequencies[num][1]
            d = int(num - deviation_position)
            deviation = (value, d)
            deviations_list.append(deviation)

        deviations_subtotal = 0
        for element in deviations_list:
            f = element[0]
            d = element[1]
            result = f * d
            deviations_subtotal += result

        print("\n Value | Frequency | Deviation")
        for element in range(len(data)):
            individual_number = data_frequencies[element][0]
            individual_frequency = data_frequencies[element][1]
            individual_deviation = deviations_list[element][1]
            print(" {}  |  {}  |  {}".format(individual_number, individual_frequency, individual_deviation))

        deviations_result = data_frequencies[deviation_position][0] + (deviations_subtotal / data_counter)
        deviations_result = round(deviations_result, 2)
        print("\n  The result for the arithmetic average using deviation was: ", deviations_result)

        # TODO Clean code, and show results in a table

        main_loop = False


if __name__ == '__main__':
    try:
        arithmetic_averages_simple_freq()
    except KeyboardInterrupt:
        exit()
