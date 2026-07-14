from src.passage import next_passage
from src.display import welcome,show_menu,show_passage
from src.game import select_category,select_difficulty,play_again
from src.typing import get_user_input
from src.timer import start_time,end_time,elapsed_time

def main():
    start=start_time()
    passage=next_passage()
    show_passage(passage)
    end=end_time()
    print(elapsed_time(start,end))

if __name__ == "__main__":
    main()