def exiting():
    import time
    while True:
        exiting_decision = input("  The program will exit. Do you want to wait? y/n ")
        if exiting_decision == "n" or exiting_decision == "N":
            time.sleep(1)
            exit()
        else:
            print("   Ok, when you're ready, exit by pressing 'CTRL'+'C' ")
            while True:
                pass
