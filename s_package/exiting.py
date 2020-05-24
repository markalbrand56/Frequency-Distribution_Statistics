def Exiting():
    while True:
        exiting = input("   Do you want to exit? y/n ")
        if exiting == "y" or exiting == "Y":
            tr = False
            break
        else:
            print("   Ok, when you're ready exit by pressing 'CTRL'+'C' ")
            while True:
                pass