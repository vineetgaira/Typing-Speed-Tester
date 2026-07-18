import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)
from src.passage import next_passage,index_difficulty,index_category, category_passage
from src.display import welcome,show_menu,show_passage,show_difficulty,show_category,show_results,goodbye

from src.statistics import count_errors,calculate_accuracy,calculate_cpm,calculate_wpm
from src.typing import get_user_input
from src.timer import start_time,end_time, elapsed_time
from src.utils import clear_screen, pause


def play_game():
    while True:
        clear_screen()
        welcome()
        show_menu()
        choice=select_from_menu()
        if choice==1:
            clear_screen()
            show_difficulty()
            difficulty_choices=select_difficulty()
            difficulty=index_difficulty[difficulty_choices]
            passage=next_passage(difficulty)
            clear_screen()
            show_passage(passage)
            start=start_time()
            user_input_difficulty=get_user_input(passage)
            end=end_time()
            time=elapsed_time(start,end)
            errors=count_errors(passage,user_input_difficulty)
            wpm=calculate_wpm(user_input_difficulty,time)
            cpm=calculate_cpm(user_input_difficulty,time)
            accuracy=calculate_accuracy(user_input_difficulty,errors)
            show_results(wpm,cpm,accuracy)
            pause()
            

        elif choice==2:
            clear_screen()
            show_category()
            category_choices=select_category()
            category=index_category[category_choices]
            passage=category_passage(category)
            clear_screen()
            show_passage(passage)
            start=start_time()
            user_input_category=get_user_input(passage)
            end=end_time()
            time=elapsed_time(start,end)
            errors=count_errors(passage,user_input_category)
            wpm=calculate_wpm(user_input_category,time)
            cpm=calculate_cpm(user_input_category,time)
            accuracy=calculate_accuracy(user_input_category,errors)
            show_results(wpm,cpm,accuracy)
            pause()
            
        else:
            goodbye()
            return
        
def select_from_menu():

    valid_choices={1,2,3}
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

