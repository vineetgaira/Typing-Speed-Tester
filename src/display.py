import textwrap
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


BANNER=r""" _____          _             ___                  _   _____       _
|_   _|  _ _ __(_)_ _  __ _  / __|_ __  ___ ___ __| | |_   _|__ __| |_ ___ _ _
  | || || | '_ \ | ' \/ _` | \__ \ '_ \/ -_) -_) _` |   | |/ -_|_-<  _/ -_) '_|
  |_| \_, | .__/_|_||_\__, | |___/ .__/\___\___\__,_|   |_|\___/__/\__\___|_|
      |__/|_|         |___/      |_|
"""

def welcome():
    print(Fore.CYAN + BANNER)
    print(Fore.YELLOW + Style.BRIGHT + " " * 20 )

def show_menu():

    print(Fore.MAGENTA + "=" * 46)
    print(Fore.GREEN + Style.BRIGHT + "               MAIN MENU")
    print(Fore.MAGENTA + "=" * 46)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Select Difficulty (Easy / Medium / Hard)")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Select Category")
    print(Fore.WHITE + "  [3] " + Fore.RED + "Exit")


def show_difficulty():
    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "      DIFFICULTY MENU")
    print(Fore.MAGENTA + "=" * 26)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "Easy")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "Medium")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Hard")

    print(Fore.MAGENTA + "=" * 26)

def show_category():

    print(Fore.MAGENTA + "=" * 26)
    print(Fore.GREEN + Style.BRIGHT + "      CATEGORY MENU")
    print(Fore.MAGENTA + "=" * 26)

    print(Fore.WHITE + "  [1] " + Fore.CYAN + "General Knowledge")
    print(Fore.WHITE + "  [2] " + Fore.CYAN + "History")
    print(Fore.WHITE + "  [3] " + Fore.CYAN + "Literature")
    print(Fore.WHITE + "  [4] " + Fore.CYAN + "Programming")
    print(Fore.WHITE + "  [5] " + Fore.CYAN + "Quotes")
    print(Fore.WHITE + "  [6] " + Fore.CYAN + "Science")

    print(Fore.MAGENTA + "=" * 26)

def show_passage(passage):

    wrapped_text = textwrap.fill(passage, width=70)
    print(Fore.LIGHTBLUE_EX+wrapped_text)

def show_results(wpm,cpm,accuracy):
    print(Fore.WHITE + "  WPM :" + Fore.CYAN + f"{wpm}")
    print(Fore.WHITE + "  CPM :" + Fore.CYAN + f"{cpm}")
    print(Fore.WHITE + "  ACCURACY :" + Fore.CYAN + f"{int(accuracy)}%")

def show_best_score():
    pass

def goodbye():
    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"Thanks for playing...."+Style.RESET_ALL)

