import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)
from src.passage import next_passage,index_difficulty,index_category, category_passage
from src.display import welcome,show_menu,show_passage,show_difficulty,show_category,show_results

from src.statistics import count_errors,calculate_accuracy,calculate_cpm,calculate_wpm
from src.typing import get_user_input
from src.timer import start_time,end_time, elapsed_time


def play_game():
    while True:
        welcome()
        show_menu()
        choice=select_from_menu()
        if choice==1:
            passage=next_passage("easy")
            show_passage(passage)
            start=start_time()
            user_input=get_user_input(passage)
            end=end_time()
            time=elapsed_time(start,end)
            errors=count_errors(passage,user_input)
            wpm=calculate_wpm(passage,time)
            cpm=calculate_cpm(passage,time)
            accuracy=calculate_accuracy(user_input,errors)
            show_results(wpm,cpm,accuracy)

        elif choice==2:
            show_difficulty()
            difficulty_choices=select_difficulty()
            difficulty=index_difficulty[difficulty_choices]
            passage=next_passage(difficulty)
            show_passage(passage)
            start=start_time()
            user_input_difficulty=get_user_input(passage)
            end=end_time()
            time=elapsed_time(start,end)
            count_errors(passage,user_input_difficulty)
            wpm=calculate_wpm(passage,time)
            cpm=calculate_cpm(passage,time)
        elif choice==3:
            show_category()
            category_choices=select_category()
            category=index_category[category_choices]
            passage=category_passage(category)
            show_passage(passage)
            start=start_time()
            user_input_category=get_user_input(passage)
            end=end_time()
            time=elapsed_time(start,end)
            count_errors(passage,user_input_category)
            
        elif choice==6:
            print(Fore.GREEN+Style.BRIGHT+"Thanks for playing...")
            return
        else:
            print(Fore.GREEN+Style.BRIGHT+"Coming soon...")
        

def main_menu():
# This should only print the main menu 
    pass
    
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
