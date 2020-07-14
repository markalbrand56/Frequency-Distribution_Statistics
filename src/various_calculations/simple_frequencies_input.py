def input_simple_frequencies(mode: int):
    # mode 1 = Each occurrence of the number
    # mode 2 = Table mode. 1 occurrence per value
    from src.etc.colors import Colors
    from src.etc.exiting import exiting

    text_color = Colors()
    data = []
    while True:
        try:
            num = float(input("  Enter a number: "))
            if num == 0.0:
                break  # 0 is for finishing the input process
            elif num in data and mode == 2:
                pass  # The numbers of the table should be given, not each value
            elif num > 0:
                data.append(num)
            else:
                pass  # Negative numbers won't be added
        except ValueError:
            text_color.RED()
            print(" Enter a number please.")  # With this exception raised, the user can continue entering data
            text_color.RESET()

    if len(data) <= 1:
        text_color.RED()
        print(" \nEnter more than one number, please. Try again.")
        exiting()
        text_color.RESET()

    return data
