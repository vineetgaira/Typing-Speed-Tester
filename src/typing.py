import textwrap

def get_user_input(passage):
    user_input=input("Enter the above passage:")
    if len(user_input)>len(passage):
        print("You have wrote the whole passage.")
    return user_input

