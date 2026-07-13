from src.passage import load_passages
from src.display import show_passage


def main():
    passage= load_passages()
    show_passage(passage)

if __name__ == "__main__":
    main()