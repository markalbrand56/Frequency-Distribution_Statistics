from colorama import Fore, Back, Style


class Colors:
    def __init__(self):
        pass

    def RED(self):
        print(Fore.RED)

    def BLUE(self):
        print(Fore.BLUE)

    def GREEN(self):
        print(Fore.GREEN)

    def RESET(self):
        print(Style.RESET_ALL)
