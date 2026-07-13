import textwrap
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def welcome():
    pass

def show_menu():
    pass

def show_passage(passage):

    wrapped_text = textwrap.fill(passage, width=70)
    print(Fore.GREEN+wrapped_text)

def show_results():
    pass

def show_best_score():
    pass

def goodbye():
    pass

