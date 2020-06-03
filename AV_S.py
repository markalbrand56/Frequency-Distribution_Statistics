from s_package.exiting import exiting
from time import sleep


def arithmetic_averages_simple_freq():
    data = []
    data_counter = 0
    main_loop = True
    while main_loop:
        while True:  # To keep receiving data from the user
            try:
                num = float(input("  Enter a number: "))
                if num == 0.0:
                    break  # 0 is for finishing the input process
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

        print(data_counter)
        print(data)

        data_frequencies = []
        for number in data:
            try:
                input_frequency = int(input("What is the frequency of: {} ? ".format(number)))
                frequency = (number, input_frequency)
                data_frequencies.append(frequency)
            except ValueError:
                print(" \nEnter a number, and try again ")
                exiting()
                # main_loop = False
                # break
        print(data_frequencies)

        for element in data_frequencies:
            freq = element[1]
            data_counter += freq

        cumulative_data = 0  # the sum of every number
        for element in data_frequencies:
            num = element[0]
            list_frequency = element[1]
            subtotal = num * list_frequency
            cumulative_data += subtotal

        print(cumulative_data)

        arithmetic_average = cumulative_data / data_counter
        arithmetic_average = round(arithmetic_average, 2)
        print("\nThe arithmetic average is: {}".format(arithmetic_average))

        # TODO Arithmetic averages with deviation

        dev_loop = True
        while dev_loop:
            try:
                deviation_position = int(input("In what position do you want to set the center of the deviation? "))
                deviation_position -= 1
                dev_loop = False
            except ValueError:
                print("Enter a number please")

        deviations = []
        for num in range(len(data_frequencies)):
            value = data_frequencies[num][1]
            d = int(num - deviation_position)
            deviation = (value, d)
            deviations.append(deviation)

        print(deviations)

        deviations_subtotal = 0
        for element in deviations:
            f = element[0]
            d = element[1]
            result = f * d
            deviations_subtotal += result

        print(deviations_subtotal)
        print(cumulative_data)
        deviations_result = data_frequencies[deviation_position][0] + (deviations_subtotal / data_counter)
        deviations_result = round(deviations_result, 2)
        print(deviations_result)

        main_loop = False


if __name__ == '__main__':
    try:
        arithmetic_averages_simple_freq()
    except KeyboardInterrupt:
        exit()
