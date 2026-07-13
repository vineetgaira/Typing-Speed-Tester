import textwrap
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def welcome():
    print(Fore.LIGHTBLUE_EX+r""" _____          _             ___                  _   _____       _
|_   _|  _ _ __(_)_ _  __ _  / __|_ __  ___ ___ __| | |_   _|__ __| |_ ___ _ _
  | || || | '_ \ | ' \/ _` | \__ \ '_ \/ -_) -_) _` |   | |/ -_|_-<  _/ -_) '_|
  |_| \_, | .__/_|_||_\__, | |___/ .__/\___\___\__,_|   |_|\___/__/\__\___|_|
      |__/|_|         |___/      |_|
""")

def show_menu():
    print(Fore.LIGHTBLUE_EX+r"""
==============================================
                MAIN MENU
==============================================
  [1] Start Typing Test
  [2] Select Difficulty (Easy / Medium / Hard)
  [3] View High Scores
  [4] View History
  [5] Exit
==============================================

""")

def show_passage(passage):

    wrapped_text = textwrap.fill(passage, width=70)
    print(Fore.LIGHTBLUE_EX+wrapped_text)

def show_results():
    pass

def show_best_score():
    pass

def goodbye():
    pass

