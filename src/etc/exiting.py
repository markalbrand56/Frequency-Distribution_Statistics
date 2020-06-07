def exiting():
    import time
    from src.etc.colors import Colors
    from main import main as main_app
    text_color = Colors()
    while True:
        text_color.RED()
        exiting_decision = input(" The program has ended. Do you want to exit? y/n ")
        if exiting_decision == "Y" or exiting_decision == "y":
            time.sleep(1)
            text_color.RESET()
            exit()
        else:
            returning_decision = input("  Do you want to return to the main menu? y/n ")
            returning_decision = returning_decision.lower()
            if returning_decision == 'y':
                text_color.RESET()
                main_app()
            else:
                print("   Ok, when you're ready, exit by pressing 'CTRL'+'C' ")
                text_color.RESET()
                time.sleep(0.5)
                main_app()
                while True:
                    pass
