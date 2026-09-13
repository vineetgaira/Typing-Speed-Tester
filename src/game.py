import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)
from src.passage import next_passage, category_passage
from src.display import welcome,show_menu,show_passage,show_difficulty,show_category,show_results,goodbye
from src.constants import MENU_CHOICES, index_category, index_difficulty
from src.statistics import count_errors,calculate_accuracy,calculate_cpm,calculate_wpm
from src.typing import get_user_input
from src.timer import start_time,end_time, elapsed_time
from src.utils import clear_screen, pause, show_error


def run_round(passage):
    clear_screen()
    show_passage(passage)
    start = start_time()
    user_input = get_user_input(passage)
    end = end_time()
    time = elapsed_time(start, end)

    errors = count_errors(passage, user_input)
    wpm = calculate_wpm(user_input, time)
    cpm = calculate_cpm(user_input, time)
    accuracy = calculate_accuracy(user_input, errors)

    show_results(wpm, cpm, accuracy)
    pause()


def play_game():
    while True:
        clear_screen()
        welcome()
        show_menu()
        choice = menu_choice(MENU_CHOICES, "Choice: ")

        if choice == "difficulty":
            clear_screen()
            show_difficulty()
            difficulty_choice = menu_choice(index_difficulty, "Choice: ")
            passage = next_passage(difficulty_choice)
            run_round(passage)

        elif choice == "category":
            clear_screen()
            show_category()
            category_choice = menu_choice(index_category, "Choice: ")
            passage = category_passage(category_choice)
            run_round(passage)

        else:
            goodbye()
            return
        
def menu_choice(options: dict, prompt : str ) -> str:
    valid_choices=set(options.keys())
    while True:
        try:
            choice=int(input(Fore.GREEN + Style.BRIGHT + prompt +Style.RESET_ALL))
            if choice in valid_choices:
                return options[choice]
            else:
                show_error("Please enter a valid number.")
        except ValueError:
            show_error("Please enter a valid integer.")
    
