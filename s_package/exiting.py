def exiting():
    import time
    while True:
        exiting_decision = input("   Do you want to exit? y/n ")
        if exiting_decision == "y" or exiting_decision == "Y":
            time.sleep(1)
            tr = False
            exit()
        else:
            print("   Ok, when you're ready exit by pressing 'CTRL'+'C' ")
            while True:
                pass
