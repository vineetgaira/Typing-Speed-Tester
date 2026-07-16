import os
from colorama import Fore, Style

def clear_screen():
   
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    pause=input(Fore.CYAN+Style.BRIGHT+"Press enter to continue..."+Style.RESET_ALL)

def exit_program():
   pass
