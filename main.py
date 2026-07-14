from src.passage import next_passage
from src.display import welcome,show_menu,show_passage,show_difficulty,show_category

from src.game import select_category,select_difficulty,play_again,select_from_menu
from src.statistics import count_errors
from src.typing import get_user_input
from src.timer import start_time,end_time,elapsed_time

def main():

    passage=next_passage()
    show_passage(passage)
    user_input=get_user_input(passage)
    print(count_errors(passage,user_input))
    



  
if __name__ == "__main__":
    main()