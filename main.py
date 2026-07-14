from src.passage import next_passage
from src.display import welcome,show_menu,show_passage,show_difficulty,show_category

from src.game import select_category,select_difficulty,play_again
from src.typing import get_user_input
from src.timer import start_time,end_time,elapsed_time

def main():
    show_difficulty()
    show_category()
if __name__ == "__main__":
    main()