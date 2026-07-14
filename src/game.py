def play_game():
    pass

def main_menu():
    pass

def select_category():

    valid_choices={}
    while True:
        try:
            user_choice=int(input("Select category: "))
            if user_choice in valid_choices:
                return user_choice
            else:
                print("Please select a valid number.")
        except ValueError:
            print("Please select a valid integer.")


def select_difficulty():
    valid_choices={1,2,3}
    while True:
        try:
            user_choice=int(input("Select difficulty: "))
            if user_choice in valid_choices:
                return user_choice
            else:
                print("Please select a valid number.")
        except ValueError:
            print("Please select a valid integer.")

def play_again():
    pass


