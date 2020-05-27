def Exiting():
    import time
    while True:
        exiting = input("   Do you want to exit? y/n ")
        if exiting == "y" or exiting == "Y":
            time.sleep(1)
            tr = False
            exit()
        else:
            print("   Ok, when you're ready exit by pressing 'CTRL'+'C' ")
            while True:
                pass
