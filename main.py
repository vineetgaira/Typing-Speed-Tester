from src.passage import load_passages
from src.display import show_passage
import textwrap
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def main():
    passage= load_passages()
    show_passage(passage)

if __name__ == "__main__":
    main()