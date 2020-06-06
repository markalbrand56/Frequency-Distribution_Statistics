def exiting():
    import time
    from etc.colors import Colors
    text_color = Colors()
    while True:
        text_color.RED()
        exiting_decision = input("  The program will exit. Do you want to wait? y/n ")
        if exiting_decision == "n" or exiting_decision == "N":
            time.sleep(1)
            text_color.RESET()
            exit()
        else:
            print("   Ok, when you're ready, exit by pressing 'CTRL'+'C' ")
            text_color.RESET()
            while True:
                pass
