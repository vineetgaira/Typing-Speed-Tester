import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)
from src.passage import next_passage,index_difficulty,index_category
from src.display import welcome,show_menu,show_passage,show_difficulty,show_category

from src.statistics import count_errors
from src.typing import get_user_input
from src.timer import start_time,end_time,elapsed_time


def play_game():
    pass

def main_menu():
# This should only print the main menu 
    show_menu()
    choice=select_from_menu()
    
    return choice
        
    
def select_from_menu():

    valid_choices={1,2,3,4,5,6}
    while True:
        try:
            choice=int(input(Fore.GREEN + Style.BRIGHT + "Enter your choice: "+Style.RESET_ALL))
            if choice in valid_choices:
                return choice
            else:
                print(Fore.RED+"Please select a valid number.")
        except ValueError:
            print(Fore.RED+"Please select a valid integer.")
    
def select_category():

    valid_choices={1,2,3,4,5,6}
    while True:
        try:
            user_choice=int(input(Fore.GREEN+Style.BRIGHT+"Select category: "+Style.RESET_ALL))
            if user_choice in valid_choices:
                return user_choice
            else:
                print(Fore.RED+"Please select a valid number.")
        except ValueError:
            print(Fore.RED+"Please select a valid integer.")

def select_difficulty():
    valid_choices={1,2,3}
    while True:
        try:
            user_choice=int(input(Fore.GREEN+Style.BRIGHT+"Select difficulty: "+Style.RESET_ALL))
            if user_choice in valid_choices:
                return user_choice
            else:
                print(Fore.RED+"Please select a valid number.")
        except ValueError:
            print(Fore.RED+"Please select a valid integer.")

def play_again():

    while True:
        user_exit=input(Fore.GREEN+Style.BRIGHT+"Do you wanna try again? y/n :"+Style.RESET_ALL)
        if user_exit=="y":
            return True
        elif user_exit=="n":
            return False
        else:
            print(Fore.RED+"Please enter a valid choice(y/n).")
