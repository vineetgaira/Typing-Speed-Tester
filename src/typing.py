from colorama import Fore, Style

def get_user_input(passage):
    user_input=input(Fore.GREEN+Style.BRIGHT+"Enter the above passage:"+Style.RESET_ALL)
    if len(user_input)>len(passage):
        print(Fore.RED+"You have wrote the whole passage.")
    return user_input

