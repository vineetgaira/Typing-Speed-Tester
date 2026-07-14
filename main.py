from src.passage import next_passage
from src.display import welcome,show_menu,show_passage
from src.game import select_difficulty
from src.typing import get_user_input

def main():
    passage=next_passage()
    show_passage(passage)
    get_user_input(passage)

if __name__ == "__main__":
    main()