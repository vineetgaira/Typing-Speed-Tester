def play_game():
    pass

def main_menu():
    pass

def select_category():

    valid_choices={1,2,3,4,5,6}
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

    while True:
        user_exit=input("Do you wanna try again? y/n :")
        if user_exit=="y":
            return True
        elif user_exit=="n":
            return False
        else:
            print("Please enter a valid choice(y/n).")

