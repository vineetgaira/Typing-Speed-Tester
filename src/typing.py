import textwrap
import colorama
from colorama import Fore

def get_user_input(passage):
    user_input=input(Fore.BLUE+"Enter the above passage:")
    if len(user_input)>len(passage):
        print(Fore.RED+"You have wrote the whole passage.")
    return user_input

